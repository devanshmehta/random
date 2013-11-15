package config;

public class Tokenize {
    
    /**
     * Tokenizes a line into token
     * 
     * @param line
     * @return Token if found otherwise null
     * @throws NullPointerException if the line is null or 
     *         has zero length.
     */
    public static Token getTokenFor(String line) {
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
            parseSection(line, index++);
        }else {
            parseProperty(line, index);
        }
    }
    
    private Token parseComment(String line, int index) {
        return new Token(TOKEN_TYPE.COMMENT, line.substring(index));
    }
    
    private Token parseSection(String line, int index) {
        char c = line.charAt(index);
        StringBuilder sb = new StringBuilder();
        while(c != ']' || c != '\n') {
            if(Character.isCharacter(c)) {
                sb.append(c);
            }else {
                //throw an exception
            }
            c = line.charAt(++index);
        }
        if(c == ']') {
            if(line.charAt(++index != '\n') {
                //throw an exception
            }
        }
        if(c == '\n') {
            //throw an exception
        }
        return new Token(TOKEN_TYPE.SECTION, sb.toString());
    }
    
    private Token parseProperty(String line, int index) {
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
            //throw an exception
        }
        if(property.length() == 0) {
            //throw an exception
        }
        return new Token()
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
    
    private String TOKEN_TYPE tokenType;
    private String value;
  
}
