from actuators.speak.pyttsx3.pyttsx3 import PyTTSX3
from actuators.speak.system_out.system_out import SystemOut
from actuators.speak.google_tts.google_tts import GoogleTextToSpeech
from sensors.listen.system_in.system_in import SystemIn
from sensors.listen.google_stt.google_stt import GoogleSpeechToText
from tasks.chat.chatgpt.chatgpt import ChatGPT
import logging
logging.basicConfig(level=logging.WARNING)


def main():
    speaker = GoogleTextToSpeech()
    listener = GoogleSpeechToText()
    # listener = SystemIn()
    chat = ChatGPT([speaker], [listener])
    chat.chat()


if '__name__' == main():
    main()
