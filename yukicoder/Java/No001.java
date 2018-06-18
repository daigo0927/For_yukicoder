import java.util.*;

public class No001{
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);

		int N = sc.nextInt();
		int count = 0;
		while(true){
			if(N == 1) break;
			
			if(N%2 == 0){
				N /= 2;
			}else{
				N++;
			}
			count++;
		}
		System.out.println(count);
	}
}
