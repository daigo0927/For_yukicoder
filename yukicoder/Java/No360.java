import java.util.*;

public class No360{
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);

		int[] D = new int[7];
		for(int i = 0; i < 7; i++){
			D[i] = sc.nextInt();
		}
		boolean ans = true;
		Arrays.sort(D);
		for(int i = 1; i < 6; i++){
			if(D[i] == D[i-1] && D[i] == D[i+1]) ans = false;
		}
		if(D[0] == D[1] || D[5] == D[6]) ans = false;
		if(D[1] == D[2] && D[4] == D[5]) ans = false;
		
		System.out.println(ans ? "YES": "NO");
	}
}
