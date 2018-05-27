import java.util.*;

public class No175{
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);

		int L = sc.nextInt();
		int N = sc.nextInt();
		String[] S = new String[N];
		for(int i = 0; i < N; i++){
			S[i] = sc.next();
		}
		System.out.println((int)Math.pow(2, L-3)*N);
	}
}
