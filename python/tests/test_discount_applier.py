import pytest

from discount_applier import DiscountApplier
from user import User
from unittest.mock import MagicMock, Mock


class Notifier:
    counter = 0
    user_list = []
    def notify(self, user, msg):
        self.counter += 1
        self.user_list.append(user)

def test_apply_v1_no_mock():
    my_user_list = [User("a", "a"), User("b", "b"), User("c", "c")]
    notifier = Notifier()

    da = DiscountApplier(notifier)
    da.apply_v1(10, my_user_list)

    assert notifier.counter == len(my_user_list)


def test_apply_v2_no_mock():
    my_user_list = [User("a", "a"), User("b", "b"), User("c", "c")]
    notifier = Notifier()

    da = DiscountApplier(notifier)
    da.apply_v2(10, my_user_list)

    for i in range(len(my_user_list)):
        assert my_user_list[i].name == notifier.user_list[i].name
        assert my_user_list[i].email == notifier.user_list[i].email



def test_apply_v1_with_mock():
    my_user_list = [User("a", "a"), User("b", "b"), User("c", "c")]
    notifier = MagicMock()

    da = DiscountApplier(notifier)
    da.apply_v1(10, my_user_list)

    assert notifier.notify.call_count == len(my_user_list)

"""
def test_apply_v2_with_mock():
    my_user_list = [User("a", "a"), User("b", "b"), User("c", "c")]
    notifier =MagicMock
    notifier.name = ["a","b","c"]
    da = DiscountApplier(notifier)
    da.apply_v2(10, my_user_list)

    for i in range(len(my_user_list)):
        assert my_user_list[i].name == notifier.user_list[i].name
        assert my_user_list[i].email == notifier.user_list[i].email
"""
