import java.util.Comparator;

/**
 * Compares decimals represented as String. It compares
 * only the positive integers.
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
            int firstNumDigit = firstNum.charAt(i) - '0';
            int secondNumDigit = secondNum.charAt(i) - '0';
            if(firstNumDigit != secondNumDigit) {
                return firstNumDigit - secondNumDigit;
            }
        }
        //It means everything before the dot is similar.
        return 0;
    }
    
    /**
     * Returns the number of characters before the decimal 
     * point starts.
     * 
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
