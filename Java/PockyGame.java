import java.util.Scanner;

public class PockyGame{
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);
		int L = sc.nextInt();
		int K = sc.nextInt();

		int n = 0;
		if(L%(K*2) == 0){
			n = L/(K*2);
		}else{
			n = L/(K*2)+1;
		}
		System.out.println(K*(n-1));
		
	}
}
