import pytest
import substitution_cipher

key = 'BCDEFGHIJKLMNOPQRSTUVWXYZA' # Caesar cipher ;-)

testdata = [
    ('A', 'B'),
    ('B', 'C'),
    ('Z', 'A'),
    ('ABC', 'BCD'),
    ('XYZ', 'YZA'),
    ('AbCd', 'BcDe'),
    ('XyZ', 'YzA'),
]

@pytest.mark.parametrize("message, expected", testdata)
def test_Encrypt(message, expected):
    assert substitution_cipher.Encrypt(message, key) == expected

@pytest.mark.parametrize("expected, message", testdata)
def test_Decrypt(message, expected): 
    assert substitution_cipher.Decrypt(message, key) == expected