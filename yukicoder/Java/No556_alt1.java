import java.util.*;

public class No556_alt1{
	public static class UnionFind{
		int[] par;

		public UnionFind(int n){
			this.par = new int[n];
			Arrays.fill(par, -1);
		}
		
		public int find(int x){
			if(par[x] < 0){
				return x;
			}else{
				return par[x] = find(par[x]);
			}
		}

		public boolean union(int x, int y){
			x = find(x);
			y = find(y);
			if(x == y) return false;

			if(par[x] < par[y]){
				par[x] += par[y];
				par[y] = x;
			}else if(par[x] > par[y]){
				par[y] += par[x];
				par[x] = y;
			}else if(x < y){
				par[x] += par[y];
				par[y] = x;
			}else{
				par[y] += par[x];
				par[x] = y;
			}
			return true;
		}

		public int size(int x){
			return -par[find(x)];
		}
	}
	
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);
		
		int n = sc.nextInt();
		int m = sc.nextInt();

		UnionFind uf = new UnionFind(n);
		for(int i = 0; i < m; i++){
			int a = sc.nextInt()-1;
			int b = sc.nextInt()-1;
			uf.union(a, b);
		}

		for(int i = 0; i < n; i++){
			System.out.println(uf.find(i)+1);
		}
	}
}
