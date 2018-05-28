import java.util.*;

public class No396{
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int M = sc.nextInt();
		int X = sc.nextInt();
		int Y = sc.nextInt();

		if(X%(2*M) == Y%(2*M) || (X+Y)%(2*M) == 1){
			System.out.println("YES");
		}else System.out.println("NO");
	}
}
