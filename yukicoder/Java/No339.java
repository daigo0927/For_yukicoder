import java.util.*;

public class No339{
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);

		int N = sc.nextInt();
		int[] A = new int[N];
		for(int i = 0; i < N; i++){
			A[i] = sc.nextInt();
		}
		Arrays.sort(A);
		int min_A = A[0];
		int gcd = 100;
		for(int i = 1; i < N; i++){
			int gcd_tmp = get_gcd(min_A, A[i]);
			if(gcd_tmp < gcd) gcd = gcd_tmp;
		}
		System.out.println(100/gcd);
	}
	private static int get_gcd(int x, int y){
		int tmp;
		while((tmp  = x%y) != 0){
			x = y;
			y = tmp;
		}
		return y;
	}
}
