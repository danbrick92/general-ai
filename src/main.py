from actuators.speak.google_tts.google_tts import GoogleTextToSpeech
from sensors.listen.google_stt.google_stt import GoogleSpeechToText
from tasks.chat.chatgpt.chatgpt import ChatGPT
import logging
import os

# Import Button and RGB LED if on Pi
try:
    is_pi = (os.uname().nodename == 'raspberrypi')
except:
    is_pi = False
if is_pi:
    from pi_components.click_button import ClickButton
    from pi_components.rgb_led import RGBLed
    
logging.basicConfig(level=logging.INFO)

 
def main():
    extras = {}
    if is_pi:
        extras = {'button': ClickButton(), 'led': RGBLed()}
        
    try:
        speaker = GoogleTextToSpeech()
        listener = GoogleSpeechToText()
        chat = ChatGPT([speaker], [listener], extras)
        chat.chat()
    except Exception as e:
        logging.error(str(e))
    finally:
        if extras['led'] is not None:
            extras['led'].reset()


if '__name__' == main():
    main()
