#!/usr/bin/python3
"""
Fabric script to distribute archive to the web servers
"""
from fabric.api import *
from os.path import exists
from datetime import datetime

env.hosts = ['54.237.36.103', '100.24.74.195']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/id_rsa'


def do_deploy(archive_path):
    """Decompress and distribute archive to web servers"""
    try:
        if not exists(archive_path):
            return False
        put(archieve_path, '/tmp/')

        timestamp = archive_path[-18:-4]
        sudo('mkdir -p /data/web_static/releases/
              webstatic_{}'.format(timestamp))
        sudo('tar -xzf /tmp/web_static_{0}.tgz -C /data/web_static/
              releases/web_static_{0}/'.format(timestamp))
        sudo('mv /data/web_static/releases/web_static_{0}/web_static/* \
/data/web_static/releases/web_static_{0}/'.format(timestamp))
        sudo('rm -rf /data/web_static/releases/\
web_static_{}/web_static'.format(timestamp))
        sudo('rm -rf /data/web_static/current')
        sudo('ln -s /data/web_static/releases/\
web_static_{}/ /data/web_static/current'.format(timestamp))
    except:
        return False

    return True
