import java.util.*;

public class No652{
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);

		int a = sc.nextInt();
		int b = sc.nextInt();
		String xx = sc.next();
		if(!xx.contains(".")){
			xx.concat(".0");
		}
		double x;
		if(xx.contains("+")){
			x = Double.valueOf(xx.substring(4));
		}else{
			x = -Double.valueOf(xx.substring(4));
		}
		double diff = Math.round((x-9.0)*100000)/100000.0;
		int a_diff = (int)((diff*60.0)/60.0);
		int b_diff = (int)((diff*60.0)%60.0);
		// System.out.println(diff + " " + a_diff + " " + b_diff);

		int a_new = a + a_diff;
		int b_new = b + b_diff;
		if(b_new >= 60){
			b_new -= 60;
			a_new += 1;
		}else if(b_new < 0){
			b_new += 60;
			a_new -= 1;
		}
		if(a_new >= 24) a_new -= 24;
		else if(a_new < 0) a_new += 24;

		System.out.println(String.format("%02d", a_new) + ":" + String.format("%02d", b_new));
	}
}
