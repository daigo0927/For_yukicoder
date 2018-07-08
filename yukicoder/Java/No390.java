import java.util.*;

public class No390{
	public static void main(String[] args){
		int max_x = 1000000;
		
		Scanner sc = new Scanner(System.in);

		int n = sc.nextInt();
		int[] x = new int[n];
		for(int i = 0; i < n; i++){
			x[i] = sc.nextInt();
		}
		Arrays.sort(x);

		int[] dp = new int[max_x+1];
		for(int i:x){
			dp[i] = 1;
		}

		int ans = 0;
		for(int i = 0; i <= max_x; i++){
			if(dp[i] <= 0){
				continue;
			}
			for(int j = i*2; j <= max_x; j += i){
				if(dp[j] >= 1){
					dp[j] = Math.max(dp[j], dp[i]+1);
				}
			}
			ans = Math.max(ans, dp[i]);
		}
		System.out.println(ans);
	}
}
