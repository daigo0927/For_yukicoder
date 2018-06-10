import java.util.*;

public class No429{
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);

		int N = sc.nextInt();
		int K = sc.nextInt();
		int X = sc.nextInt();
		int[] start = new int[N];
		for(int i = 0; i < N; i++){
			start[i] = i+1;
		}
		
		int[][] AB = new int[K][2];
		for(int i = 0; i < K; i++){
			if(i == X-1){
				String a = sc.next();
				String b = sc.next();
				AB[i][0] = 0;
				AB[i][1] = 0;
				continue;
			}
			AB[i][0] = sc.nextInt();
			AB[i][1] = sc.nextInt();
		}
		
		int[] C = new int[N];
		for(int i = 0; i < N; i++){
			C[i] = sc.nextInt();
		}

		for(int i = 0; i < X-1; i++){
			start = perm(start, AB[i][0]-1, AB[i][1]-1);
		}
		for(int i = K-1; i > X-1; i--){
			C = perm(C, AB[i][0]-1, AB[i][1]-1);
		}

		List<Integer> answer = new ArrayList<Integer>();
		for(int i = 0; i < N; i++){
			if(start[i] != C[i]) answer.add(i+1);
		}

		System.out.println(answer.get(0)+" "+answer.get(1));
		
	}
	private static int[] perm(int[] list, int idx1, int idx2){
		int num1 = list[idx1];
		int num2 = list[idx2];
		list[idx1] = num2;
		list[idx2] = num1;
		return list;
	}
}
