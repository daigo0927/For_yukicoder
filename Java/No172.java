import java.util.*;

public class No172{
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);
		double x = Math.abs(sc.nextDouble());
		double y = Math.abs(sc.nextDouble());
		double r = sc.nextDouble();
		
		double R = Math.sqrt(Math.pow((x+y)/2, 2)*2);
		System.out.println((int)Math.ceil(Math.sqrt(2)*(R+r)));
	}
}
