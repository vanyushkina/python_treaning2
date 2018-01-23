from model.contact import Contact


def test_modify_first_contact_firstname(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Nick"))
    old_contact = app.contact.get_contact_list()
    app.contact.modify_first_contact(Contact(firstname="Masha"))
    new_contact = app.contact.get_contact_list()
    assert len(old_contact) == len(new_contact)


def test_modify_first_contact_lastname(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(lastname="Frolov"))
    old_contact = app.contact.get_contact_list()
    app.contact.modify_first_contact(Contact(lastname="Semenova"))
    new_contact = app.contact.get_contact_list()
    assert len(old_contact) == len(new_contact)
