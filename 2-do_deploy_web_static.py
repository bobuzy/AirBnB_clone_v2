#!/usr/bin/python3
"""
Fabric script to decompress tgz archive passed
"""
from os.path import exists
from fabric.api import *
env.hosts = ['100.24.74.195', '54.237.36.103']


def do_deploy(archive_path):
    """Decompress archive_path passed"""
    if not exists(archive_path):
        return False

    try:
        put(archive_path, '/tmp/')
        folder_exe = archive_path.split("/")[-1]
        folder_name = folder_exe.split(".")[0]
        destination = '/data/web_static/releases/'
        run('mkdir -p {}{}/'.format(destination, folder_name))
        run('tar -xzf /tmp/{} -C {}{}/'.format(folder_exe,
                                               destination, folder_name))
        run('rm /tmp/{}'.format(folder_exe))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(destination,
                                                    folder_name))
        run('rm -rf {}{}/web_static'.format(destination, folder_exe))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(destination,
                                                          folder_name))
        return True
    except:
        return False
