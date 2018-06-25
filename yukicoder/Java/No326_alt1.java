import java.util.*;

public class No326_alt1{
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);

		int N = sc.nextInt();
		int K = sc.nextInt();
		ArrayList<Integer> A_tmp = new ArrayList<Integer>(N);
		for(int i = 0; i < N; i++){
			A_tmp.add(i+1);
		}
		for(int i = 0; i < K; i++){
			int x = sc.nextInt()-1;
			int y = sc.nextInt()-1;
			int tmp = A_tmp.get(x);
			A_tmp.set(x, A_tmp.get(y));
			A_tmp.set(y, tmp);
		}

		
		ArrayList<Integer> A_end = new ArrayList<Integer>(N);
		for(int i = 0; i < N; i++) A_end.add(0);
		for(int i = 0; i < N; i++){
			int idx_end = sc.nextInt()-1;
			A_end.set(idx_end, i+1);
		}

		// System.out.println(A_tmp.toString());
		// System.out.println(A_end.toString());
				ArrayList<Integer> ans = new ArrayList<Integer>(N*N/2);
		for(int i = 0; i < N; i++){
			if(A_tmp.get(i) != A_end.get(i)){
				int a_end = A_end.get(i);
				int idx = A_tmp.indexOf(a_end);
				for(int j = idx-1; j >= i; j--){
					A_tmp.set(j+1, A_tmp.get(j));
					ans.add(j);
				}
				A_tmp.set(i, a_end);
			}
		}

		System.out.println(ans.size());
		for(int idx:ans){
			System.out.println((idx+1) +" "+ (idx+2));
		}
	}
}
