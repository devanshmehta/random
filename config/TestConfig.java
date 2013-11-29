package config;

import java.io.IOException;
import java.text.ParseException;

/**
 * Class for testing Config class.
 * 
 * @author devansh.mht@gmail.com
 */
public class TestConfig {

    public static void main(String[] args) 
        throws IOException, ParseException {
        String fileName = "config/testfile.config";
        Config config = new Config(fileName);
        String s = config.getProperty("firstsection", "propertyname");
        System.out.println(s);
        s = config.getProperty("secondsection", "propertyname");
        System.out.println(s);
    }

}