import java.util.*;

public class No478{
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);

		int n = sc.nextInt();
		int k = sc.nextInt();

		StringBuilder sb = new StringBuilder();
		int v = 2;
		boolean down = true;
		for(int i = 0; i < n; i++){
			if(i <= k){
				sb.append(0);
				sb.append(" ");
			}
			else{
				if(down){
					sb.append(v--);
					sb.append(" ");
					down = false;
				}else{
					sb.append(v);
					sb.append(" ");
					v += 2;
					down = true;
				}
			}
		}
		System.out.println(sb);
	}
}
