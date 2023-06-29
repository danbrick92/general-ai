package dev.danbrick92.generalai.sensors.listen.googlespeechtotext;

import dev.danbrick92.generalai.sensors.listen.Listener;
import com.google.cloud.speech.v1.RecognitionAudio;
import com.google.cloud.speech.v1.RecognitionConfig;
import com.google.cloud.speech.v1.RecognitionConfig.AudioEncoding;
import com.google.cloud.speech.v1.RecognizeResponse;
import com.google.cloud.speech.v1.SpeechClient;
import com.google.cloud.speech.v1.SpeechRecognitionAlternative;
import com.google.cloud.speech.v1.SpeechRecognitionResult;
import javazoom.jl.decoder.JavaLayerException;

import java.io.IOException;
import java.util.List;

public class GoogleSpeechToText extends Listener {

    SoundRecorder soundRecorder = new SoundRecorder();
    private final long record_time_ms = 5000;

    @Override
    public String listen() throws IOException {

        // creates a new thread that waits for a specified
        // of time before stopping
        Thread stopper = new Thread(new Runnable() {
            public void run() {
                try {
                    Thread.sleep(record_time_ms);
                } catch (InterruptedException ex) {
                    ex.printStackTrace();
                }
                soundRecorder.finish();
            }
        });

        stopper.start();

        // start recording
        soundRecorder.start();
        return "";



//        try (SpeechClient speechClient = SpeechClient.create()) {
//
//            // The path to the audio file to transcribe
//            String gcsUri = "gs://cloud-samples-data/speech/brooklyn_bridge.raw";
//
//            // Builds the sync recognize request
//            RecognitionConfig config =
//                    RecognitionConfig.newBuilder()
//                            .setEncoding(AudioEncoding.LINEAR16)
//                            .setSampleRateHertz(16000)
//                            .setLanguageCode("en-US")
//                            .build();
//            RecognitionAudio audio = RecognitionAudio.newBuilder()..setUri(gcsUri).build();
//
//            // Performs speech recognition on the audio file
//            RecognizeResponse response = speechClient.recognize(config, audio);
//            List<SpeechRecognitionResult> results = response.getResultsList();
//
//            for (SpeechRecognitionResult result : results) {
//                // There can be several alternative transcripts for a given chunk of speech. Just use the
//                // first (most likely) one here.
//                SpeechRecognitionAlternative alternative = result.getAlternativesList().get(0);
//                System.out.printf("Transcription: %s%n", alternative.getTranscript());
//            }
//            return "";
//        }
//        catch (IOException e) {
//            throw new RuntimeException(e);
//        }
    }
}
