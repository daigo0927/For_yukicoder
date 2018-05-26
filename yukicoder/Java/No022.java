import java.util.*;

public class No022{
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int K = sc.nextInt();
		K--;
		String s = sc.next();
		char[] S = s.toCharArray();

		StringBuilder sb = new StringBuilder();
		sb.append(String.valueOf(S[K]));
		if(S[K] == '('){
			while(sb.length() > 0){
				if(sb.charAt(sb.length() - 1) == S[K+1]){
					sb.append(S[K+1]);
				}else{
					sb.deleteCharAt(sb.length()-1);
				}
				K++;
			}
			System.out.println(K+1);
		}
		else{
			while(sb.length() > 0){
				if(sb.charAt(sb.length() - 1) == S[K-1]){
					sb.append(S[K-1]);
				}else{
					sb.deleteCharAt(sb.length()-1);
				}
				K--;
			}
			System.out.println(K+1);
		}
		// for(int i = 0; i < S.length; i++){
		// 	System.out.println(S[i]);
		// }

	}
}
