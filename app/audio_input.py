import speech_recognition as sr

def ouvir_microfone():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Fale algo:")
        audio = recognizer.listen(source)

    try:
        texto = recognizer.recognize_google(audio, language="pt-BR")
        print(f"🗣️ Você disse: {texto}")
        return texto
    except sr.UnknownValueError:
        print("😕 Não entendi o que você disse.")
        return None
    except sr.RequestError as e:
        print(f"Erro na requisição: {e}")
        return None
