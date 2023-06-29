package dev.danbrick92.generalai;

import dev.danbrick92.generalai.actuators.speak.googletexttospeech.GoogleTextToSpeech;
import dev.danbrick92.generalai.actuators.speak.systemout.SystemOutput;
import dev.danbrick92.generalai.sensors.listen.userprompt.UserPrompt;
import dev.danbrick92.generalai.tasks.converse.chatgpt.ChatGPT;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.ConfigurableApplicationContext;

@SpringBootApplication
public class Application {

	public static void main(String[] args) {
		ConfigurableApplicationContext context = SpringApplication.run(Application.class, args);

		ChatGPT chat = (ChatGPT) context.getBean("chatGPT");
		UserPrompt userPrompt = (UserPrompt) context.getBean("userPrompt");
		// SystemOutput systemOutput = (SystemOutput) context.getBean("systemOutput");
		GoogleTextToSpeech googleTextToSpeech = (GoogleTextToSpeech) context.getBean("googleTextToSpeech");
		chat.converse(userPrompt, googleTextToSpeech);
	}

}
