#!/usr/bin/python3
"""
Fabric script that distributes an archive to your web servers
"""
from os.path import exists
from re import A
from fabric.api import put
from fabric.api import run
from fabric.api import env
from fabric.api import sudo
env.hosts = ['34.203.31.100', '54.227.101.39']


def do_deploy(archive_path):
    """Prototype: def do_deploy"""

    if exists(archive_path) is False:
        return False
    archive = archive_path.split('/')[1]
    put("archive_path", "/tmp/")
    run("mkdir -p /data/web_static/releases/{}".format(archive[0:-4]))
    run("tar -xzf /tmp/{} -C /data/web_static/releases/{}".fotmat(
        archive, archive[0:-4]))
    run("mv /data/web_static/releases/{}/web_static/*\
            /data/web_static/releases/{}/".format(
                archive[0:-4], archive[0:-4]))
    run("rm -rf /tmp/{}".format(archive))
    run("rm -f /data/web_static/releases/{}/web_static".fotmat(archive))
    run("rm /data/web_static/current")
    run("ln -s /data/web_static/releases/{}/ \
        /data/web_static/current".format(archive[0:-4]))
    sudo("service nginx restart")
    return True
