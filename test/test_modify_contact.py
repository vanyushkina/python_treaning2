from model.contact import Contact


def test_modify_first_contact_firstname(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Nick"))
    app.contact.modify_first_contact(Contact(firstname="Masha"))


def test_modify_first_contact_lastname(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(lastname="Frolov"))
    app.contact.modify_first_contact(Contact(lastname="Semenova"))
