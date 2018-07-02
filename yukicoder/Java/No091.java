import java.util.*;

public class No091{
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);

		int r = sc.nextInt();
		int g = sc.nextInt();
		int b = sc.nextInt();
		int[] rgb = new int[]{r, g, b};

		while(true){
			Arrays.sort(rgb);
			if(rgb[2]-rgb[0] <= 2){
				break;
			}else{
				rgb[0] += 1;
				rgb[2] -= 2;
			}
		}
		System.out.println(rgb[0]);
	}
}
