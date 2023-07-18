#!/usr/bin/python3

"""
Install mysql 5.7 on both web servers
"""

from fabric.api import *

env.user = "ubuntu"
#env.hosts = ['54.237.54.19', '54.146.64.168']
env.hosts = ['54.146.64.168']
#env.hosts = ['54.237.54.19']

def copy_key():
    """Copy mysql repo publick key to server"""
    put("./signature.key", "./")

def add_ssh_pub():
    """Copy alx ssh public key to server"""
    put("./alx_pub_key", "./")
    run("cat alx_pub_key >> ./.ssh/authorized_keys")

def create_new_user():
    """Run sql script in create_user.sql file but replica user is
    only created on web-01 server alone"""
    put("./create_user.sql", "./")
    run("mysql -u root -p < ./create_user.sql")
    put("./replica.sql", "./")
    run("mysql -u root -p < ./replica.sql")

def create_new_table():
    """Create table in the database"""
    put("./create_table.sql", "./")
    run("mysql -u root -p < ./create_table.sql")

def copy_config():
    """Copy mysql primary configuration"""
    sudo("cp /etc/mysql/mysql.conf.d/mysqld.cnf ./")
    get("./mysqld.cnf", "./")
    local("cat mysqld.cnf > 4-mysql_configuration_replica")

def dwnld_file():
    get("./tyrell_corp.sql", "./")
    put("./tyrell_corp.sql", "/tmp/")

