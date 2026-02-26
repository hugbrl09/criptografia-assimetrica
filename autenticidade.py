from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from rsa import carregar_chaves

public_key, private_key = carregar_chaves()

def assinar(private_key, mensagem):
    return private_key.sign(
        mensagem,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )


def verificar(public_key, mensagem, assinatura):
    try:
        public_key.verify(
            assinatura,
            mensagem,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        print("✅ Assinatura válida!")
    except:
        print("❌ Assinatura inválida!")