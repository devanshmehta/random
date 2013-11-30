package config;

/**
 * Tokens for the config file.
 * 
 * @author devansh.mht@gmail.com
 */
class Token {
    
    public Token(TokenType tokenType, String value) {
        this.tokenType = tokenType;
        this.value = value;
    }
    
    public TokenType getTokenType() {
        return tokenType;
    }
    
    public String getValue() {
        return value;
    }

    @Override
    public String toString() {
        return ("Token Type: " + tokenType + 
                " Value: " + value);
    }

    @Override
    public int hashCode() {
        return tokenType.hashCode() + value.hashCode();
    }
    
    @Override
    public boolean equals(Object obj) {
        if(this == obj) {
            return true;
        }
        if(!(obj instanceof Token)) {
            return false;
        }
        Token token = (Token) obj;
        return (tokenType == token.tokenType && 
                value.equals(token.value));        
    }
    
    private TokenType tokenType;
    private String value;
  
}
