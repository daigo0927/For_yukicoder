import java.util.*;

public class No517{
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);

		int n = sc.nextInt();
		HashMap<Character, Integer> map1 = new HashMap<>();
		HashMap<Integer, Character> map2 = new HashMap<>();
		HashMap<Integer, Integer> connect = new HashMap<>();

		int idx = 0;
		for(int i = 0; i < n; i++){
			char[] str = sc.next().toCharArray();
			for(int j = 0; j < str.length; j++){
				map1.put(str[j], idx);
				map2.put(idx, str[j]);
				if(j != str.length-1){
					connect.put(idx, idx+1);
				}
				idx++;
			}
		}

		int length = idx;
		if(length == 1){
			System.out.println(map2.get(0));
			return;
		}
		
		int m = sc.nextInt();
		for(int i = 0; i < m; i++){
			char[] str = sc.next().toCharArray();
			for(int j = 0; j < str.length-1; j++){
				int idx_before = map1.get(str[j]);
				int idx_after = map1.get(str[j+1]);
				
				if(connect.containsKey(idx_before) && connect.get(idx_before) != idx_after){
					System.out.println(-1);
					return;
				}else if(!connect.containsKey(idx_before)){
					connect.put(idx_before, idx_after);
				}
			}
		}
		// System.out.println(Arrays.toString(a));
		// System.out.println(Arrays.toString(b));
		for(int i = 0; i < length; i++){
			int count = 0;
			idx = i;
			boolean flg = false;
			String s = "";
			while(true){
				if(count > length) break;
				if(!connect.containsKey(idx)){
					if(count == length-1){
						s += map2.get(idx);
						flg = true;
						break;
					}else{
						break;
					}
				}
				s += map2.get(idx);
				idx = connect.get(idx);
				count++;
			}
			if(flg){
				System.out.println(s);
				return;
			}
		}
		System.out.println(-1);
	}
}
