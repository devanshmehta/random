package config; 

import java.io.IOException;
import java.util.Properties;
import java.util.Map;
import java.util.HashMap;

/**
 * Parses the configuration file. The configuration file
 * either contains section name or properties. The properties
 * should come after the section name. Line starting with 
 * # is considered to be comment.
 * 
 * @ author devansh.mht@gmail.com
 */
public class Config {
  
    public Config(String fileName) {
        this.fileName = fileName;
        sectionProperties = new HashMap<String, Properties>();
    }
  
    private Map<String, Properties> sectionProperties;
    private String fileName;
}
