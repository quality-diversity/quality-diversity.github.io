# List of papers

{{ site.data.paperlist.papers.size }} papers are listed. 

You can click on each title to display more information, including authors, url to pdf, abstract and bibtex. 

{% comment %} tags:
<span class="badge review">Review</span>
<span class="badge robotics">Robotics</span>
<span class="badge games">Games</span>
<span class="badge all">All</span> ––>
{% endcomment %}

{% assign paperlist = site.data.paperlist.papers | group_by: 'year' | sort:"name"  %}
{% for yeargroup in paperlist reversed %}
{% if yeargroup.name == "" %}
   <h3>Undated: {{ yeargroup.size }} Papers</h3>
{% else %}
   <h3>{{ yeargroup.name }}: {{ yeargroup.size }} Papers</h3>
{% endif %}
<ul>
	{% assign sortedgroup = yeargroup.items | sort:"title"  %}
	{% for item in sortedgroup %}
	{% if item.title %}
	<li>
		<details><summary><b>{{ item.title }}</b>
		{% if item.tags contains "review" %}<span class="badge review">Review</span>{% endif %}
		{% if item.tags contains "robotics" %}<span class="badge robotics">Robotics</span>{% endif %}
		{% if item.tags contains "games" %}<span class="badge games">Games</span>{% endif %}
		</summary>
		<blockquote>
		{% if item.authors %}
		   <h4>Authors:</h4>
		   <ul>
		   {% for author in item.authors %}
		      <li>{{ author }}</li>
		   {% endfor %}
		   </ul>
		{% endif %}

		{% if item.abstract %}
		   <h4>Abstract:</h4>
		   {{ item.abstract }}
		{% endif %}

		{% if item.pdfurl or item.codeurl or item.webpageurl %}
		   <h4>Links:</h4>
		   <ul>
		   {% if item.pdfurl %}
		   <li><a href="{{ item.pdfurl }}">Paper</a></li>
		   {% endif %}
		   {% if item.codeurl %}
		   <li><a href="{{ item.codeurl }}">Source-code</a></li>
		   {% endif %}
		   {% if item.webpageurl %}
		   <li><a href="{{ item.webpageurl }}">Webpage</a></li>
		   {% endif %}
		   </ul>
		{% endif %}

		{% if item.bibtex %}	 
		   <h4>Bibtex:</h4>
		   <pre><code>{{ item.bibtex }}</code></pre>
		{% endif %}

		<hr>
		
		 </blockquote>
		</details>
	</li>
	{% endif %}
	{% endfor %}
</ul>
{% endfor %}

