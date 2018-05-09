import java.util.Scanner;

public class SekainoNantoka{
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);
		int A = sc.nextInt();
		int B = sc.nextInt();

		for(int i= A; i<=B; i++){
			if(i%3==0 || String.valueOf(i).matches(".*3.*")){
				System.out.println(i);
			}
		}
	}
}
