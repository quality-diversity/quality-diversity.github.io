import sys
import os
import urllib, urllib.request
import yaml
import json
import xmltodict
from builtins import input

def clean_string(string):
    return string.strip().replace("\n ", "").replace(":", "").replace("\u2013","–").replace("-","–")# replace utf-8 symbol (ndash) to ascii (-)

# check if there are any update on the remote and
os.system("git remote update")
command = os.popen("git status -uno --porcelain")
output = command.read()[:-1]
if output:
    print("\033[91m WARNING: There are currently either local or remote changes. Please pull/push before adding more papers:\033[0m")
    print(output)
    exit()

not_added=[]
    
for i in range(1, len(sys.argv)):
    paper_title = sys.argv[i].replace(":", "")
    print(f"\033[93mprocessing: {paper_title}\033[0m")
    paper_title_nospace = urllib.parse.quote_plus(paper_title)
    paper_title_nospace = paper_title_nospace.replace("-", "+")
    #print(paper_title_nospace)
    # URLs to get info from arxiv and crossref
    urlarxiv = f'http://export.arxiv.org/api/query?search_query=ti:{paper_title_nospace}&start=0&max_results=1&sortBy=relevance&sortOrder=ascending'
    urlcrossref = f'http://api.crossref.org/works?query.title="{paper_title_nospace}"&mailto=QD@imperial.ac.uk&rows=1'

    #get data from arxiv and crossref
    try:
        datacrossref = urllib.request.urlopen(urlcrossref)
        crossrefdict = json.loads(datacrossref.read().decode("utf-8-sig"))["message"]["items"][0]
        crossref_ok = clean_string(crossrefdict["title"][0]).lower() == clean_string(paper_title).lower()
        #print(clean_string(crossrefdict["title"][0]).lower())
        #print(clean_string(paper_title).lower())
    except Exception as e:
        print(e)
        
        print("\033[91m ERROR: retrieving info from crossref failed \033[0m")
        crossref_ok = False

    try:
        dataarxiv = urllib.request.urlopen(urlarxiv)
        arxivdict = xmltodict.parse(dataarxiv.read().decode("utf-8-sig"))["feed"]["entry"]
        arxiv_ok = clean_string(arxivdict["title"]).lower() == clean_string(paper_title).lower()
        #print(clean_string(arxivdict["title"]).lower())
        #print(clean_string(paper_title).lower())

    except Exception as e:
        print(e)
        
        print("\033[91m ERROR: retrieving info from Arxiv failed \033[0m")
        arxiv_ok = False
    # uncomment these prints if you want to see the content of what is obtained from arxiv or crossref
    #print(json.dumps(crossrefdict, indent=4))
    #print(json.dumps(arxivdict, indent=4))
    
    # Checking which source is correct, if not both

    if not arxiv_ok and not crossref_ok:
        print("\033[91m ERROR: paper not found on both arXiv and Crossref \033[0m")
        not_added.append(paper_title)
        continue
    
    if crossref_ok:
        #get bib from DOI
        doi = crossrefdict["DOI"]
        bibaddress = f'http://api.crossref.org/works/{doi}/transform/application/x-bibtex'
        bib = urllib.request.urlopen(bibaddress).read().decode("utf-8-sig")
    else: # arxiv_ok
        authors_str = ""
        first_lastname = ""
        for string in arxivdict['author']:
            names = string['name'].split(" ",1)
            if authors_str != "":
                authors_str += " and "
            if first_lastname == "":
                first_lastname = names[1]
            authors_str += names[1] + ", " + names[0]
            year = arxivdict['published'][0:4]
        bib = "@article{"+first_lastname+year+arxivdict['title'].split(" ",1)[0].strip(',')+",\n\ttitle={" + clean_string(arxivdict['title']) + "},\n\tauthor={" + authors_str +  "},\n\tjournal={arXiv preprint arXiv:"+ arxivdict['id'].split("/")[-1] + "},\n\tyear={" + year+"} }"

        
    # Construct data structure required for the yml file
    data ={'paper': [{'title':clean_string(arxivdict['title']) if arxiv_ok else clean_string(crossrefdict["title"][0]),
                     "authors": ([arxivdict['author']["name"]] if isinstance(arxivdict['author'], dict) else [string["name"] for string in arxivdict['author']]) if arxiv_ok else ([string["given"]+" "+string["family"] for string in crossrefdict['author']]),
                     "year": int(arxivdict['published'][0:4]) if arxiv_ok else crossrefdict["published"]["date-parts"][0][0],
                     "pdfurl": next(item['@href'] for item in arxivdict['link'] if item.get('@title') == 'pdf')  if arxiv_ok else crossrefdict["URL"],
                     "bibtex": bib}
                     ]
           }

    if arxiv_ok:
        data['paper'][0]["abstract"] = arxivdict['summary']

    print(json.dumps(data, indent=4))
    # Asking the user if what we found is correct. 
    proceed_answer = input( f'\033[92m\t The above information will be added to the file. Is this correct and shall we proceed?\n y(yes)|anything else to quit: \n')
    if proceed_answer != "y":
        print("\033[91m WARNING: Asked to not proceed. \033[0m")
        not_added.append(paper_title)
        continue

    
    ## Adding the structure to the top of the file
    with open("_data/paperlist.yml", "r") as f:
        contents = f.readlines()
        contents.insert(1,"\n"+yaml.dump(data).split("\n",1)[1])
    with open("_data/paperlist.yml", "w") as f:
        contents = "".join(contents)
        f.write(contents)
    
    print(f'\033[92m{paper_title} added to _data/paperlist.yml. use git diff to double check edits before pushing.\033[0m')


print(f'not added:\n {not_added}')
