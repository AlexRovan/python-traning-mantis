# -*- coding: utf-8 -*-
import pytest
import json
import os.path
from fixture.application import Application
from fixture.orm import ORM_fixture
import ftputil

fixture = None
target = None


@pytest.fixture(scope= "session")
def config(request):
    return load_config(request.config.getoption("--target"))


@pytest.fixture()
def app(request,config):
    global fixture

    browser = request.config.getoption("--browser")
    if fixture is None or not fixture.is_valid():
        fixture = Application(browser,config)

    #fixture.session.login_ensure(config["webadmin"]["username"], config["webadmin"]["password"])
    return fixture


@pytest.fixture(scope= "session")
def db (config):
    db_fixture = ORM_fixture(config["db"]["host"],config["db"]["database"],config["db"]["user"],config["db"]["password"])
    return db_fixture


@pytest.fixture(scope = "session",autouse = True)
def stop(request):

    def fin():
        fixture.session.logout_ensure()
        fixture.destroy()

    request.addfinalizer(fin)


def load_config(file):
    global target
    if target is None:
        config_path =os.path.join(os.path.dirname(os.path.abspath(__file__)), file)
        with open(config_path) as configfile:
            target = json.load(configfile)
    return target

@pytest.fixture(scope = "session",autouse = True)
def server_config(request,config):
    install_server_config(config["ftp"]["host"],config["ftp"]["username"],config["ftp"]["password"])
    def fin():
        restore_server_config(config["ftp"]["host"],config["ftp"]["username"],config["ftp"]["password"])
    request.addfinalizer(fin)


def install_server_config(host,user,pwd):
    with ftputil.FTPHost(host,user,pwd) as remote:
        if remote.path.isfile("config_inc.php.bak"):
            remote.remove("config_inc.php.bak")
        if remote.path.isfile("config_inc.php"):
            remote.rename("config_inc.php","config_inc.php.bak")
        remote.upload(os.path.join(os.path.dirname(__file__),"resource/config_inc.php"),"config_inc.php")


def restore_server_config(host,user,pwd):
    with ftputil.FTPHost(host,user,pwd) as remote:
        if remote.path.isfile("config_inc.php.bak"):
            if remote.path.isfile("config_inc.php"):
                remote.remove("config_inc.php")
            remote.rename("config_inc.php.bak","config_inc.php")


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox")
    parser.addoption("--target", action="store", default="target.json")