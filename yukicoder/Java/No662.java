import java.util.*;

public class No662{
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);
		
		String[] str = new String[5];
		int[] coin = new int[5];
		for(int i = 0; i < 5; i++){
			str[i] = sc.next();
			coin[i] = sc.nextInt();
		}

		long[] n = new long[3];
		long[][] reels = new long[3][5];
		
		for(int i = 0; i < 3; i++){
			Arrays.fill(reels[i], 0);
			n[i] = sc.nextInt();
			for(int j = 0; j < n[i]; j++){
				int idx = Arrays.asList(str).indexOf(sc.next());
				reels[i][idx]++;
			}
		}
		// System.out.println(Arrays.deepToString(reels));

		long[] num_atari = new long[5];
		long score_sum = 0;
		for(int i = 0; i < 5; i++){
			num_atari[i] = reels[0][i]*reels[1][i]*reels[2][i]*5;
			score_sum += coin[i]*num_atari[i];
		}
		System.out.println((double)score_sum/(double)(n[0]*n[1]*n[2]));
		for(int i = 0; i < 5; i++) System.out.println(num_atari[i]);

	}
}
