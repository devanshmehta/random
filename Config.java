package config; 

import java.io.IOException;
import java.util.Properties;
import java.util.Map;
import java.util.HashMap;

public class Config {
  
    public Config(String fileName) {
        this.fileName = fileName;
        sectionPropeties = new HashMap<String, Properties>();
    }
  
    private Map<String, Properties> sectionProperties;
    private String fileName;
}
