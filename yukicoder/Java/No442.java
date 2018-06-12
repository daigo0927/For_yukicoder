import java.util.*;

public class No442{
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);

		long a = sc.nextLong();
		long b = sc.nextLong();

		long sum = a+b;
		long mul = a*b;

		long g1 = gcd(sum, a);
		sum /= g1;
		long g2 = gcd(sum, b);
		
		System.out.println(g1*g2);
	}
	private static long gcd(long x, long y){
		long tmp;
		while((tmp = x%y) != 0){
			x = y;
			y = tmp;
		}
		return y;
	}
}
