import java.util.Scanner;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class No143{
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);

		int K = sc.nextInt();
		int N = sc.nextInt();
		int num_beans = K*N;
		
		int F = sc.nextInt();
		int num_eats = 0;
		for(int i = 0; i < F; i++){
			num_eats += sc.nextInt();
		}

		if(num_beans >= num_eats){
			System.out.println(num_beans - num_eats);
		}else{
			System.out.println("-1");
		}
	}
}
