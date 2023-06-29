package dev.danbrick92.generalai.tasks.converse.chatgpt;

import java.util.List;

public class ChatGPTResponse {

    public static class Choice {

        private int index;
        private ChatGPTMessage message;

        public ChatGPTMessage getMessage(){
            return message;
        }
    }

    private List<Choice> choices;

    public List<Choice> getChoices(){
        return choices;
    }
}
