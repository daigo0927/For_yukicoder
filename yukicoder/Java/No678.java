import java.util.*;

public class No678{
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);

		int N = sc.nextInt();
		int xLB = sc.nextInt();
		int xRB = sc.nextInt();
		int[] beam = new int[1281];
		Arrays.fill(beam, xLB, xRB+1, 1);
		
		int[][] positions = new int[N][4];
		for(int n = 0; n < N; n++){
			for(int i = 0; i < 4; i++){
				positions[n][i] = sc.nextInt();
			}
		}
		int[] is_hit = new int[N];
		Arrays.fill(is_hit, 0);
		
		for(int h = 1680; h > 0; h--){
			for(int n = 0; n < N; n++){
				if(is_hit[n] == 1) continue;
				if(h < positions[n][3] && is_beam(beam, positions[n][0], positions[n][2])){
					is_hit[n] = 1;
					Arrays.fill(beam,
								Math.max(positions[n][0], 0),
								Math.min(positions[n][2]+1, 1281),
								0);
					// System.out.println("enemy " + n + " hit");
				}
			}
		}
		for(int n = 0; n < N; n++){
			System.out.println(is_hit[n]);
		}
	}
	private static boolean is_beam(int[] beam, int l, int r){
		l = Math.max(0, l);
		r = Math.min(r+1, 1281);
		for(int x = l; x < r; x++){
			if(beam[x] == 1) return true;
		}
		return false;
	}
}
