import java.util.Scanner;
import java.util.Arrays;

public class No120{
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		int[] result = new int[T];
		
		for(int i = 0; i < T; i++){
			int N = sc.nextInt();
			String[] l = new String[N];
			for(int n = 0; n < N; n++){
				l[n] = sc.next();
			}
			String L = String.join("", l);
			// System.out.println(L);

			result[i] = make_kadomatsu(L);
		}
		for(int i = 0; i < T; i++){
			System.out.println(result[i]);
		}
		
	}
	private static int make_kadomatsu(String take){
		int max = 0;
		int l = take.length();
		if(l < 3) return max;
		
		for(int i = 0; i < l; i++){
			for(int j = i+1; j < l; j++){
				for(int k = j+1; k < l; k++){
					int n1 = Integer.parseInt(""+take.charAt(i));
					int n2 = Integer.parseInt(""+take.charAt(j));
					int n3 = Integer.parseInt(""+take.charAt(k));
					max = make_k(n1, n2, n3);
						
					StringBuilder sb = new StringBuilder(take);
					sb.deleteCharAt(k);
					sb.deleteCharAt(j);
					sb.deleteCharAt(i);

					max += make_kadomatsu(sb.toString());
				}
			}
		}
		return max;
	}
	private static int make_k(int n1, int n2, int n3){
		int n[] = {n1, n2, n3};
		int make_able = 0;
		for(int i = 0; i < 3; i++){
			for(int j = 0; j < 3; j++){
				if(j == i) continue;
				for(int k = 0; k < 3; k++){
					if(k == j || k == i) continue;
					int a = n[i];
					int b = n[j];
					int c = n[k];
					if((a != b && b != c && c != a) &&
					   (b > Math.max(a, c) || b < Math.min(a, c))){
						make_able = 1;
					}
				}
			}
		}
		return make_able;
	}
}
