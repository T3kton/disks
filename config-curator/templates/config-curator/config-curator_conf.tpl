{% target '/etc/config-curator.conf' %}# this file is auto generated by config-curator do not edit by hand
# generated at {{ __timestamp__ }}
# for {{ _hostname }}, uuid: {{ __uuid__ }}

[config]
config_host: {{ config_host }}
config_proxy: {{ config_proxy }}
uuid: {{ __uuid__ }}

{% endtarget %}