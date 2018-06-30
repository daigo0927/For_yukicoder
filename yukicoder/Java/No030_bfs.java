import java.util.*;

public class No030{
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);

		int n = sc.nextInt();
		int m = sc.nextInt();

		int[][] list = new int[n][n];
		for(int i = 0; i < n; i++){
			Arrays.fill(list[i], 0);
		}
		for(int i = 0; i < m; i++){
			int p = sc.nextInt()-1;
			int q = sc.nextInt();
			int r = sc.nextInt()-1;
			list[r][p] = q;
		}
		// System.out.println(Arrays.deepToString(list));
		long[] ans = new long[n-1];
		Arrays.fill(ans, 0);
		LinkedList<Integer> link = new LinkedList<Integer>();
		for(int i = 0; i < n-1; i++){
			ans[i] = list[n-1][i];
			if(list[n-1][i] > 0){
				link.offer(i);
			}
		}

		while(link.size() > 0){
			int idx = link.poll();
			boolean start = true;
			long num = ans[idx];
			for(int i = 0; i < n-1; i++){
				ans[i] += num*list[idx][i];
				if(list[idx][i] > 0){
					link.offer(i);
					start = false;
				}
			}
			if(!start){
				ans[idx] = 0;
			}
			// System.out.println(link);
		}
		for(int i = 0; i < n-1; i++){
			System.out.println(ans[i]);
		}
	}
}
