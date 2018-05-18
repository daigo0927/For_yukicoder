import java.util.Scanner;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
import java.math.BigDecimal;

public class No056{
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);

		BigDecimal D = new BigDecimal(sc.next());
		BigDecimal P = new BigDecimal(sc.next());
		BigDecimal t = new BigDecimal("1");
		BigDecimal hund = new BigDecimal("100");
		BigDecimal tax = t.add(P.divide(hund));
		BigDecimal value = D.multiply(tax);

		System.out.println(value.intValue());
	}
}
