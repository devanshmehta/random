package config;

public class Tokenize {

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
