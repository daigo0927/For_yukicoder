import java.util.Scanner;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
import java.util.Arrays;

public class PermuteStrings{
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);

		String[] A = sc.next().split("");
		String[] B = sc.next().split("");
		Arrays.sort(A);
		Arrays.sort(B);

		for(int i = 0; i < A.length; i++){
			if(!A[i].equals(B[i])){
				System.out.println("NO");
				break;
			}
			if(i == A.length-1){
				System.out.println("YES");
			}
		}
		
	}
}
