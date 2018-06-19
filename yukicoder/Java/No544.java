import java.util.*;

public class No544{
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);

		int N = sc.nextInt();
		int a = 0, b = 0;
		int N_ = N;
		for(int i = 9; i >= 0; i--){
			int div = N_/(int)Math.pow(10, i);
			if(div == 7) a += Math.pow(10, i);
			N_ -= div*Math.pow(10, i);
		}
		b = N - a;
		System.out.println(a + " " + b);
	}
}
