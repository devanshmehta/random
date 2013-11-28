package config;

import java.text.ParseException;

/**
 * Class for testing Tokenize class.
 * 
 * @author devansh.mht@gmail.com
 */
public class TestTokenize {

    public static void main(String[] args) throws ParseException {
        Token actual = Tokenize.getTokenFor("[abc]");
        assertEqual(new Token(TOKEN_TYPE.SECTION, "abc"), actual);
        actual = Tokenize.getTokenFor("#abc");
        assertEqual(new Token(TOKEN_TYPE.COMMENT, "abc"), actual);        
        actual = Tokenize.getTokenFor("abc=xyz");
        assertEqual(new Token(TOKEN_TYPE.PROPERTY, "abc=xyz"), actual);
    }

    public static void assertEqual(Token expected, Token actual) {
        if(!expected.equals(actual)) {
            String message = ("expected(" + expected + ") " + 
                              "actual(" + actual + ")");
            throw new RuntimeException(message);
        }
    }

}