import java.util.*;

public class No080{
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);

		int d = sc.nextInt();
		if(d < 4){
			System.out.println(0);
			return;
		}
		if(d%2 != 0) d--;
		d /= 2;

		if(d%2 == 0){
			System.out.println((d/2)*(d/2));
		}else{
			System.out.println((d/2)*(d/2+1));
		}
	}
}
