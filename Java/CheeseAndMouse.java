import java.util.Scanner;

public class CheeseAndMouse{
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);

		int N = sc.nextInt();
		int K = sc.nextInt();
		if(K == 0 || K > N){
			System.out.println(0);
		}else if(N%2 == 1 && K == N/2+1){
			System.out.println(N-1);
		}else{
			System.out.println(N-2);
		}
	}
}
