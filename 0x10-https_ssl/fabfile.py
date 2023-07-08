# Install certbot, run it, replace the configuration file with new configuration
# restart load balancer

from fabric.api import *

env.user = 'ubuntu'

env.hosts = ['100.26.249.59']

def push_files():
    put("./certbot", "./")
    run("chmod 755 certbot")
    sudo("./certbot www.temz.tech temitopeabiodun685@gmail.com")
    put("./1-haproxy_ssl_termination", "./")
    sudo("cat 1-haproxy_ssl_termination > /etc/haproxy/haproxy.cfg")
    sudo("system haproxy restart")
