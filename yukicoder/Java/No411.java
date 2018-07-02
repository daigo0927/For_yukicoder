import java.util.*;

public class No411{
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);

		int n = sc.nextInt();
		int k = sc.nextInt();
		if(k == 1){
			System.out.println(aasort(n));
		}else{
			System.out.println((int)Math.pow(2, n-k));
		}
	}
	private static int aasort(int n){
		if(n == 2){
			return 0;
		}else{
			return (int)Math.pow(2, n-2)-1 + aasort(n-1);
		}
	}
}
