package dev.danbrick92.generalai.tasks.converse.chatgpt;

import dev.danbrick92.generalai.actuators.speak.Speaker;
import dev.danbrick92.generalai.actuators.speak.systemout.SystemOutput;
import dev.danbrick92.generalai.sensors.listen.Listener;
import dev.danbrick92.generalai.tasks.converse.Converser;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.stereotype.Component;
import org.springframework.web.client.RestTemplate;

@Component
public final class ChatGPT extends Converser {

    @Qualifier("openaiRestTemplate")
    @Autowired
    private RestTemplate restTemplate;

    private final String model = "gpt-3.5-turbo";
    private final String url = "https://api.openai.com/v1/chat/completions";
    private ChatGPTRequest request;

    @Override
    public Object converse(Listener listener, Speaker speaker) {
        while (true){
            // Prompt user for their input
            String query = listener.listen();

            // Check if special
            if (query.toLowerCase().equals("x")){
                System.out.println("Exiting...");
                return null;
            }

            // Get ChatGPT Response
            String reply = getResponse(query);

            // Output response
            speaker.speak(reply);
        }
    }

    public String getResponse(String query){
        // Add query to request
        if (request == null){
            request = new ChatGPTRequest(model, query);
        }
        else {
            request.addMessage("user", query);
        }

        // Call API and parse response
        ChatGPTResponse response = restTemplate.postForObject(url, request, ChatGPTResponse.class);

        if (response == null || response.getChoices() == null || response.getChoices().isEmpty()) {
            return "No response";
        }

        // Return the first response
        String reply = response.getChoices().get(0).getMessage().getContent();

        // Add to request
        request.addMessage("assistant", reply);
        return reply;
    }
}
