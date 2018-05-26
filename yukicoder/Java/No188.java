public class No188{
	public static void main(String[] args){
		
		int happyday = 0;
		for(int m=1; m<=12; m++){
			for(int d=1; d<=30; d++){
				int d1 = d/10;
				int d0 = d%10;
				if(m == d1+d0){
					happyday++;
					// System.out.println(m + "/" + d);
				}
			}
		}
		System.out.println(happyday);
	}
}
