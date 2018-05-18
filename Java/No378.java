import java.util.Scanner;

public class No378{
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);

		long N = sc.nextLong();
		long fame = N*2;
		while(true){
			fame -= N;
			N = N/2;
			if(N == 0){
				System.out.println(fame);
				break;
			}
		}
	}
}
