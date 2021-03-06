{% if sol_console %}{% target '/etc/init/' + sol_console + '.conf' %}# Auto Generated During Install

# {{ sol_console }} - getty

start on stopped rc RUNLEVEL=[2345] and (
            not-container or
            container CONTAINER=lxc or
            container CONTAINER=lxc-libvirt)

stop on runlevel [!2345]

respawn
exec /sbin/getty -8 115200 {{ sol_console }}
{% endtarget %}{% endif %}

