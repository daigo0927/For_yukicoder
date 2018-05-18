import java.util.Scanner;

public class No163{
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);
		String password = sc.next();
		String[] ps = password.split("");
		String PS = "";
		for(int i = 0; i < ps.length; i++){
			if(ps[i].toLowerCase().equals(ps[i])){
				PS += ps[i].toUpperCase();
			}else{
				PS += ps[i].toLowerCase();
			}
		}
		System.out.println(PS);
	}
}
