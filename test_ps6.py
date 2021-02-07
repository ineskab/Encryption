import ps6
from ps6 import CiphertextMessage, Message


def test_apply_shift():
    msg = "Lunia"
    a = Message(msg)
    shift = 1

    expected = "Mvojb"
    actual = a.apply_shift(shift)

    assert actual == expected

def test_apply_shift_zero_shift():
    msg = "Lunia"
    a = Message(msg)
    shift = 0

    expected = msg
    actual = a.apply_shift(shift)

    assert actual == expected

def test_apply_shift_non_alphabetical_characters():
    msg = "Lunia27 ! lunia"
    a = Message(msg)
    shift = 1

    expected = "Mvojb27 ! mvojb"
    actual = a.apply_shift(shift)

    assert actual == expected


class TestCiphertextMessage:
    def test_decrypt_message(self):
        a = CiphertextMessage('jgnnq')
        exp = (24, 'hello')
        act = a.decrypt_message()

        assert act == exp


def test_decrypt_story():
    assert 1 == ps6.decrypt_story()
