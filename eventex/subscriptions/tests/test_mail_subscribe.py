from django.core import mail
from django.test import TestCase


class SubscribePostValid(TestCase):
    def setUp(self):
        data = dict(name='Guilherme Bagnato', cpf='12345678901',
                    email='gui.bagnato@gmail.com', phone='16-9911-4332')
        self.client.post('/inscricao/', data)
        self.email = mail.outbox[0]

    def test_subscription_email_subject(self):
        expect = 'Confirmação de inscrição'

        self.assertEqual(expect, self.email.subject)

    def test_subscription_email_from(self):
        expect = 'contato@eventex.com.br'

        self.assertEqual(expect, self.email.from_email)

    def test_subscription_email_to(self):
        expect = ['contato@eventex.com.br', 'gui.bagnato@gmail.com']

        self.assertEqual(expect, self.email.to)

    def test_subscription_email_body(self):
        contents = [
            'Guilherme Bagnato',
            '12345678901',
            'gui.bagnato@gmail.com',
            '16-9911-4332'
        ]

        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)
