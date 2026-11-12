{%- target '/var/lib/cloud/seed/nocloud-net/meta-data' -%}
# Auto Generated During Install
instance-id: {{ _structure_config_uuid }}
local-hostname: {{ _hostname }}


apt:
{% if http_proxy %}
  proxy: {{ http_proxy }}
  http_proxy: {{ http_proxy }}
{% endif %}

{% endtarget %}
