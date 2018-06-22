import java.util.*;

public class No697{
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);

		int H = sc.nextInt();
		int W = sc.nextInt();
		int[] dx = {0, 1, 0, -1};
		int[] dy = {-1, 0, 1, 0};

		int[][] a = new int[H][W];
		for(int h = 0; h < H; h++){
			for(int w = 0; w < W; w++){
				a[h][w] = sc.nextInt();
			}
		}

		int ans = 0;
		for(int h = 0; h < H; h++){
			for(int w = 0; w < W; w++){
				if(a[h][w] == 1){
					ans++;

					LinkedList<ArrayList<Integer>> list = new LinkedList<>();
					ArrayList<Integer> wh = new ArrayList<Integer>();
					wh.add(w);
					wh.add(h);
					list.add(wh);
					a[h][w] = 0;
					
					while(list.size()>0){
						ArrayList<Integer> xy = list.poll();
						int x = xy.get(0), y = xy.get(1);
						// System.out.println(y+" "+x);
						
						for(int i = 0; i < 4; i++){
							int xx = x+dx[i], yy = y+dy[i];
							if(xx >= 0 && xx < W && yy >= 0 && yy < H){
								if(a[yy][xx] == 1){
									ArrayList<Integer> xy_new = new ArrayList<Integer>();
									xy_new.add(xx);
									xy_new.add(yy);
									list.add(xy_new);
									a[yy][xx] = 0;
								}
							}
						}
					}
				}
			}
		}
		System.out.println(ans);
	}
}

