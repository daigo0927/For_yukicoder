import java.util.Scanner;

public class Chokin{
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);
		int R = 0;
		int L = sc.nextInt();
		int M = sc.nextInt();
		int N = sc.nextInt();

		if(N >= 25){
			M += N/25;
			N -= 25*(N/25);
		}
		if(M >= 4){
			L += M/4;
			M -= 4*(M/4);
		}
		if(L >= 10){
			R += L/10;
			L -= 10*(L/10);
		}
		System.out.println(L+M+N);
	}
}

