# Tutorials

<ul>
	{% for item in site.data.samplelist.docs %}
        <a href="{{ item.url }}" class="btn">{{ item.pagetitle }}</a>
	{% endfor %}
</ul>
