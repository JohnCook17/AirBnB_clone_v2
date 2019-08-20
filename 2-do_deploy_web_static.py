#!/usr/bin/python3

from os.path import exists
from os.path import isfile
from datetime import datetime
from fabric.api import *
from shlex import split

env.hosts = ['35.196.125.111', '35.185.45.37']

def do_pack():

    files = "web_static"
    now = datetime.now()
    my_time = now.strftime("%Y%m%d%H%M%S")
    if exists("versions"):
        pass
    else:
        local('mkdir versions')
    local("tar cfvz versions/web_static_{}.tgz {}".format(my_time, files))
    if isfile("versions/web_static_{}.tgz".format(my_time)):
        return "versions/web_static_{}.tgz".format(my_time)
    else:
        return None

def do_deploy(archive_path):
    
    try:
        my_path = archive_path.split(".")[0]
        put("{}".format(archive_path), "/tmp")
        run("tar -xvf * -C /data/web_static/releases/{}".format(my_path))
        run("rm -r /tmp/{}".format(archive_path))
        run("ln -s /data/web_static/current /data/web_static/releases/{}".format(my_path))

        return True
    except:
        return False