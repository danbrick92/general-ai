package dev.danbrick92.generalai.actuators;

import dev.danbrick92.generalai.tasks.Task;
import org.springframework.stereotype.Component;

import java.util.List;

@Component
public interface Actuator {

    public void actuate(Object data);

}
