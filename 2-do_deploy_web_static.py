#!/usr/bin/python3
"""
Fabric script that distributes an archive to your web servers
"""
from os.path import exists
from fabric.api import put
from fabric.api import run
from fabric.api import env
from fabric.api import sudo

env.hosts = ['34.203.31.100', '54.227.101.39']


def do_deploy(archive_path):
    """
    Distributes an archive to your web servers
    Returns False if the file at the path archive_path doesn't exist
    """
    if exists(archive_path) is False:
        return False
    try:
        filename = archive_path.split("/")[-1]
        unfile = filename[0:-4]
        path = "/data/web_static/releases/"
        put(archive_path, "/tmp/")
        run("sudo mkdir -p {}{}".format(path, unfile))
        run("sudo tar -xzf /tmp/{} -C {}{}".format(filename, path, unfile))
        run("sudo rm -rf /tmp/{}".format(filename))
        run("sudo mv {0}{1}/web_static/* {0}{1}/".format(path, unfile))
        run("sudo rm -rf {}{}/web_static".format(path, unfile))
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -s {}{}/ /data/web_static/current".format(path, unfile))
        sudo('service nginx restart')
        return True
    except Exception:
        return False
