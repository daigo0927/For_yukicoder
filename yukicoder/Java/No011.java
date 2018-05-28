import java.util.*;

public class No011{
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);

		int W = sc.nextInt();
		int H = sc.nextInt();
		int N = sc.nextInt();

		ArrayList<Integer> mark_unique = new ArrayList<Integer>();
		ArrayList<Integer> num_unique = new ArrayList<Integer>();
		
		for(int i = 0; i < N; i++){
			int mark = sc.nextInt();
			if(!mark_unique.contains(mark)) mark_unique.add(mark);
			
			int num = sc.nextInt();
			if(!num_unique.contains(num)) num_unique.add(num);
		}
		
		int m_unique = mark_unique.size();
		int n_unique = num_unique.size();
		System.out.println(m_unique*H + n_unique*W - m_unique*n_unique - N);
	}
}
