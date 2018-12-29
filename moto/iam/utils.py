from __future__ import unicode_literals
import random
import string
import six


def random_alphanumeric(length):
    return ''.join(six.text_type(
        random.choice(
            string.ascii_letters + string.digits
        )) for _ in range(length)
    )


def random_resource_id(size=20):
    chars = list(range(10)) + list(string.ascii_lowercase)

    return ''.join(six.text_type(random.choice(chars)) for x in range(size))


def random_access_key():
    return ''.join(six.text_type(
        random.choice(
            string.ascii_uppercase + string.digits
        )) for _ in range(16)
    )


def random_policy_id():
    return 'A' + ''.join(
        random.choice(string.ascii_uppercase + string.digits)
        for _ in range(20)
    )
