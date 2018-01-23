# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    old_contact = app.contact.get_contact_list()
    app.contact.create(Contact(firstname="Anna", lastname="Orlova", mobile="64985587"))
    new_contact = app.contact.get_contact_list()
    assert len(old_contact) + 1 == len(new_contact)


def test_add_empty_contact(app):
    old_contact = app.contact.get_contact_list()
    app.contact.create(Contact(firstname="", lastname="", mobile=""))
    new_contact = app.contact.get_contact_list()
    assert len(old_contact) + 1 == len(new_contact)


