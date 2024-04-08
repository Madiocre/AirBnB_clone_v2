#!/usr/bin/python3
""" This module contains the function do_pack that generates a .tgz archive
  from the contents of the web_static folder (fabric script) """
from fabric.api import *
from datetime import datetime


def do_pack():
    """ Fabric script that generates a .tgz archive from the contents of the...
    ...web_static folder """
    local("sudo mkdir -p versions")
    time = datetime.now().strftime("%Y%m%d%H%M%S")
    data = "versions/web_static_{}.tgz".format(time)
    result = local("sudo tar -cvzf {} web_static".format(data))
    if result.succeeded:
        return data
    else:
        return None
