package dev.danbrick92.generalai.sensors.listen.userprompt;
import dev.danbrick92.generalai.sensors.listen.Listener;
import org.springframework.stereotype.Component;

import java.util.Scanner;

@Component
public class UserPrompt extends Listener {

    public String listen(){
        return promptUser();
    }

    public String promptUser(){
        System.out.println("Please enter your question here: ");
        Scanner scanner = new Scanner(System.in);
        String question = scanner.nextLine();
        return question;
    }

}
