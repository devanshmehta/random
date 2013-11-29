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
        assertEquals("value", s);
        s = config.getProperty("secondsection", "propertyname");
        assertEquals("value", s);
    }

    public static void assertEquals(String expected, String actual) {
        if(!expected.equals(actual)) {
            String message = ("expected(" + expected + ") " + 
                              "!= actual(" + actual +")");
            throw new RuntimeException(message);
        }
    }
}