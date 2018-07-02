import java.util.*;

public class No141{
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);

		int m = sc.nextInt();
		int n = sc.nextInt();
		int x = m, y = n, tmp;
		while((tmp = x%y) != 0){
			x = y;
			y = tmp;
		}
		if(y > 1){
			m /= y;
			n /= y;
		}

		int count = 0;
		while(m != n){
			if(n == 1){
				count += m-1;
				break;
			}
			if(m > n){
				m -= n;
			}
			else{
				int l = m;
				m = n;
				n = l;
			}
			// System.out.println(m+"/"+n);
			count++;
		}
		System.out.println(count);
	}
}
