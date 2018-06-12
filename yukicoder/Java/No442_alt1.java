import java.util.*;

public class No442_alt1{
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);

		long a = sc.nextLong();
		long b = sc.nextLong();

		// gcd(A+B, A*B);
		// = g*gcd(a+b, a*b*g); // g = gcd(A, B), a = A/g, b = B/g;
		// = g*gcd(a+b, g); // a, b are disjoint, so a+b, a*b are also disjoint
		long g = gcd(a, b);
		long gd = gcd((a+b)/g, g);
		
		System.out.println(g*gd);
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
