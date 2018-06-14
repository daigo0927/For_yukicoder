import java.util.*;

public class No523{
	static long TMP = 1000000007;
	
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);

		long N = sc.nextLong();

		long ans = 1;
		// answer is 2N!/2!^N
		for(long i = N; i > 0; i--){
			ans = (ans*i)%TMP;
			ans = (ans*(2*i-1))%TMP;
		}
		System.out.println(ans);
	}
}
