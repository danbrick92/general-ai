package dev.danbrick92.generalai.tasks.converse.chatgpt;

public class ChatGPTMessage {

    private String role;
    private String content;

    ChatGPTMessage(String role, String content) {
        this.role = role;
        this.content = content;
    }

    ChatGPTMessage() {
    }

    public String getRole() {
        return role;
    }

    public void setRole(String role) {
        this.role = role;
    }

    public String getContent() {
        return content;
    }

    public void setContent(String content) {
        this.content = content;
    }
}