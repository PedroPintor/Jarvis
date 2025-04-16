from audio_input import ouvir_microfone
# from agent import responder_ia
from audio_output import falar_texto

def main():
    print("🤖 Iniciando IA-Falante. Pressione Ctrl+C para sair.")
    while True:
        entrada = ouvir_microfone()
        if entrada:
            # resposta = responder_ia(entrada)
            print(f"🤖 IA: {resposta}")
            falar_texto(resposta)

if __name__ == "__main__":
    main()
