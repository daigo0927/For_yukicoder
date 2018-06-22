import java.util.*;

public class No462{
	static long mod = (long)Math.pow(10, 9) + 7;
	
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);

		int N = sc.nextInt();
		int k = sc.nextInt();
		if(k == 0){
			System.out.println(fact(N));
			return;
		}

		long[] a = new long[k+1];
		for(int i = 0; i < k; i++){
			a[i] = sc.nextLong();
		}
		a[k] = (long)Math.pow(2, N) - 1;
		Arrays.sort(a);
		// System.out.println(Arrays.toString(a));
		
		for(int i = 1; i < k+1; i++){
			if((a[i] & a[i-1]) != a[i-1]){
				System.out.println(0);
				return;
			}
		}

		long ans = fact(Long.bitCount(a[0]));
		for(int i = 1; i < k+1; i++){
			long xor = a[i]^a[i-1];
			ans *= fact(Long.bitCount(xor));
			ans %= mod;
		}
		System.out.println(ans);
	}

	private static long fact(long n){
		if(n == 0) return 1;
		long ret = 1;
		for(long i = n; i > 0; i--){
				ret = ret*i%mod;
		}
		return ret;
	}
}
