import pytest
import substitution_cipher

key = 'JIECHSDUGFRVAWNQTYBZOLKMPX'

testdata = [
    ('A', 'J'),
    ('B', 'I'),
    ('Z', 'X'),
    ('ABC', 'JIE'),
    ('XYZ', 'MPX'),
    ('AbCd', 'JiEc'),
    ('XyZ', 'MpX'),
]

@pytest.mark.parametrize("message, expected", testdata)
def test_Encrypt(message, expected):
    assert substitution_cipher.Encrypt(message, key) == expected

@pytest.mark.parametrize("expected, message", testdata)
def test_Decrypt(message, expected): 
    assert substitution_cipher.Decrypt(message, key) == expected