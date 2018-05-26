import java.util.*;

public class No334_2{
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		
		StringBuilder sb = new StringBuilder();
		int[] K = new int[N];
		for(int i = 0; i < N; i++){
			K[i] = sc.nextInt();
		}
		
		if(game(K)) System.out.println(ans[0]+" "+ans[1]+" "+ans[2]);
		else System.out.println(-1);
	}
	
	static int[] ans = new int[3];
	private static boolean game(int[] K){
		int n = K.length;
		for(int i = 0; i < n; i++){
			for(int j = i+1; j < n; j++){
				for(int k = j+1; k < n; k++){
					int a = K[i];
					int b = K[j];
					int c = K[k];
					if(b > Math.max(a, c) || b < Math.min(a, c)){
						int[] K_new = new int[n-3];
						int idx = 0;
						for(int l = 0; l < n; l++){
							if(l == i || l == j || l == k) continue;
							K_new[idx] = K[l];
							idx++;
						}
						if(!game(K_new)){
							ans[0] = i;
							ans[1] = j;
							ans[2] = k;
							return true; // D wins
						}
					}
				}
			}
		}
		return false; // D lose
	}
}
