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
