import java.util.*;

public class No638{
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);

		long N = sc.nextLong();
		long result = judge(N);
		if(result == -1) System.out.println(result);
		else System.out.println(result + " " + (N-result));

	}

	private static long judge(long N){
		if(N < 3) return -1;
		
		for(long a = 3; a <= N/2; a++){
			if(!is2pow(a) && !is2pow(N-a)){
				return a;
			}
		}
		return -1;
	}
	private static boolean is2pow(long a){
		if((a & (a-1)) == 0) return true;
		else return false;
	}
}
