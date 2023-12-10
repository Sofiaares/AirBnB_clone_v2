#!/usr/bin/python3
"""
script (based on the file 1-pack_web_static.py) that distributes
an archive to your web servers.
"""

from fabric.api import run, put, env
import os

def do_deploy(archive_path):
    if not os.path.exists(archive_path):
        return False

    filename = os.path.basename(archive_path)
    name_no_ext = filename.split('.')[0]

    try:
        put(archive_path, '/tmp/{}'.format(filename))
        run('mkdir -p /data/web_static/releases/{}/'.format(name_no_ext))
        run('tar -xzf /tmp/{} -C /data/web_static/releases/{}/'.format(filename, name_no_ext))
        run('rm /tmp/{}'.format(filename))

        # Merge directories recursively to avoid overwriting or conflicting with existing files
        run('rsync -av --ignore-existing /data/web_static/releases/{}/web_static/ /data/web_static/releases/{}/'.format(name_no_ext, name_no_ext))

        run('rm -rf /data/web_static/releases/{}/web_static'.format(name_no_ext))
        run('rm -rf /data/web_static/current')
        run('ln -s /data/web_static/releases/{}/ /data/web_static/current'.format(name_no_ext))

        return True

    except Exception as e:
        return False
