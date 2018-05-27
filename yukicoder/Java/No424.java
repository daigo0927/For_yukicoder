import java.util.*;

public class No424{
	
	static int h, w, sx, sy, gx, gy;
	static String[] B;
	static int[] dx = {0, 1, 0, -1};
	static int[] dy = {1, 0, -1, 0};
	static boolean[][] visited;

	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);

		h = sc.nextInt();
		w = sc.nextInt();
		sx = sc.nextInt();
		sy = sc.nextInt();
		gx = sc.nextInt();
		gy = sc.nextInt();
		B = new String[h];
		for(int i = 0; i < h; i++){
			B[i] = sc.next();
		}
		visited = new boolean[h][w];
		visited[sx-1][sy-1] = true;
		dfs(sx-1, sy-1);

		if(visited[gx-1][gy-1]) System.out.println("YES");
		else System.out.println("NO");
	}

	private static void dfs(int x, int y){
		for(int dir = 0; dir < 4; dir++){
			int x1 = x + dx[dir];
			int y1 = y + dy[dir];
			if(0 <= x1 && x1 < h && 0 <= y1 && y1 < w){
				if(Math.abs((int)B[x1].charAt(y1) - (int)B[x].charAt(y)) <= 1
				   && !visited[x1][y1]){
					visited[x1][y1] = true;
					dfs(x1, y1);
				}
			}

			int x2 = x + 2*dx[dir];
			int y2 = y + 2*dy[dir];
			if(0 <= x2 && x2 < h && 0 <= y2 && y2 < w){
				if(B[x2].charAt(y2) == B[x].charAt(y)
				   && (int)B[x1].charAt(y1) < (int)B[x].charAt(y)){
					if(!visited[x2][y2]){
						visited[x2][y2] = true;
						dfs(x2, y2);
					}
				}
			}
		}
	}
}
