import java.util.*;

public class No683{
	static boolean ans = false;
	
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);

		long A = sc.nextLong();
		long B = sc.nextLong();

		operate(A, B);
		System.out.println(ans? "Yes": "No");
	}
	private static void operate(long a, long b){
		if(a == 0 || b == 0){
			ans = true;
			return;
		}
		else if(a%2 == 0 && b%2 == 0){
			operate(a/2, b-1);
			operate(a-1, b/2);
		}else if(a%2 == 0 && b%2 != 0){
			operate(a/2, b-1);
		}else if(a%2 != 0 && b%2 == 0){
			operate(a-1, b/2);
		}
	}
}
