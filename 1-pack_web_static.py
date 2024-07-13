#!/usr/bin/env python3
"""
    Write a Fabric script that generates a .tgz archive from the contents of
    the web_static folder of your AirBnB Clone repo, using the function do_pack
    All files in the folder web_static must be added to the final archive
    All archives must be stored in the folder versions (your function should
    also create this folder if it doesn’t exist)
    The name of the archive created must be
    web_static_<year><month><day><hour><minute><second>.tgz
    The function do_pack must return the archive path if the archive has been
    created correctly generated. Otherwise, it should return None
"""
from fabric.api import local, lcd
from datetime import datetime
import os


def do_pack():
    """ generates a .tgz archive from the contents of the web_static folder
    """
    try:
        local("mkdir -p versions")
        time_stamp = datetime.now().strftime("%Y%m%d%H%M%S")
        archive_name = "versions/web_static_" + time_stamp + ".tgz"
        print(f"Packing web_static to {archive_name}")
        local(f"tar -cvzf {archive_name} web_static")
        archive_size = os.path.getsize(archive_name)
        print(f"web_static packed: {archive_name} -> {archive_size} bytes")
    except Exception:
        return None


if __name__ == "__main__":
    do_pack()
