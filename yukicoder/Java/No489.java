import java.util.*;

public class No489{
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);

		int N = sc.nextInt();
		int D = sc.nextInt();
		int K = sc.nextInt();
		int[] x = new int[N];
		for(int i = 0; i < N; i++){
			x[i] = sc.nextInt();
		}
		int[] q = new int[N];
		int h = 0, t = -1;
		int diff = 0, a = 0, b = 0;
		for(int i = 0; i < N; i++){
			while(t >= h && q[h] < i-D) ++h;
			if(t >= h && x[i]-x[q[h]] > diff){
				diff = x[i] - x[q[h]];
				a = q[h];
				b = i;
			}
			while(t >= h && x[q[t]] > x[i]){
				--t;
			}

			q[++t] = i;
		}
		if(diff == 0) System.out.println(0);
		else{
			System.out.println((long)K*diff);
			System.out.println(a + " " + b);
		}
	}
}
