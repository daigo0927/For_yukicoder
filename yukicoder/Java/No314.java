import java.util.*;

public class No314{
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		long mod = 1000000007;
		if(N == 1) System.out.println(1);
		else if(N == 2) System.out.println(2);
		else{
			long KK = 1;
			long KP = 1;
			long PK = 0;
			long[] kk_kp_pk = new long[3];
			while(N-2 > 0){
				kk_kp_pk = kenkenpa(KK, KP, PK);
				KK = kk_kp_pk[0]%mod;
				KP = kk_kp_pk[1]%mod;
				PK = kk_kp_pk[2]%mod;
				N--;
			}
			System.out.println((KK+KP+PK)%mod);
		}
		
	}
	private static long[] kenkenpa(long KK, long KP, long PK){

		long[] kk_kp_pk = {PK, KK+PK, KP};
		return kk_kp_pk;
	}
}
