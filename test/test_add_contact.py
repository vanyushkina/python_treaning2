# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    app.contact.create(Contact(firstname="Anna", lastname="Orlova", mobile="64985587"))


def test_add_empty_contact(app):
    app.contact.create(Contact(firstname="", lastname="", mobile=""))

