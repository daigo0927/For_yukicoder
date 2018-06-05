import java.util.*;

public class No007{
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);
		
		int N = sc.nextInt();

		boolean prime[] = new boolean[N+1];
		for(int i = 2; i <= N; i++){
			prime[i] = true;
		}
		for(int i = 2; i < Math.sqrt(N); i++){
			if(prime[i]){
				for(int j = i+i; j <= N; j+=i){
					prime[j] = false;
				}
			}
		}

		boolean dp[] = new boolean[N+1];
		for(int i = 4; i <= N; i++){
			for(int j = i; j >= 2; j--){
				if(prime[j]){
					if(i-j >= 2 && !dp[i-j]){
						dp[i] = true;
						break;
					}
				}
			}
		}
		if(dp[N]) System.out.println("Win");
		else System.out.println("Lose");
	}
}
