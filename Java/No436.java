import java.util.Scanner;

public class No436{
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);
		String[] s = sc.nextLine().split("");
		
		int num_c = 0;
		int num_w = 0;
		for(int i = 0; i < s.length; i++){
			if(s[i].equals("c")) num_c++;
			else num_w++;
		}
		if(num_c-1 <= num_w) System.out.println(num_c-1);
		else System.out.println(num_w);
		
	}
}
