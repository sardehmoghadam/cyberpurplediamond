{# Dictionary Items #}

<ul>
{% for key, value in dictionary.items %}
    <li><a href="{{key}}">{{value}}</a></li>
{% endfor %}
</ul>


{# define attribute in template #}
{% with i=1 %}