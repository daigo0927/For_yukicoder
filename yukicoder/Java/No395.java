import java.util.Scanner;

public class No395{
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);

		int A = sc.nextInt();
		if(A < 15) System.out.println(-1);
		else System.out.println(A-7);
	}
}
