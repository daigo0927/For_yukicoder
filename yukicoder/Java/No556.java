import java.util.*;

public class No556{
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);

		int n = sc.nextInt();
		int m = sc.nextInt();
		ArrayList<Integer> monkeys = new ArrayList<Integer>(n);
		for(int i = 0; i < n; i++){
			monkeys.add(i+1);
		}
		for(int i = 0; i < m; i++){
			int a = sc.nextInt();
			int b = sc.nextInt();

			int boss_a = monkeys.get(a-1);
			int boss_b = monkeys.get(b-1);
			int num_teama = 0, num_teamb = 0;
			for(int j = 0; j < n; j++){
				if(monkeys.get(j) == boss_a) num_teama++;
				if(monkeys.get(j) == boss_b) num_teamb++;
			}

			if(num_teama > num_teamb){
				for(int j = 0; j < n; j++){
					if(monkeys.get(j) == boss_b) monkeys.set(j, boss_a);
				}
			}else if(num_teamb > num_teama){
				for(int j = 0; j < n; j++){
					if(monkeys.get(j) == boss_a) monkeys.set(j, boss_b);
				}
			}else if(boss_a < boss_b){
				for(int j = 0; j < n; j++){
					if(monkeys.get(j) == boss_b) monkeys.set(j, boss_a);
				}
			}else if(boss_b < boss_a){
				for(int j = 0; j < n; j++){
					if(monkeys.get(j) == boss_a) monkeys.set(j, boss_b);
				}
			}
			// System.out.println(monkeys.toString());
		}

		for(int i = 0; i < n; i++){
			System.out.println(monkeys.get(i));
		}
	}
}
