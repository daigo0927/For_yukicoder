import java.util.*;

public class No120{
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		for(int t = 0; t < T; t++){
			int N = sc.nextInt();
			int[] l = new int[N];
			int[] count = new int[N];
			for(int n = 0; n < N; n++){
				l[n] = sc.nextInt();
			}
			Arrays.sort(l);
			int kind = 0;
			int c = 1;
			for(int i = 1; i < N; i++){
				if(l[i] == l[i-1]){
					c++;
				}else{
					count[kind++] = c;
					c = 1;
				}
			}
			count[kind++] = c;
			Arrays.sort(count);
			int max = 0;
			while(N-2 > 0 && count[N-3]>0){
				max++;
				count[N-3]--;
				count[N-2]--;
				count[N-1]--;
				Arrays.sort(count);
			}
			System.out.println(max);
		}
	}
}
