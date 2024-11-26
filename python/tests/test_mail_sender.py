import pytest

from mail_sender import MailSender, SendMailRequest, SendMailResponse
from user import User

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


def test_send_v1():
    recipient = User("billy", "billy@efrei.net")
    http_client = HttpClient()

    mail_sender = MailSender(http_client)
    mail_sender.send_v1(recipient, "blblblbllb")

    assert http_client.user_email == recipient.email


def test_send_v2():
    recipient = User("billy", "billy@efrei.net")
    http_client = HttpClient()

    mail_sender = MailSender(http_client)
    mail_sender.send_v2(recipient, "blblblbl")

    assert isinstance(http_client.request, SendMailRequest)
