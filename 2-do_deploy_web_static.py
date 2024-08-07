#!/usr/bin/python3
"""
Fabric script to distribute archive to the web servers
"""
from fabric.api import *
from os.path import exists

env.hosts = ['54.237.36.103', '100.24.74.195']
env.user = 'ubuntu'


def do_deploy(archive_path):
    """
    Decompress and distribute archive to web servers.

    Args:
        archive_path (str): Path to the archive file to be deployed.

    Returns:
        bool: True if the deployment was successful, False otherwise.
    """
    if exists(archive_path) is False:
        return False
    try:
        file_n = archive_path.split("/")[-1]
        no_ext = file_n.split(".")[0]
        path = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(path, no_ext))
        run('tar -xzf /tmp/{} -C {}{}/'.format(file_n, path, no_ext))
        run('rm /tmp/{}'.format(file_n))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, no_ext))
        run('rm -rf {}{}/web_static'.format(path, no_ext))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(path, no_ext))
        return True
    except:
        return False
