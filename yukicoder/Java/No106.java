import java.util.*;

public class No106{
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);

		int N = sc.nextInt();
		int K = sc.nextInt();

		int[] min_prime = new int[N+1];
		for(int i = 2; i < N+1; i++){
			if(min_prime[i] == 0){
				for(int j = 1; j*i < N+1; j++){
					min_prime[i*j]++;
				}
			}
		}
		int count = 0;
		for(int i = 2; i < N+1; i++){
			if(min_prime[i] >= K) count++;
		}
		System.out.println(count);
	}
}
