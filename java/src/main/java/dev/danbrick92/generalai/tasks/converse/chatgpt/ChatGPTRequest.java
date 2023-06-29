package dev.danbrick92.generalai.tasks.converse.chatgpt;

import java.util.List;
import java.util.ArrayList;

public class ChatGPTRequest {

    private String model;
    private List<ChatGPTMessage> messages;

    public ChatGPTRequest(String model, String message) {
        this.model = model;
        this.messages = new ArrayList<>();
        this.messages.add(new ChatGPTMessage("user", message));
    }

    public String getModel() {
        return model;
    }

    public void setModel(String model) {
        this.model = model;
    }

    public List<ChatGPTMessage> getMessages() {
        return messages;
    }

    public void setMessages(List<ChatGPTMessage> messages) {
        this.messages = messages;
    }

    public void addMessage(String role, String message){
        ChatGPTMessage chatGPTMessage = new ChatGPTMessage(role, message);
        messages.add(chatGPTMessage);
    }

    public void resetMessages(){
        this.messages = new ArrayList<>();
    }
}
