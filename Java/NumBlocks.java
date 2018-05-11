import java.util.Scanner;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
import java.util.Arrays;

public class NumBlocks{
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);

		int L = sc.nextInt();
		int N = sc.nextInt();
		
		int[] W = new int[N];
		for(int i = 0; i < N; i++){
			W[i] = sc.nextInt();
		}
		Arrays.sort(W);
		int blocks_width = 0;
		int num_blocks = 0;
		for(int i = 0; i < N; i++){
			if(blocks_width + W[i] > L){
				break;
			}else{
				blocks_width += W[i];
				num_blocks++;
			}
		}
		System.out.println(num_blocks);
	}
}
