{# Copyright (C) 2019, Nokia #}
{{ "=" * e.attrib["type"]|length }}{{ "=" * e.attrib["name"]|length }}{{ "=" * 2 }}
{{ e.attrib["type"] }}: {{e.attrib["name"]}}
{{ "=" * e.attrib["type"]|length }}{{ "=" * e.attrib["name"]|length }}{{ "=" * 2 }}

:scope: {{ e.scope }}
:generated: {{ e.attrib["generated"] }}

{{ e.doc}}


{% for kw in  e.findall("kw") %}

{{ kw.attrib["name"]|title }}
{{ "=" * kw.attrib["name"]|title|length }}
.. py:function:: {{ kw.attrib["name"]|lower|replace(" ", "_") }}({{ kw.arguments.getchildren()|join(', ') }})

   {% if kw.doc.text %}
   {% for line in  kw.doc.text.splitlines(True) -%}
        {{ "   " }}{{ line }}
   {%- endfor %}
   {% else %}
   :todo: documentation
   {% endif %}


{% endfor %}

