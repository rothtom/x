from credit import validate

def main():
    test_validate()


def test_validate():
    assert validate(378282246310005) == "AMEX"
    assert validate(5555555555554444) == "MASTERCARD"
    assert validate(5105105105105100) == "MASTERCARD"
    assert validate(4111111111111111) == "VISA"
    assert validate(1234567890) == "INVALID"
