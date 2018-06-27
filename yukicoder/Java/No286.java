import java.util.*;

public class No286{
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);

		int n = sc.nextInt();
		int[] m = new int[n];
		for(int i = 0; i < n; i++){
			m[i] = sc.nextInt();
		}

		int[] dp = new int[1<<n];
		Arrays.fill(dp, 100000000);
		dp[0] = 0;
		for(int i = 0; i < (1<<n); i++){
			int now = 0;
			for(int j = 0; j < n; j++){
				if(((1<<j)&i) > 0){
					now += m[j];
				}
			}
			for(int j = 0; j < n; j++){
				if(((1<<j)&i) == 0){
					dp[i+(1<<j)] = Math.min(dp[i+(1<<j)], dp[i]+Math.max(m[j]-now%1000, 0));
				}
			}
		}
		System.out.println(dp[(1<<n)-1]);
	}
}
