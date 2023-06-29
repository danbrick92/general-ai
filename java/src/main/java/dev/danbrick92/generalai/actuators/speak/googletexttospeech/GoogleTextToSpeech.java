package dev.danbrick92.generalai.actuators.speak.googletexttospeech;

// Imports the Google Cloud client library
import com.google.cloud.texttospeech.v1.AudioConfig;
import com.google.cloud.texttospeech.v1.AudioEncoding;
import com.google.cloud.texttospeech.v1.SsmlVoiceGender;
import com.google.cloud.texttospeech.v1.SynthesisInput;
import com.google.cloud.texttospeech.v1.SynthesizeSpeechResponse;
import com.google.cloud.texttospeech.v1.TextToSpeechClient;
import com.google.cloud.texttospeech.v1.VoiceSelectionParams;
import com.google.common.io.ByteSource;
import com.google.protobuf.ByteString;
import dev.danbrick92.generalai.actuators.speak.Speaker;
import javazoom.jl.decoder.JavaLayerException;
import javazoom.jl.player.Player;
import org.springframework.stereotype.Component;
import java.io.*;

@Component
public class GoogleTextToSpeech extends Speaker {

    @Override
    public void speak(String message) {
        try (TextToSpeechClient textToSpeechClient = TextToSpeechClient.create()) {
            // Set the text input to be synthesized
            SynthesisInput input = SynthesisInput.newBuilder().setText(message).build();

            // Build the voice request, select the language code ("en-US") and the ssml voice gender
            // ("neutral")
            VoiceSelectionParams voice =
                    VoiceSelectionParams.newBuilder()
                            .setLanguageCode("en-US")
                            .setSsmlGender(SsmlVoiceGender.FEMALE)
                            .build();

            // Select the type of audio file you want returned
            AudioConfig audioConfig =
                    AudioConfig.newBuilder().setAudioEncoding(AudioEncoding.MP3).build();

            // Perform the text-to-speech request on the text input with the selected voice parameters and
            // audio file type
            SynthesizeSpeechResponse response =
                    textToSpeechClient.synthesizeSpeech(input, voice, audioConfig);

            // Get the audio contents from the response
            ByteString audioContents = response.getAudioContent();

            byte[] audioArray = audioContents.toByteArray();
            InputStream targetStream = ByteSource.wrap(audioArray).openStream();
            playAudio(targetStream);
        } catch (IOException | JavaLayerException e) {
            throw new RuntimeException(e);
        }
    }

    public void playAudio(InputStream inputStream) throws JavaLayerException {
        Player player = new Player(inputStream);
        player.play();
    }
}
