#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from the contents
of the web_static folder of your AirBnB Clone repo
"""
from fabric.api import local
from datetime import datetime

def do_pack():
    """
    Create a .tgz archive from the web_static folder
    """
    # Get the current timestamp
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")

    # Create the versions directory if it doesn't exist
    local("mkdir -p versions")

    # Create the archive file
    result = local("tar -cvzf versions/web_static_{}.tgz web_static".format(timestamp))

    # Check if the archive was created successfully
    if result.succeeded:
        return "versions/web_static_{}.tgz".format(timestamp)
    else:
        return None
