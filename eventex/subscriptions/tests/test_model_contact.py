from django.test import TestCase
from django.core.exceptions import ValidationError

from eventex.core.models import Speaker, Contact


class ContactModelTest(TestCase):
    def setUp(self):
        self.speaker = Speaker.objects.create(
            name='Guilherme Bagnato',
            slug='guilherme-bagnato',
            photo='http://hbn.link/hb-pic'
        )

    def test_email(self):
        contact = Contact.objects.create(
            speaker=self.speaker,
            kind=Contact.EMAIL,
            value='gui.bagnato@gmail.com',
        )

        self.assertTrue(Contact.objects.exists())

    def test_phone(self):
        contact = Contact.objects.create(
            speaker=self.speaker,
            kind=Contact.PHONE,
            value='11-1234567',
        )

        self.assertTrue(Contact.objects.exists())

    def test_choices(self):
        """Contact kid should be limited to E or P"""
        contact = Contact(speaker=self.speaker, kind='A', value='B')
        self.assertRaises(ValidationError, contact.full_clean)

    def test_str(self):
        contact = Contact(
            speaker=self.speaker,
            kind=Contact.EMAIL,
            value='gui.bagnato@gmail.com',
        )
        self.assertEqual('gui.bagnato@gmail.com', str(contact))


class ContactManagerTest(TestCase):
    def setUp(self):
        s = Speaker.objects.create(
            name='Guilherme Bagnato',
            slug='guilherme-bagnato',
            photo='http://hbn.link/hb-pic'
        )

        s.contact_set.create(kind=Contact.EMAIL, value='gui.bagnato@gmail.com')
        s.contact_set.create(kind=Contact.PHONE, value='11123456789')

    def test_mails(self):
        qs = Contact.objects.emails()
        expected = ['gui.bagnato@gmail.com']
        self.assertQuerysetEqual(qs, expected, lambda o: o.value)

    def test_phones(self):
        qs = Contact.objects.phones()
        expected = ['11123456789']
        self.assertQuerysetEqual(qs, expected, lambda o: o.value)
