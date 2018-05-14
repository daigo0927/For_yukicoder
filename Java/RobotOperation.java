import java.util.Scanner;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class RobotOperation{
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);

		int X = sc.nextInt();
		int Y = sc.nextInt();
		int L = sc.nextInt();

		int num_step = 0;
		if(X != 0 && Y >= 0){
			num_step += 1;
		}else if(Y < 0){
			num_step += 2;
		}
		
		if(X%L == 0){
			num_step += Math.abs(X)/L;
		}else{
			num_step += Math.abs(X)/L+1;
		}
		
		if(Y%L == 0){
			num_step += Math.abs(Y)/L;
		}else{
			num_step += Math.abs(Y)/L+1;
		}
		System.out.println(num_step);
		
	}
}
