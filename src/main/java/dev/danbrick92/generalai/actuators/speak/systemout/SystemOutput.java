package dev.danbrick92.generalai.actuators.speak.systemout;

import dev.danbrick92.generalai.actuators.speak.Speaker;
import org.springframework.stereotype.Component;

@Component
public class SystemOutput extends Speaker {

    @Override
    public void speak(String message) {
        System.out.println(message);
    }
}
