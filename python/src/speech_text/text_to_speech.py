# # Imports
import os
# import pyttsx3
# import logging

# # Classes
# class Speak:

#     def __init__(self):
#         self.engine = pyttsx3.init()

#     def speak(self, message: str):
#         logging.info(f"Speaking: {message}")
#         self.engine.say(message)
#         self.engine.runAndWait()

#     def set_male_voice(self):
#         logging.info(f"Set to male")
#         voices = self.engine.getProperty('voices')
#         self.engine.setProperty('voice', voices[0].id) 

#     def set_female_voice(self):
#         logging.info(f"Set to female")
#         voices = self.engine.getProperty('voices')
#         self.engine.setProperty('voice', voices[1].id) 

# # Functions
# def sample():
#     spk = Speak()
#     spk.set_male_voice()
#     spk.speak("Hello, Carly. Is that you?")
#     spk.set_female_voice()
#     spk.speak("Hello, Carly. Is that you?")


from google.cloud import texttospeech

# import required module
from pydub import AudioSegment
from pydub.playback import play
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = os.environ['GCP_API_KEY']

def synthesize_speech(text, output_filename):

    # Create a Text-to-Speech client
    client = texttospeech.TextToSpeechClient()

    # Set the text input
    input_text = texttospeech.SynthesisInput(text=text)

    # Configure the voice settings
    voice = texttospeech.VoiceSelectionParams(
        language_code="en-US",
        ssml_gender=texttospeech.SsmlVoiceGender.FEMALE
    )

    # Set the audio configuration
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3
    )

    # Perform the text-to-speech request
    response = client.synthesize_speech(
        input=input_text, voice=voice, audio_config=audio_config
    )

    # Save the audio to a file
    with open(output_filename, 'wb') as out:
        out.write(response.audio_content)
        print(f"Audio content written to '{output_filename}'")

    song = AudioSegment.from_mp3(output_filename)
    print('playing sound using  pydub')
    play(song)

# Test the text-to-speech function
synthesize_speech("Hello, world!", "output.mp3")
