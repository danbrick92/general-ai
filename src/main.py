from actuators.speak.google_tts.google_tts import GoogleTextToSpeech
from sensors.listen.google_stt.google_stt import GoogleSpeechToText
from tasks.chat.chatgpt.chatgpt import ChatGPT
import logging
logging.basicConfig(level=logging.WARNING)


def main():
    speaker = GoogleTextToSpeech()
    listener = GoogleSpeechToText()
    chat = ChatGPT([speaker], [listener])
    chat.chat()


if '__name__' == main():
    main()
