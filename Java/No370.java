import java.util.Scanner;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
import java.util.Arrays;

public class No370{
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);

		int N = sc.nextInt();
		int M = sc.nextInt();
		int[] D = new int[M];
		int num_trash_minus = 0;
		int num_trash_plus = 0;
		for(int i = 0; i < M; i++){
			D[i] = sc.nextInt();
			if(D[i] < 0){
				num_trash_minus++;
			}else{
				num_trash_plus++;
			}
		}
		int[] D_minus = new int[num_trash_minus];
		int minus_idx = 0;
		int[] D_plus = new int[num_trash_plus];
		int plus_idx = 0;
		for(int i = 0; i < M; i++){
			if(D[i] < 0){
				D_minus[minus_idx] = D[i];
				minus_idx++;
			}else{
				D_plus[plus_idx] = D[i];
				plus_idx++;
			}
		}

		int walk_min = 1000000000;
		for(int i = 0; i <= N; i++){
			if(i > num_trash_minus || N-i > num_trash_plus){
				continue;
			}
			int walk_minus = 2*search(D_minus, i) + search(D_plus, N - i);
			int walk_plus = search(D_minus, i) + 2*search(D_plus, N - i);

			if(Math.min(walk_minus, walk_plus) < walk_min){
				walk_min = Math.min(walk_minus, walk_plus);
			}
		}
		
		System.out.println(walk_min);
	}

	private static int search(int[] d, int n){
		int[] d_abs = new int[d.length];
		for(int i = 0; i < d.length; i++){
			d_abs[i] = Math.abs(d[i]);
		}
		Arrays.sort(d_abs);

		if(n > 0){
			return d_abs[n-1];
		}else{
			return 0;
		}
		
	}
}
