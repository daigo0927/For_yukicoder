import java.util.*;

public class No397{
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);

		int N = sc.nextInt();
		int[] A = new int[N];
		for(int i = 0; i < N; i++){
			A[i] = sc.nextInt();
		}
		int M = 0;
		int[][] uv = new int[N*N][2];
		for(int i = 0; i < N; i++){
			for(int j = 0; j < N - 1 - i; j++){
				if(A[j] > A[j+1]){
					int tmp = A[j];
					A[j] = A[j+1];
					A[j+1] = tmp;
					uv[M][0] = j;
					uv[M][1] = j+1;
					M++;
				}
			}
		}
		System.out.println(M);
		for(int i = 0; i < M; i++){
			System.out.println(uv[i][0] + " " + uv[i][1]);
		}
		int a = sc.nextInt();

	}
}
