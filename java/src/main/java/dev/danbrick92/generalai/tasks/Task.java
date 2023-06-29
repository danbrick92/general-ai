package dev.danbrick92.generalai.tasks;

import dev.danbrick92.generalai.actuators.Actuator;
import dev.danbrick92.generalai.sensors.Sensor;
import org.springframework.stereotype.Component;

import java.util.List;

@Component
public interface Task {

    public Object task(List<Sensor> sensors, List<Actuator> actuators);
}
