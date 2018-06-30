import java.util.*;

public class No306{
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);

		double ax = sc.nextDouble();
		double ay = sc.nextDouble();
		double bx = sc.nextDouble();
		double by = sc.nextDouble();

		double py;
		if(ay > by){
			py = (bx/(ax+bx))*(ay-by) + by;
		}else if(by > ay){
			py = (ax/(ax+bx))*(by-ay) + ay;
		}else{
			py = ay;
		}
		System.out.println(py);
	}
}
