package dev.danbrick92.generalai.tasks.converse.chatgpt;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.web.client.RestTemplate;

@Configuration
public class OpenAIRestTemplate {

    @Autowired
    @Qualifier("openAIAPIKey")
    private OpenAIAPIKey openAIAPIKey;

    @Bean
    @Qualifier("openaiRestTemplate")
    public RestTemplate openaiRestTemplate() {
        RestTemplate restTemplate = new RestTemplate();
        restTemplate.getInterceptors().add((request, body, execution) -> {
            request.getHeaders().add("Authorization", "Bearer " + openAIAPIKey.getApiKey());
            return execution.execute(request, body);
        });
        return restTemplate;
    }
}