import java.util.*;

public class No208{
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);

		int x = sc.nextInt();
		int y = sc.nextInt();
		int x2 = sc.nextInt();
		int y2 = sc.nextInt();

		if(x == y && x2 == y2 && x2 < x) System.out.println(x+1);
		else System.out.println(Math.max(x, y));
	}
}
