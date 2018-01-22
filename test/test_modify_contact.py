from model.contact import Contact


def test_modify_first_contact_firstname(app):
    app.contact.modify_first_contact(Contact(firstname="Masha"))


def test_modify_first_contact_lastname(app):
    app.contact.modify_first_contact(Contact(lastname="Semenova"))
