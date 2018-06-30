import java.util.*;

public class No030{
	static int[] dp;
	static int[][] in;
	
	static int dfs(int i, int n){
		if(i == n) return 1;
		if(dp[i] != 0) return dp[i];
		int res = 0;
		for(int j = 1; j < 101; j++){
			if(in[i][j] != 0){
				res += in[i][j]*dfs(j, n);
			}
		}
		return dp[i] = res;
	}
	
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);

		int n = sc.nextInt();
		int m = sc.nextInt();
		dp = new int[101];
		int[] ans = new int[101];
		Arrays.fill(ans, -1);
		in = new int[101][101];
		for(int i = 0; i < m; i++){
			int p = sc.nextInt();
			int q = sc.nextInt();
			int r = sc.nextInt();
			in[p][r] = q;
		}

		for(int i = 1; i < n; i++){
			boolean flg = true;
			for(int j = 1; j < 101; j++){
				if(in[j][i] != 0){
					System.out.println(0);
					flg = false;
					break;
				}
			}
			if(flg){
				System.out.println(dfs(i, n));
			}
		}
	}
}
