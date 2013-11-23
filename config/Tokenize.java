package config;

import java.text.ParseException;

public class Tokenize {
    
    /**
     * Tokenizes a line into token
     * 
     * @param line
     * @return Token if found otherwise null
     * @throws NullPointerException if the line is null or 
     *         has zero length.
     * @throws ParseException if there is error in parsing 
     *         the line.
     */
    public static Token getTokenFor(String line) 
        throws ParseException {
        if(line == null || line.length() == 0) {
            throw new NullPointerException();
        }
        line = line.trim();
        line += '\n';
        int index = 0;
        char c = line.charAt(index);
        if(c == '#') {
            return parseComment(line, index++);
        }else if(c == '[') {
            return parseSection(line, index++);
        }else {
            return parseProperty(line, index);
        }
    }
    
    private static Token parseComment(String line, int index) {
        return new Token(TOKEN_TYPE.COMMENT, line.substring(index));
    }
    
    private static Token parseSection(String line, int index) 
        throws ParseException {
        char c = line.charAt(index);
        StringBuilder sb = new StringBuilder();
        while(c != ']' || c != '\n') {
            if(Character.isLetter(c)) {
                sb.append(c);
            }else {
                throw new ParseException(line.trim(), index);
            }
            c = line.charAt(++index);
        }
        if(c == ']') {
            if(line.charAt(++index) != '\n') {
                throw new ParseException(line.trim(), index);
            }
        }
        if(c == '\n') {
            throw new ParseException(line.trim(), index);
        }
        return new Token(TOKEN_TYPE.SECTION, sb.toString());
    }
    
    private static Token parseProperty(String line, int index) 
        throws ParseException {
        char c = line.charAt(index);
        StringBuilder property = new StringBuilder();
        StringBuilder value = new StringBuilder();
        boolean foundEquals = false;
        while(index < line.length() - 1) {
            if(c == '=') {
                foundEquals = true;
            }
            if(!foundEquals) {
                property.append(c);
            }else {
                value.append(c);
            }
            c = line.charAt(++index);
        }
        if(!foundEquals) {
            throw new ParseException("cannot find equals", 0);
        }
        if(property.length() == 0) {
            throw new ParseException("length of property is 0", 0);
        }
        property.append('=');
        property.append(value);
        return new Token(TOKEN_TYPE.PROPERTY, property.toString());
    }
}

enum TOKEN_TYPE {
    COMMENT, PROPERTY, SECTION
}

class Token {
    
    public Token(TOKEN_TYPE tokenType, String value) {
        this.tokenType = tokenType;
        this.value = value;
    }
    
    public TOKEN_TYPE getTokenType() {
        return tokenType;
    }
    
    public String getValue() {
        return value;
    }
    
    private TOKEN_TYPE tokenType;
    private String value;
  
}
