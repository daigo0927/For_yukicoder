import java.util.*;
import java.io.*;

public class No522{
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);
		PrintWriter pw = new PrintWriter(System.out);

		int n = sc.nextInt();

		for(int a = 1; a <= n/3; a++){
			for(int b = a; b <= (n-a)/2; b++){
				pw.println(a+" "+b+" "+(n-a-b));
			}
		}
		pw.flush();
	}
}
