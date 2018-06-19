import java.util.*;
import java.io.*;

public class No491{
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);

		long N = sc.nextLong();
		long tmp = (long)Math.pow(10, 9) + 1;
		if(N < tmp) System.out.println(0);
		else{
			long div = N/tmp;
			String s = String.valueOf(div);
			int l = s.length();
			
			long ans = 0;
			for(int i = 1; i <= l; i++){
				int start;
				if(i%2 != 0) start = (int)Math.pow(10, i/2);
				else start = (int)Math.pow(10, i/2-1);
				
				for(int d = start; d < 10*start; d++){
					int mirror = symmetry(d, i%2!=0);
					if(mirror > div) break;
					else ans++;
				}
			}
			System.out.println(ans);
		}
	}
	
	private static int symmetry(int n, boolean odd){
		String s = String.valueOf(n);
		int l = s.length();
		StringBuilder sb;
		if(odd){
			sb = new StringBuilder(s.substring(0, l-1));
		}else{
			sb = new StringBuilder(s);
		}
		int mirror = Integer.parseInt(s+sb.reverse().toString());
		return mirror;
	}
}
