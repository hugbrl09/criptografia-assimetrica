from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

def gerar_chaves():
    # Gerando chave privada
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048
    )

    # Gerando chave pública
    public_key = private_key.public_key()

    # Salvando chave privada em arquivo
    with open("private_key.pem", "wb") as f:
        f.write(
            private_key.private_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PrivateFormat.PKCS8,
                encryption_algorithm=serialization.NoEncryption()
            )
        )

    # Salvando chave pública em arquivo
    with open("public_key.pem", "wb") as f:
        f.write(
            public_key.public_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PublicFormat.SubjectPublicKeyInfo
            )
        )

    print("Chaves geradas com sucesso!")

def carregar_chaves():
    with open("private_key.pem", "rb") as f:
        private_key = serialization.load_pem_private_key(
            f.read(),
            password=None
        )

    with open("public_key.pem", "rb") as f:
        public_key = serialization.load_pem_public_key(
            f.read()
        )

    return private_key, public_key