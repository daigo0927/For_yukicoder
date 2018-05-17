import java.util.Scanner;

public class WhichIsNext{
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);

		String S = sc.nextLine();
		for(int i = 0; i < 8; i++){
			
			String[] row = sc.nextLine().split("");
			for(int j = 0; j < 8; j++){
				if(!row[j].equals(".")){
					if(S.equals("oda")) S = "yukiko";
					else S = "oda";
				}
			}
		}
		System.out.println(S);
	}
}
