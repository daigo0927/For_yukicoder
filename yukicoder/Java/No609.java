import java.util.*;

public class No609{
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);

		int N = sc.nextInt();
		long[] Y = new long[N];
		for(int i = 0; i < N; i++){
			Y[i] = sc.nextLong();
		}
		Arrays.sort(Y);

		long med;
		if(N%2 != 0){
			med = Y[(N-1)/2];
		}else{
			long med_tmp = Y[N/2-1] + Y[N/2];
			if(med_tmp%2 > 0){
				med = med_tmp/2 + 1;
			}else{
				med = med_tmp/2;
			}
		}

		long diff = 0;
		for(int i = 0; i < N; i++){
			diff += Math.abs(med - Y[i]);
		}
		
		System.out.println(diff);
	}
}
