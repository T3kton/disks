{% set _reposets = {} %}
{% for repo in repo_list %}
{% if repo.type == 'apt' and repo.distribution %}
{% set key = ( repo.uri, repo.distribution, repo.arch, repo.key_file ) %}
{% if key in _reposets %}
{% do _reposets.__setitem__( key, _reposets[ key ] + repo.components ) %}
{% else %}
{% do _reposets.__setitem__( key, repo.components ) %}
{% endif %}
{% endif %}
{% endfor %}

{% set _entries = {} %}
{% for info, component_list in _reposets.items() %}
{% set component_list = component_list | unique_list | sort | tuple %}
{% set key = ( info[0], component_list, info[2], info[3] ) %}
{% if key in _entries %}
{% do _entries.__setitem__( key, _entries[ key ] + [ info[1] ] ) %}
{% else %}
{% do _entries.__setitem__( key, [ info[1] ] ) %}
{% endif %}
{% endfor %}

{% target '/etc/apt/sources.list.d/ubuntu.sources' %}# Auto Generated During Install

{% for info, distribution_list in _entries.items() %}
Types: deb
URIs: {{ info[0] }}
Suites:{% for distribution in distribution_list | unique_list | sort %} {{ distribution }}{% endfor %}
Components:{% for component in info[1] %} {{ component }}{% endfor %}
Signed-By: /usr/share/keyrings/{{ info[3] }}
{% if info[2] %}Architectures: {{ info[2] }}{% endif %}

{% endfor %}
{% endtarget %}
