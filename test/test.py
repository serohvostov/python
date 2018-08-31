# -*- coding: utf-8 -*-
import pytest
from model.site_class import SiteClass
from fixture.application import Application


@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.tearDown)
    return fixture


def test_test(app):
    # открытие сайта
    app.open_browser()
    app.loginn.login(SiteClass("demo-admin", "https://www.google.kz"))
    app.loginn.link(SiteClass("demo-admin", "https://www.google.kz"))


def test_test2(app):
    # открытие сайта
    app.open_browser()
    app.loginn.login(SiteClass("demo-admin", "https://www.google.kz"))
    app.loginn.link(SiteClass("demo-admin", "https://www.google3333.kz"))
