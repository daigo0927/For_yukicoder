import java.util.*;

public class No688{
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);

		int k = sc.nextInt();
		if(k < 2){
			System.out.println(1);
			System.out.println(0);
			return;
		}
		
		int num_0 = 0, num_1 = 0;
		for(int i = 2; i < k; i++){
			int div = k/(i*(i-1)/2);
			if((div&(div-1)) == 0){
				num_1 = i;
				while(div > 1){
					div = div/2;
					num_0++;
				}
				break;
			}
		}
		// System.out.println(num_0+", "+num_1);
		System.out.println(num_0+num_1);
		StringBuilder ans = new StringBuilder(num_0+num_1);
		for(int i = 0; i < num_0; i++){
			ans.append("0 ");
		}
		for(int i = 0; i < num_1; i++){
			if(i < num_1-1) ans.append("1 ");
			else ans.append("1");
		}
		System.out.println(ans);
	}
}
