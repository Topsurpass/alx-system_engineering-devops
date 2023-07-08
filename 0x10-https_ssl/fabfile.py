#from fabric.api import run, local, sudo
from fabric.api import *

env.user = 'ubuntu'

env.hosts = ['100.26.249.59']

def push_files():
    put("./certbot", "./")
    put("./1-haproxy_ssl_termination", "./")
    sudo("cat 1-haproxy_ssl_termination > /etc/haproxy/haproxy.cfg")

def append():
    sudo("cat /etc/ssl/www.temz.tech/www.temz.tech.pem")
