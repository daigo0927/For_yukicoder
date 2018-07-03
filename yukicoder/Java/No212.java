import java.util.*;

public class No212{
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);

		int p = sc.nextInt();
		int c = sc.nextInt();
		double e_p = (2+3+5+7+11+13)/6.0;
		double e_c = (4+6+8+9+10+12)/6.0;

		double ans = Math.pow(e_p, p)*Math.pow(e_c, c);
		System.out.println(ans);
	}
}
