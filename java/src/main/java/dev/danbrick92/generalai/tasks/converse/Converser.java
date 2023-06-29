package dev.danbrick92.generalai.tasks.converse;

import dev.danbrick92.generalai.tasks.Task;
import dev.danbrick92.generalai.actuators.Actuator;
import dev.danbrick92.generalai.sensors.Sensor;
import dev.danbrick92.generalai.sensors.listen.Listener;
import dev.danbrick92.generalai.actuators.speak.Speaker;
import java.security.InvalidParameterException;
import java.util.List;


public abstract class Converser implements Task {

    @Override
    public Object task(List<Sensor> sensors, List<Actuator> actuators) {
        // Get listener object
        Sensor sensor = sensors.stream().
                filter(s -> s instanceof Listener).
                findFirst().
                orElseThrow(() -> new InvalidParameterException("Must provide Listener object to Conversator"));
        Listener listener = (Listener) sensor;

        // Get speaker object
        Actuator actuator = actuators.stream().
                filter(a -> a instanceof Speaker).
                findFirst().
                orElseThrow(() -> new InvalidParameterException("Must provide Listener object to Conversator"));
        Speaker speaker = (Speaker) actuator;

        return converse(listener, speaker);
    }

    public abstract Object converse(Listener listener, Speaker speaker);
}
