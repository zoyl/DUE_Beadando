from Crypto.PublicKey import RSA


def private_key(plaintext, key):

    encrypted_key = key.export_key(passphrase=plaintext, pkcs=8, protection="scryptAndAES128-CBC")
    return encrypted_key


def public_key(plaintext, key):
    public_key = key.publickey().export_key()
    return public_key


def generate_key():
    return RSA.generate(2048)

