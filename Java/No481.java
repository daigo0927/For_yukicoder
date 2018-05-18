import java.util.Scanner;

public class No481{
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);
		for(int i = 1; i <= 9; i++){
			int b = sc.nextInt();
			if(b != i){
				System.out.println(i);
				break;
			}
			if(i == 9 && b == 9){
				System.out.println(10);
			}
		}
	}
}
