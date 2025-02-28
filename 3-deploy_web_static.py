#!/usr/bin/python3
""" AirBnB clone - Deploy static using fabric """

from datetime import datetime
from fabric.api import *
import os

env.hosts = ['54.197.44.197', '34.207.227.83']
env.user = "ubuntu"


def do_pack():
    """
    Returns the archive path if archive has been
    correctly gernerated else return None
    """

    local("mkdir -p versions")
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    archive_pathh = "versions/web_static_{}.tgz".format(date)
    tgz_archive = local("tar -cvzf {} web_static".format(archive_pathh))

    if tgz_archive.succeeded:
        return archive_pathh
    else:
        return None


def do_deploy(archive_path):
    """
    Fabric script that distributes an archive to your web servers,
    using the function
    """
    if os.path.exists(archive_path):
        archive_file = archive_path[9:]
        newfileversion = "/data/web_static/releases/" + archive_file[:-4]
        archive_file = "/tmp/" + archive_file

        put(archive_path, "/tmp/")
        run("sudo mkdir -p {}".format(newfileversion))

        run("sudo tar -xzf {} -C {}/".format(archive_file, newfileversion))
        run("sudo rm -rf {}".format(archive_file))
        run("sudo mv {}/web_static/* {}".format(newfileversion,
                                                newfileversion))

        run("sudo rm -rf {}/web_static".format(newfileversion))
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -s {} /data/web_static/current".format(newfileversion))

        print("New version deployed!")
        return True

    return False


def deploy():
    """
    creates and distributes an archive to your web servers
    """
    archivePath = do_pack
    if path:
        do_deploy(archivePath)
    else:
        return False
