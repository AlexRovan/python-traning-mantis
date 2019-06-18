# -*- coding: utf-8 -*-
import pytest
import json
import os.path
from fixture.application import Application
from fixture.orm import ORM_fixture

fixture = None
target = None


@pytest.fixture()
def app(request):
    global fixture
    global target

    browser = request.config.getoption("--browser")
    target = load_config(request.config.getoption("--target"))
    if fixture is None or not fixture.is_valid():
        fixture = Application(browser,target["web"]["baseUrl"])

    fixture.session.login_ensure(target["webadmin"]["username"], target["webadmin"]["password"])
    return fixture

@pytest.fixture(scope= "session")
def db (request):
    target=load_config(request.config.getoption("--target"))["db"]
    db_fixture = ORM_fixture(target["host"],target["database"],target["user"],target["password"])
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


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox")
    parser.addoption("--target", action="store", default="target.json")