#!/usr/bin/python3
"""
Fabric script to genereate tgz archive from web_static folder
"""
from fabric.api import *
from datetime import datetime


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
