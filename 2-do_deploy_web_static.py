#!/usr/bin/python3
"""
    A fabric script (based on the file 1-pack_web_static.py) that distributes
    an archive to a web server, using the function do_deploy:
    - Return False if the file at the path archive_path dosen't exist
    - Uploading the archive to the /tmp/ directory of the web server
    - Decompressing the archive to the folder
        /data/web_static/releases/<archive filename without extension>
        on the web server
    - Deleting the archive from the web server
    - Deleting the symbolic link /data/web_static/current from the web server
    - Creating a new symbolic link /data/web_static/current on the new web
        server, linked to the new version of the code
        /data/web_static/releases/<archive filename without extension>
    - All remote commands must be executed on both servers
    - Return True if all operation have been done correctly, False otherwise.
    """
from fabric.api import env, put, run, sudo
import os.path


env.hosts = ['3.95.32.114', '100.26.238.118']


def do_deploy(archive_path):
    """Deploying an archive to a web server"""
    if not os.path.exists(archive_path):
        return False

    try:
        # uploading the archive to the /tmp/
        put(archive_path, "/tmp/")

        file_name = os.path.basename(archive_path)
        folder_name = file_name.split('.')[0]
        release_folder = f"/data/web_static/releases/{folder_name}"

        # decompressing the archive folder
        run(f"mkdir -p /data/web_static/releases/{folder_name}/")
        run(f"tar xzf /tmp/{file_name} -C {release_folder}")

        # deleting the archive from the web server
        sudo(f"rm /tmp/{file_name}")

        # move file to correct location
        sudo(f"mv {release_folder}/web_static/* {release_folder}")
        sudo(f"rm -rf {release_folder}/web_static")

        # deleting older symbolic link
        sudo("rm /data/web_static/current")

        # Creating a new symbolic link
        sudo(f"ln -s {release_folder} /data/web_static/current")

        sudo("systemctl restart nginx")
        return True

    except Exception as e:
        print(e)
        return False
