import java.util.*;

public class No607{
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);

		int N = sc.nextInt();
		int M = sc.nextInt();
		int[][] a = new int[M][N];
		for(int m = 0; m < M; m++){
			for(int n = 0; n < N; n++){
				if(m == 0){
					a[m][n] = sc.nextInt();	
				}else{
					a[m][n] = sc.nextInt() + a[m-1][n];
				}
			}
		}
		// System.out.println(Arrays.deepToString(a));
		System.out.println(is777(a)? "YES" : "NO");
	}

	private static boolean is777(int[][] passengers){
		
		for(int m = 0; m < passengers.length; m++){
			int num_passengers = passengers[m][0];
			int head = 1;
			int tail = 0;
			while(true){
				if(num_passengers < 777){
					if(head == passengers[0].length) break;
					num_passengers += passengers[m][head];
					head++;
				}else if(num_passengers > 777){
					if(tail == passengers[0].length) break;
					num_passengers -= passengers[m][tail];
					tail++;
				}else{
					return true;
				}
				// System.out.println(m + " " + num_passengers);
			}
		}
		return false;
	}
}
