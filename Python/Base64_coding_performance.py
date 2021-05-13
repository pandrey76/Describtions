# In [1]: import base64
#
# In [2]: password = "1234567890"
#
# In [3]: enc = base64.b64encode(password.encode(encoding="utf-8"))
#
# In [4]: print(enc)
# b'MTIzNDU2Nzg5MA=='
#
# In [5]: data = base64.b64decode(enc)
#
# In [6]: print(data)
# b'1234567890'
#
# In [7]: dec = data.decode(encoding="utf-8")
#
# In [8]: print(dec)
# 1234567890

import base64

password = "a1234567890"

# ascii
# /////////////////////////////////////////////////////////////
password_byte_ascii = password.encode(encoding='ascii')
print(password_byte_ascii)
for b in password_byte_ascii:
    print(b)
ascii_enc = base64.b64encode(password_byte_ascii)
print(ascii_enc)

data_from_ascii = base64.b64decode(ascii_enc)
print(data_from_ascii)

ascii_dec = data_from_ascii.decode(encoding="ascii")
print(ascii_dec)

password_byte_utf8 = password.encode(encoding='utf-8')
print(password_byte_utf8)
for b in password_byte_utf8:
    print(b)


# Decoding to base64
# /////////////////////////////////////////////////////////
# print(base64.b64decode(password_byte_utf8))
# print(base64.b64decode(password_byte_ascii))
# /////////////////////////////////////////////////////////

enc = base64.b64encode(password.encode(encoding="utf-8"))
print(enc)

data = base64.b64decode(enc)
print(data)

dec = data.decode(encoding="utf-8")
print(dec)
