package dev.danbrick92.generalai.sensors.listen;

import dev.danbrick92.generalai.sensors.Sensor;

import java.util.ArrayList;
import java.util.List;

public abstract class Listener implements Sensor {

    public Object sense(){
        return listen();
    }

    public abstract String listen();

}
