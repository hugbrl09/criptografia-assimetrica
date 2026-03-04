from rsa import gerar_chaves, carregar_chaves
gerar_chaves()

from confidencialidade import criptografar, descriptografar
from autenticidade import assinar, verificar


menu ="""=== SISTEMA RSA ===\n
1 - Confidencialidade (criptografar)
2 - Autenticidade (assinar)
3 - Ambos (assinar + criptografar)
4 - Sair"""

# if not os.path.exists("private_key.pem") or not os.path.exists("public_key.pem"):
#     print("🔑 Gerando chaves...")
#     gerar_chaves()
private_key, public_key = carregar_chaves()

while True:
    print(menu)
    opcao = input("\nEscolha uma opção: ")
    mensagem = input("\nDigite a mensagem: ").encode("utf-8")

    if opcao == "1":
        ciphertext = criptografar(public_key, mensagem)

        with open("mensagem_criptografada.bin", "wb") as f:
            f.write(ciphertext)
        print("\nMensagem criptografada:", ciphertext)

        mensagem_original = descriptografar(private_key, ciphertext)

        print("\nMensagem descriptografada:")
        print(mensagem_original.decode("utf-8"))

    elif opcao == "2":
        assinatura = assinar(private_key, mensagem)

        with open("assinatura.bin", "wb") as f:
            f.write(assinatura)
        print("\nAssinatura:", assinatura)

        verificar(public_key, mensagem, assinatura)

    elif opcao == "3":
        assinatura = assinar(private_key, mensagem)
        ciphertext = criptografar(public_key, mensagem)

        with open("mensagem_criptografada.bin", "wb") as f:
            f.write(ciphertext)
        print("\nMensagem criptografada:", ciphertext)

        with open("assinatura.bin", "wb") as f:
            f.write(assinatura)
        print("\nAssinatura:", assinatura)

        print("\n🔓 Descriptografando...")
        mensagem_original = descriptografar(private_key, ciphertext)

        print("Mensagem descriptografada:")
        print(mensagem_original.decode("utf-8"))

        print("\n🔎 Verificando assinatura...")
        verificar(public_key, mensagem_original, assinatura)

    elif opcao == "4":
        print("Saindo...")
        break

    else:
        print("Opção inválida.")