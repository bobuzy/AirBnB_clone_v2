#!/usr/bin/python3

from fabric.api import *
from datetime import datetime

def do_pack():
    """Create a .tgz archive from the contents of the web_static folder."""

    # Get the cuttent time and convert it to a string
    time = datetime.now()
    formatted_time = time.strftime('%Y%m%d%H%M%S')

    # Create the versions folder (in the local machine) if it doesn't exist
    local('mkdir -p versions')

    # Compress the web_static folder and name it using the current time
    archive = "versions/web_static_{}.tgz".format(formatted_time) 
    result = local('tar -czf {} web_static'.format(archive))

    # Return the archieve path if it was created successfully
    if result.ok:
        return archive
    else:
        return None
