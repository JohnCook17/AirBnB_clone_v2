#!/usr/bin/python3

from os.path import exists
from os.path import isfile
from datetime import datetime
from fabric.api import local

def do_pack():
    files = "web_static"
    now = datetime.now()
    my_time = now.strftime("%Y%m%d%H%M%S")
    print("now = {}".format(now))
    print("now = {}".format(my_time))
    if exists("versions"):
        pass
    else:
        local('mkdir versions')
    local("tar cfvz versions/web_static_{}.tgz {}".format(my_time, files))
    if isfile("versions/web_static_{}.tgz".format(my_time)):
        return "versions/web_static_{}.tgz".format(my_time)
    else:
        print("none")
        return None
