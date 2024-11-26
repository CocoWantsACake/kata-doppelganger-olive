import pytest
from unittest.mock import MagicMock

from mail_sender import MailSender, SendMailRequest, SendMailResponse
from user import User

@pytest.fixture(scope="session")
def recipient(): return User("billy", "billy@efrei.net")

@pytest.fixture(scope="session")
def http_client(): return HttpClient()

@pytest.fixture(scope="session")
def mail_sender(http_client): return MailSender(http_client)

class HttpClient:

    user_email = None
    request = None

    def post(self, base_url, request):
        self.request = request

        if not isinstance(request, SendMailRequest):
            raise Exception("'request' should be from the 'SendMailRequest' class, but is a '{}' isntead.".format(type(request)))

        self.user_email = request.recipient
        return SendMailResponse(503, "aa")

#def create_base_scenario():


def test_send_v1_no_mock(recipient, http_client, mail_sender):
    mail_sender.send_v1(recipient, "blblblbllb")
    assert http_client.user_email == recipient.email


def test_send_v2_no_mock(recipient, http_client, mail_sender):
    mail_sender.send_v2(recipient, "blblblbl")
    assert isinstance(http_client.request, SendMailRequest)

"""
def test_send_v1_with_mock(recipient, http_client, mail_sender):
    mail_sender.send_v1(recipient, "blblblbllb")
    assert http_client.user_email == recipient.email


def test_send_v2_with_mock(recipient, http_client, mail_sender):
    mail_sender.send_v2(recipient, "blblblbl")
    assert isinstance(http_client.request, SendMailRequest)
"""