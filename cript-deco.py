from base64 import b64decode
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

SENHA = "??"

def descriptografar(valor_criptografado, senha=SENHA):
    chave = senha.encode("utf-8")

    dados = b64decode(valor_criptografado)

    iv = dados[:16]
    texto_criptografado = dados[16:]

    cipher = AES.new(chave, AES.MODE_CBC, iv)

    texto = unpad(cipher.decrypt(texto_criptografado), AES.block_size)

    return texto.decode("utf-8")

secret_criptografado = "??"

print(descriptografar(secret_criptografado))