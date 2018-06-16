import java.util.*;

public class No533{
	public static void main(String[] args){
		long mod = 1000000007;
		
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();

		long[][] dp = new long[3][N+1];
		dp[0][1] = 1;
		if(N > 1) dp[1][2] = 1;
		if(N > 2){
			dp[0][3] = 1;
			dp[1][3] = 1;
			dp[2][3] = 1;
		}
		for(int i = 4; i < N+1; i++){
			dp[0][i] = (dp[1][i-1] + dp[2][i-1])%mod;
			dp[1][i] = (dp[0][i-2] + dp[2][i-2])%mod;
			dp[2][i] = (dp[0][i-3] + dp[1][i-3])%mod;
		}
		long ans = dp[0][N];
		ans = (ans + dp[1][N])%mod;
		ans = (ans + dp[2][N])%mod;
		System.out.println(ans);
	}
}
