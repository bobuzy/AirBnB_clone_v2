#!/usr/bin/python3
"""
script that generates a .tgz archive from the contents of the web_static
"""
from fabric.api import *
from datetime import datetime


def do_pack():
    """generate tgz file"""
    now = datetime.now()
    archive = 'web_static_' + now.strftime("%Y%m%d%H%M%S") + '.' + 'tgz'

    local('mkdir -p versions')
    result = local('tar -cvzf versions/{} web_static'.format(archive))

    if result is not None:
        return archive
    else:
        return None
