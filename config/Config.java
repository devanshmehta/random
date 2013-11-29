package config; 

import java.io.File;
import java.io.IOException;
import java.text.ParseException;
import java.util.Scanner;
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
  
    public Config(String fileName) throws IOException, ParseException {
        this.fileName = fileName;
        sectionProperties = new HashMap<String, Properties>();
        parseFile(new File(fileName));
    }

    public String getProperty(String sectionName, String propName) {
        return sectionProperties.get(sectionName).
            getProperty(propName);
    }

    private void parseFile(File file) throws IOException, ParseException {
        String sectionName = null;
        Properties property = null;
        try(Scanner scanner = new Scanner(file)) {
            while(scanner.hasNext()) {
                String line = scanner.nextLine();
                if(line.trim().length() == 0) {
                    continue;
                }
                Token token = Tokenize.getTokenFor(line);
                if(token.getTokenType() == TOKEN_TYPE.SECTION) {
                    sectionName = token.getValue();
                    property = new Properties();
                    sectionProperties.put(sectionName, property);
                } else if(token.getTokenType() == TOKEN_TYPE.PROPERTY) {
                    if(property == null) {
                        String message = ("No section found for " +
                                          token.getValue());
                        throw new RuntimeException(message);
                    }
                    int equalsIndex = line.indexOf('=');
                    String propertyName = line.substring(0, equalsIndex);
                    String value = line.substring(equalsIndex + 1);
                    property.setProperty(propertyName, value);
                } else if(token.getTokenType() == TOKEN_TYPE.COMMENT) {
                    //ignore
                } else {
                    String message = ("No token found for " + 
                                      line);
                    throw new RuntimeException(message);
                }
            }
        }
    }
  
    private Map<String, Properties> sectionProperties;
    private String fileName;
}
