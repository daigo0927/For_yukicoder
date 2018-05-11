import java.util.Scanner;

public class Hajimeno_N_ho{
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);
		int a = sc.nextInt();
		int b = sc.nextInt();
		sc.close();

		int step = b/a;
		if(step*a == b){
			System.out.println(step);
		}else{
			System.out.println(step+1);
		}
	}
}
