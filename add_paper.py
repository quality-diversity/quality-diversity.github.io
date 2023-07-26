import sys
import os
import urllib, urllib.request
import yaml
import json
import xmltodict
from builtins import input

# check if there are any update on the remote and
os.system("git remote update")
command = os.popen("git status -uno --porcelain")
output = command.read()[:-1]
if output:
    print("\033[91m WARNING: There are currently either local or remote changes. Please pull/push before adding more papers:\033[0m")
    print(output)
    #exit()

for i in range(1, len(sys.argv)):
    paper_title = sys.argv[i]
    print(f"processing: {paper_title}")
    paper_title_nospace = "+".join( paper_title.split())

    # URL to get info from arxiv and crossref
    urlarxiv = f'http://export.arxiv.org/api/query?search_query=ti:{paper_title_nospace}&start=0&max_results=1&sortBy=relevance&sortOrder=ascending'
    urlcrossref = f'http://api.crossref.org/works?query.bibliographic="{paper_title_nospace}"&mailto=QD@imperial.ac.uk&rows=1'
    dataarxiv = urllib.request.urlopen(urlarxiv)
    datacrossref = urllib.request.urlopen(urlcrossref)

    #get data from arxiv and crossref
    crossrefdict = json.loads(datacrossref.read().decode("utf-8"))
    arxivdict = xmltodict.parse(dataarxiv.read().decode("utf-8"))["feed"]["entry"]


    # Asking the user if what we found is correct. 
    proceed_answer = input( f'\033[92m\t found and Arxiv and Cross ref (both should be the title you expect): \n\t{arxivdict["title"]} (arxiv)\n\t{crossrefdict["message"]["items"][0]["title"][0]} (crossref).\033[0m\n Correct and proceed?\n y(yes)|anything else to quit: \n')
    if proceed_answer != "y":
        print("\033[91m WARNING: Asked to not proceed. \033[0m")



    #get bib from DOI
    doi = crossrefdict["message"]["items"][0]["DOI"]
    bibaddress = f'http://api.crossref.org/works/{doi}/transform/application/x-bibtex'
    bib = urllib.request.urlopen(bibaddress).read().decode("utf-8")

    # Construct data structure required for the yml file
    data ={'paper': {'title':arxivdict['title'],
                     "authors": [arxivdict['author']["name"]] if isinstance(arxivdict['author'], dict) else [string["name"] for string in arxivdict['author']],
                     "year": int(arxivdict['published'][0:4]),
                     "pdfurl": next(item['@href'] for item in arxivdict['link'] if item.get('@title') == 'pdf'),
                     "abstract": arxivdict['summary'],
                     "bibtex": bib}
           }

    ## Adding the structure to the top of the file
    with open("_data/paperlist.yml", "r") as f:
        contents = f.readlines()
        contents.insert(1,"\n"+yaml.dump(data).split("\n",1)[1])
    with open("_data/paperlist.yml", "w") as f:
        contents = "".join(contents)
        f.write(contents)
    
    print(f'\033[92m{paper_title} added to _data/paperlist.yml. use git diff to double check edits before pushing.\033[0m')


