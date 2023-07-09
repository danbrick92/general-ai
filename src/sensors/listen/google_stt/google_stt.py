import numpy as np
import time
import os
import logging
from sensors.listen.listener import Listener
from google.cloud import speech
import sounddevice as sd
import wavio as wv
import torch
torch.set_num_threads(1)


class GoogleSpeechToText(Listener):

    def __init__(self):
        logging.debug("Configuring Speech to Text class...")
        super().__init__()
        self.config = speech.RecognitionConfig(
            language_code="en",
            audio_channel_count=1
        )
        self.file_name = "recording0.wav"
        self.frequency = 16000
        self.time_limit = 30
        logging.debug("Loading VAD model...")
        self.model, self.utils = torch.hub.load(repo_or_dir='snakers4/silero-vad', model='silero_vad',force_reload=False,onnx=False)
        self.interval = 2

    def listen(self, led=None) -> str:
        # Record the user
        if led: led.set_state('recording')
        recording = self.record()
        if led: led.set_state('busy')

        # Save temp recording
        logging.debug(f"Saving temp recording to {self.file_name}...")
        if recording is not None and recording.shape[0] > 0:
            wv.write(self.file_name, recording, self.frequency, sampwidth=2)

        # Speech recognition
        try:
            logging.debug(f"Getting Google Speech to Text response...")
            with open(self.file_name, 'rb') as file:
                audio = speech.RecognitionAudio(
                    content=file.read()
                )
                reply = self.speech_to_text(audio)
        except FileNotFoundError:
            reply = ""

        # Remove temp recording
        logging.debug(f"Removing temp recording...")
        try:
            os.remove(self.file_name)
        except FileNotFoundError:
            pass
        except Exception as e:
            logging.error(f"Unable to delete temp recording file {self.file_name} with error {e}.")

        return reply

    def record(self):
        logging.info(f"Recording voice for {self.time_limit} seconds in non-blocking mode...")
        print(f"Getting your voice now for {self.time_limit} seconds...")
        full_recording = sd.rec(int(self.time_limit * self.frequency),
                           samplerate=self.frequency, channels=1, blocking=False)
        for i in range(0, self.time_limit, self.interval):
            start = i * self.frequency
            time.sleep(self.interval)
            logging.debug(f"Check from start {start} of {full_recording.shape[0]}")
            if not self.__check_contains_speech(full_recording[start:start+(self.interval*self.frequency), 0]):
                logging.info("Not hearing human voices anymore. Stopping recording.")
                sd.stop()
                return full_recording[0:start+(self.interval*self.frequency)]

        return full_recording

    def __check_contains_speech(self, recording: np.array) -> bool:
        # Get timestamps of speech
        get_speech_timestamps = self.utils[0]
        speech_timestamps = get_speech_timestamps(recording, self.model, sampling_rate=self.frequency)
        return len(speech_timestamps) > 0

    def speech_to_text(self, audio: speech.RecognitionAudio) -> str:
        logging.debug("Creating Google Speech to Text client...")
        client = speech.SpeechClient()

        # Synchronous speech recognition request
        logging.debug("Performing speech recognition...")
        response = client.recognize(config=self.config, audio=audio)
        logging.debug(f"Google Speech to Text response = {response}")

        try:
            print(f"I heard: {response.results[0].alternatives[0].transcript}")
            return response.results[0].alternatives[0].transcript
        except IndexError:
            print("Didn't catch that.")
            logging.debug(f"Google Speech to Text did not find any voice in audio")
            return ""
