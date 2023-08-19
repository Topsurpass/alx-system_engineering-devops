#from fabric.api import run, local, sudo
from fabric.api import *

env.user = 'ubuntu'

#env.hosts = ['54.146.64.168']
env.hosts = ['54.237.54.19']

#copy file to remote current working directory
def push_files():
    put("../AirBnB_clone_v2", "./")

#copy the nginx default file to local server
def download():
    #get("/etc/nginx/sites-available/default", "./")
    get("./default", "./")

#run puppet on remote server
def execute_file():
    sudo("puppet apply 101-setup_web_static.pp")

#execute both program concurrently
def total():
    push_files()
    execute_file()

#restart nginx
def restart():
    sudo("systemctl restart nginx")

