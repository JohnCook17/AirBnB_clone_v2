#!/usr/bin/python3

from os.path import exists
from os.path import isfile
from datetime import datetime
from fabric.api import local, put, run, env
from shlex import split

env.hosts = ['35.185.45.37', '34.74.14.46']


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

    if not archive_path:
        return False
    try:
        my_path = archive_path.split(".")[0]
        my_path = my_path.split("/")[1]
        put("{}".format(archive_path), "/tmp/{}.tgz".format(my_path))
        run("mkdir -p /data/web_static/releases/{}/".format(my_path))
        run("tar -xzf /tmp/{}.tgz -C /data/web_static/releases/{}/"
            .format(my_path, my_path))
        run("rm -r /tmp/{}.tgz".format(my_path))
        """
        run("rm -r /data/web_static/releases/{}/"
            .format(my_path))
        """
        run(("mv /data/web_static/releases/{}/web_static/*" +
            " /data/web_static/releases/{}/")
            .format(my_path, my_path))
        run(" rm -rf /data/web_static/releases/{}/web_static/current"
            .format(my_path))
        run("rm -rf /data/web_static/current")
        run("ln -s /data/web_static/releases/{}/ /data/web_static/current"
            .format(my_path))
        run("sudo service nginx restart")
        return True
    except:
        return False


def deploy():
    arch = do_pack()
    if arch is None:
        return False
    return do_deploy(arch)
