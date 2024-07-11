#!/usr/bin/python3
"""
Fabric script based on the 1-pack_web_static.py and 2-do_deploy_web_static.p
that creates and distributes an archive to the web servers
"""

from fabric.api import env, local, put, run
from datetime import datetime
from os.path import exists, isdir
env.hosts = ['54.237.36.103', '100.24.74.195']

def do_pack():
    """Create a .tgz archive from the contents of the web_static folder"""
    time = datetime.now()
    formatted_time = time.strftime('%Y%m%d%H%M%S')

    local('mkdir -p versions')

    archive = "versions/web_static_{}.tgz".format(formatted_time)
    result = local('tar -cvzf {} web_static'.format(archive))

    if result.ok:
        return archive
    else:
        return None

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

def deploy():
        """Deploy web static"""
        return do_deploy(do_pack())
