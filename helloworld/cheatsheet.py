{# Dictionary Items #}

<ul>
{% for key, value in dictionary.items %}
    <li><a href="{{key}}">{{value}}</a></li>
{% endfor %}
</ul>


{# define attribute in template #}
{% with i=1 %}

def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")