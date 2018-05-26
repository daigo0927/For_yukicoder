import java.util.Scanner;

public class No264{
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int k = sc.nextInt();

		if(n == k-1 || (n == 2 && k == 0)){
			System.out.println("Won");
		}else if(n == k){
			System.out.println("Drew");
		}else{
			System.out.println("Lost");
		}
	}
}
