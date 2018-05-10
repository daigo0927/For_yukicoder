import java.util.Scanner;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
import java.util.Arrays;

public class GetMed{
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		double[] A = new double[N];
		for(int i=0; i<N; i++){
			A[i] = sc.nextDouble();
		}
		Arrays.sort(A);
		if(N%2 == 0){
			System.out.println((A[N/2-1]+A[N/2])/2);
		}else{
			System.out.println(A[(N-1)/2]);
		}
	}
}
