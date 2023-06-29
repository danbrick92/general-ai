from actuators.speak.speaker import Speaker
from pydub import AudioSegment
from pydub.playback import play
from google.cloud import texttospeech
import logging
import os


class GoogleTextToSpeech(Speaker):

    output_filename = "test.mp3"

    def speak(self, message: str):
        # Create a Text-to-Speech client
        logging.debug("Creating text to speech client...")
        client = texttospeech.TextToSpeechClient()

        logging.debug("Setting up Google Text to Speech configuration...")
        # Set the text input
        input_text = texttospeech.SynthesisInput(text=message)

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
        logging.debug("Getting Google Text to Speech response...")
        response = client.synthesize_speech(
            input=input_text, voice=voice, audio_config=audio_config
        )

        # Save the audio to a file
        logging.debug(f"Writing temp response file to {self.output_filename}...")
        with open(self.output_filename, 'wb') as out:
            out.write(response.audio_content)
            logging.debug(f"Audio content written to '{self.output_filename}'")

        # Speak
        logging.info(f"Saying: {message}")
        spoken_word = AudioSegment.from_mp3(self.output_filename)
        play(spoken_word)

        # Remove temp file
        try:
            logging.debug(f"Trying to remove temp file: {self.output_filename}...")
            os.remove(self.output_filename)
        except FileNotFoundError:
            pass
        except Exception as e:
            logging.error(f"Could not remove temp file {self.output_filename} with error: {e}")

