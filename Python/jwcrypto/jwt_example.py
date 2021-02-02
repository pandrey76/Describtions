from jwcrypto import jwt, jwk


key = jwk.JWK(generate='oct', size=256)
print(key.export())

Token = jwt.JWT(header={"alg": "HS256"}, claims={"info": "I'm a signed token"})
Token.make_signed_token(key)
print(Token.serialize())
print(Token.serialize(False))
