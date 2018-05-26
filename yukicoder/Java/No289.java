import java.util.Scanner;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class No289{
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);
		String numstr = sc.next();
		String[] ns = numstr.split("");
			
		int sum_ = 0;
		for(int i=0; i<ns.length; i++){
			Pattern p = Pattern.compile("^[0-9]+$");
			Matcher m = p.matcher(ns[i]);
			if(m.find()){
				sum_ += Integer.parseInt(ns[i]);
			}
		}
		System.out.println(sum_);
	}
}
