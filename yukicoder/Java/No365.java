import java.util.*;

public class No365{
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);

		int n = sc.nextInt();
		int[] a = new int[n];
		for(int i = 0; i < n; i++){
			a[i] = sc.nextInt();
		}
		int m = n;
		int count = 0;
		for(int i = n-1; i >= 0; i--){
			if(a[i] == m){
				m--;
			}else{
				count++;
			}
		}
		System.out.println(count);
	}
}
