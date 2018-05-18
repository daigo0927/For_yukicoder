import java.util.Scanner;

public class No388{
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);
		int s = sc.nextInt();
		int f = sc.nextInt();

		int num_stair = s/f;
		System.out.println(num_stair+1);
	}
}
