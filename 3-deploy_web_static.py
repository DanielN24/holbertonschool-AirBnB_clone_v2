#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from the contents of the
web_static folder of your AirBnB Clone repo, using the function do_pack
"""
from datetime import datetime
from fabric.api import local
from os.path import isdir
from os.path import exists
from fabric.api import put
from fabric.api import run
from fabric.api import env
from fabric.api import sudo

env.hosts = ['34.203.31.100', '54.227.101.39']


def do_pack():
    """generates a .tgz"""
    try:
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        if isdir("versions") is False:
            local("mkdir versions")
        file_name = "versions/web_static_{}.tgz".format(date)
        local("tar -cvzf {} web_static".format(file_name))
        return file_name
    except Exception:
        return None


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


def deploy():
    """deploy"""
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
