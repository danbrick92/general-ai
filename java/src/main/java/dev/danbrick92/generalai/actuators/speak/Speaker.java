package dev.danbrick92.generalai.actuators.speak;

import dev.danbrick92.generalai.actuators.Actuator;

public abstract class Speaker implements Actuator {

    public void actuate(Object data) {
        String message = (String) data;
        speak(message);
    }

    public abstract void speak(String message);
}
