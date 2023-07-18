#!/usr/bin/python3

"""
Install mysql 5.7 on both web servers
"""

from fabric.api import *

env.user = "ubuntu"
#env.hosts = ['54.237.54.19', '54.146.64.168']
env.hosts = ['54.237.54.19']

def copy_key():
    """Copy mysql repo publick key to server"""
    put("./signature.key", "./")

def add_ssh_pub():
    """Copy alx ssh public key to server"""
    put("./alx_pub_key", "./")
    run("cat alx_pub_key >> ./.ssh/authorized_keys")

def create_new_user():
    """Run sql script in create_user.sql file"""
    #put("./create_user.sql", "./")
    put("./replica.sql", "./")
    run("mysql -u root -p < ./replica.sql")

def create_new_table():
    """Create table in the database"""
    put("./create_table.sql", "./")
    run("mysql -u root -p < ./create_table.sql")

