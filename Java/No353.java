import java.util.Scanner;
import java.math.BigDecimal;

public class No353{
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);

		BigDecimal A = new BigDecimal(sc.next());
		BigDecimal B = new BigDecimal(sc.next());
		System.out.println(A.add(B));
	}
}
