import java.util.Scanner;
import java.util.Arrays;

public class CWWGame{
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);

		String s = sc.nextLine();
		int max_cww = new CWWGame().get_max_cww(s);
		System.out.println(max_cww);
	}

	int get_max_cww(String s){
		char[] ss = s.toCharArray();
		int n = s.length();
		int max_cww = 0;
		for(int i = 0; i < n; i++){
			for(int j = i+1; j < n; j++){
				for(int k = j+1; k < n; k++){
					if(ss[i] != '0' && ss[i] != ss[j] && ss[j] == ss[k]){
						StringBuilder sb = new StringBuilder();
						sb.append(ss[i]);
						sb.append(ss[j]);
						sb.append(ss[k]);
						int cww = Integer.parseInt(sb.toString());
						
						StringBuilder sb2 = new StringBuilder(s);
						sb2.deleteCharAt(k);
						sb2.deleteCharAt(j);
						sb2.deleteCharAt(i);

						max_cww = Math.max(max_cww, cww+get_max_cww(sb2.toString()));
					}
				}
			}
		}
		return max_cww;
	}
}
