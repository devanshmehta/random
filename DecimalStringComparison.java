import java.util.Comparator;

/**
 * Compares decimals represented as String. It compares
 * only the positive integers. The compare method assumes
 * all the strings are properly formatted as xyz.abc or 
 * xyz where x,y,z,a,b,c are characters in (0-9).
 * 
 * @author devansh.mht@gmail.com (Devansh Mehta)
 */
public class DecimalStringComparison implements Comparator<String> {

    public int compare(String firstNum, String secondNum) {
        int charsBeforeDotInFirstNum = getCharsBeforeDot(firstNum);
        int charsBeforeDotInSecondNum = getCharsBeforeDot(secondNum);
        if(charsBeforeDotInFirstNum != charsBeforeDotInSecondNum) {
            return charsBeforeDotInFirstNum - charsBeforeDotInSecondNum;
        }
        for(int i = 0; i < charsBeforeDotInFirstNum; ++i) {
            int firstNumDigit = firstNum.charAt(i);
            int secondNumDigit = secondNum.charAt(i);
            if(firstNumDigit != secondNumDigit) {
                return firstNumDigit - secondNumDigit;
            }
        }
        //It means everything before the dot is similar.
        int charsAfterDotInFirstNum = 
                getCharsAfterDot(firstNum, charsBeforeDotInFirstNum);
        int charsAfterDotInSecondNum = 
                getCharsAfterDot(secondNum, charsBeforeDotInSecondNum);
        if(charsAfterDotInFirstNum == 0 && 
           charsAfterDotInSecondNum == 0) {
            return 0; 
        }
        if(charsAfterDotInFirstNum == 0) {
            for(int i = 0 ; i < charsAfterDotInSecondNum; ++i) {
                if(secondNum.charAt(charsBeforeDotInSecondNum + i) != '0') {
                    return 1;
                }
            }
            return 0;
        }
        if(charsAfterDotInSecondNum == 0) {
            for(int i = 0 ; i < charsAfterDotInFirstNum; ++i) {
                if(firstNum.charAt(charsBeforeDotInFirstNum + i) != '0') {
                    return 1;
                }
            }
            return 0;
        }
        int count = 0;
        if(charsAfterDotInFirstNum < charsAfterDotInSecondNum) {
            count = charsAfterDotInFirstNum;
        } else {
            count = charsAfterDotInSecondNum;
        }
        for(int i = 0; i < count; ++i) {
            int firstNumDigit = firstNum.charAt(charsBeforeDotInFirstNum + i);
            int secondNumDigit = secondNum.charAt(charsBeforeDotInSecondNum + i);
            if(firstNumDigit != secondNumDigit) {
                return firstNumDigit - secondNumDigit;
            }
        }
        if(count == charsAfterDotInFirstNum) {
            for(int i = 0; i < charsAfterDotInSecondNum - count; ++i) {
                if(secondNum.charAt(charsBeforeDotInSecondNum + count + i) != '0') {
                    return 1;
                }
            }
        } else {
            for(int i = 0; i < charsAfterDotInFirstNum - count; ++i) {
                if(firstNum.charAt(charsBeforeDotInFirstNum + count + i) != '0') {
                    return 1;
                }
            }
        }
        return 0;
    }
    
    /**
     * Gets the number of characters in the number after the decimal 
     * place.
     * 
     * @param num
     * @param numCharsBeforeDot in num
     * @return number of characters after decimal place in num.
     */
    private int getCharsAfterDot(String num, int numCharsBeforeDot) {
        if(numCharsBeforeDot == num.length()) {
            return 0;
        }
        return num.length() - 1 - numCharsBeforeDot;
    }
    
    /**
     * Returns the number of characters before the decimal 
     * point starts.
     * 
     * @param num
     * @return number of characters before decimal point start.
     */
    private int getCharsBeforeDot(String num) {
        int charsBeforeDot = 0;
        for(int i = 0; i < num.length(); ++i) {
            if(num.charAt(i) == '.') {
                break;
            }
            ++charsBeforeDot;
        }
        return charsBeforeDot;
    }
}
