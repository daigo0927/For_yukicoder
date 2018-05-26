import java.util.Scanner;
import java.util.Arrays;

public class No110{
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);

		int N_w = sc.nextInt();
		int[] W = new int[N_w];
		for(int i = 0; i < N_w; i++){
			W[i] = sc.nextInt();
		}
		int N_b = sc.nextInt();
		int[] B = new int[N_b];
		for(int i = 0; i < N_b; i++){
			B[i] = sc.nextInt();
		}

		Arrays.sort(W);
		Arrays.sort(B);
		int height_w_start = stack(W, B);
		int height_b_start = stack(B, W);
		System.out.println(Math.max(height_w_start, height_b_start));
	}

	private static int stack(int[] block_0, int[] block_1){
		int height = 0;
		int width = 30;
		int max;
		boolean put_flg;
		while(true){
			max = 0;
			put_flg = false;
			for(int i = 0; i < block_0.length; i++){
				if(block_0[i] > max && block_0[i] < width){
					max = block_0[i];
					put_flg = true;
				}
			}
			if(put_flg)	height++;
			else break;
			width = max;
			
			max = 0;
			put_flg = false;
			for(int i = 0; i < block_1.length; i++){
				if(block_1[i] > max && block_1[i] < width){
					max = block_1[i];
					put_flg = true;
				}
			}
			if(put_flg) height++;
			else break;
			width = max;
		}
		return height;
	}
}
