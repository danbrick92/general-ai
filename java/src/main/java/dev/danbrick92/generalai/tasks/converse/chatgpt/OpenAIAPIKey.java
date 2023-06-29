package dev.danbrick92.generalai.tasks.converse.chatgpt;

import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.stereotype.Component;

import java.util.Map;

@Component
@Qualifier("openAIAPIKey")
public class OpenAIAPIKey {
    private String apiKey = "";

    public OpenAIAPIKey(){
        Map<String, String> env = System.getenv();
        for (Map.Entry<String, String> entry : env.entrySet()) {
            if (entry.getKey().equals("OPENAI_API_KEY")){
                apiKey = entry.getValue().toString();
            }
        }
    }

    public String getApiKey(){
        return apiKey;
    }
}
