package dev.danbrick92.generalai.sensors;

import org.springframework.stereotype.Component;

@Component
public interface Sensor {
    public Object sense();
}
