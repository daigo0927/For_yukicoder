import java.util.Scanner;

public class No036{
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);
		long N = sc.nextLong();

		int num_prime_factor = 0;
		for(int p = 2; p < Math.sqrt(N); p++){
			while(N%p == 0){
				N /= p;
				num_prime_factor++;
			}
		}
		
		if(num_prime_factor >= 2) System.out.println("YES");
		else System.out.println("NO");
		
	}
}
