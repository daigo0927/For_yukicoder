import java.util.*;

public class No327{
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);

		long n = sc.nextLong();
		if(n < 26){
			System.out.println((char)(65+n));
			return;
		}
		
		StringBuilder sb = new StringBuilder();
		int pow = 1;
		while(true){
			if(n >= (long)Math.pow(26, pow)){
				n -= Math.pow(26, pow);
				pow++;
			}else{
				pow--;
				break;
			}
		}
		// System.out.println(pow);

		for(int p = pow; p >= 0; p--){
			long div = n/(long)Math.pow(26, p);
			sb.append((char)(65+div));
			n -= div*(long)Math.pow(26, p);
		}

		System.out.println(sb);
	}
}
