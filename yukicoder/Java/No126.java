import java.util.*;

public class No126{
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);

		int a = sc.nextInt();
		int b = sc.nextInt();
		int s = sc.nextInt();

		if(s == 1){
			System.out.println(Math.abs(s-a)+s);
			return;
		}
		if(Math.abs(s-a) <= Math.abs(s-b)){
			System.out.println(Math.abs(s-a)+s);
		}else{
			if(Math.abs(a-s) <= (s-1)){
				System.out.println(Math.abs(s-b)+Math.abs(a-s)+a);
			}else{
				System.out.println(Math.abs(s-b)+(s-1)+Math.abs(a-1)+1);
			}
		}
	}
}
