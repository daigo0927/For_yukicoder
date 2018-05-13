import java.util.Scanner;

public class PocketBiscuit{
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		boolean flg = true;
		if(N == 1){
			System.out.println(0);
			flg = false;
		}
		int num_bis = 1;
		int num_hit = 0;
		while(flg){
			if(num_bis*2<N){
				num_bis = num_bis*2;
				num_hit++;
			}else{
				System.out.println(num_hit+1);
				break;
			}
		}
	}
}
