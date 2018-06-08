import java.util.*;

public class No058{
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);

		int N = sc.nextInt();
		int K = sc.nextInt();

		int win = 0;
		int num_sample = 10000000;
		Random rand = new Random();
		for(int i = 0; i < num_sample; i++){
			int taro_score = 0;
			int jiro_score = 0;
			for(int n = 0; n < N; n++){
				if(n < K){
					taro_score += rand.nextInt(3)+3;
				}else taro_score += rand.nextInt(6);
				jiro_score += rand.nextInt(6);
			}
			if(taro_score > jiro_score) win++;
		}
		System.out.println((double)win/(double)num_sample);
	}
}
