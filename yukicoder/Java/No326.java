import java.util.*;

public class No326{
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);

		int N = sc.nextInt();
		int K = sc.nextInt();
		int[] A_tmp = new int[N];
		for(int i = 0; i < N; i++){
			A_tmp[i] = i+1;
		}
		for(int i = 0; i < K; i++){
			int x = sc.nextInt()-1;
			int y = sc.nextInt()-1;
			int tmp = A_tmp[x];
			A_tmp[x] = A_tmp[y];
			A_tmp[y] = tmp;
		}

		int[] A = new int[N];
		for(int i = 0; i < N; i++){
			A[i] = sc.nextInt();
		}
		for(int i = 0; i < N; i++){
			A_tmp[i] = A[A_tmp[i]-1];
		}

		// System.out.println(Arrays.toString(A_tmp));
		ArrayList<Integer> ans = new ArrayList<Integer>();
		for(int i = 1; i < N; i++){
			for(int j = i-1; j >= 0; j--){
				if(A_tmp[j] > A_tmp[j+1]){
					int tmp = A_tmp[j];
					A_tmp[j] = A_tmp[j+1];
					A_tmp[j+1] = tmp;
					ans.add(j);
				}
			}
		}
		
		System.out.println(ans.size());
		for(int idx:ans){
			System.out.println((idx+1) +" "+ (idx+2));
		}
	}
}
