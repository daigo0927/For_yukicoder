import java.util.Scanner;

public class No161{
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);

		int num_G = sc.nextInt();
		int num_C = sc.nextInt();
		int num_P = sc.nextInt();
		String[] S = sc.next().split("");
		int num_G_you = 0;
		int num_C_you = 0;
		int num_P_you = 0;
		for(int i = 0; i < S.length; i++){
			if(S[i].equals("G")) num_G_you++;
			else if(S[i].equals("C")) num_C_you++;
			else num_P_you++;
		}

		int score = 0;

		// win game
		int num_G_C = Math.min(num_G, num_C_you);
		score += 3*num_G_C;
		num_G -= num_G_C;
		num_C_you -= num_G_C;

		int num_C_P = Math.min(num_C, num_P_you);
		score += 3*num_C_P;
		num_C -= num_C_P;
		num_P_you -= num_C_P;

		int num_P_G = Math.min(num_P, num_G_you);
		score += 3*num_P_G;
		num_P -= num_P_G;
		num_G_you -= num_P_G;

		// Draw game
		score += Math.min(num_G, num_G_you);
		score += Math.min(num_C, num_C_you);
		score += Math.min(num_P, num_P_you);

		System.out.println(score);
	}
}
