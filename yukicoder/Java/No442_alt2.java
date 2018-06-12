import java.util.*;
import java.math.*;

public class No442_alt2{
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);

		BigInteger a = sc.nextBigInteger();
		BigInteger b = sc.nextBigInteger();
		BigInteger sum = a.add(b);
		BigInteger mul = a.multiply(b);
		System.out.println(sum.gcd(mul));
		
	}
}
