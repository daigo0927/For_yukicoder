import java.util.Scanner;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class NTimesSleep{
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);

		int N = sc.nextInt();
		int H = sc.nextInt();
		int M = sc.nextInt();
		int T = sc.nextInt();

		int sleep_time = T*(N-1);
		int min = M + sleep_time;
		int h_wake = (H+min/60)%24;
		int m_wake = min%60;

		System.out.println(h_wake);
		System.out.println(m_wake);
	}
}
