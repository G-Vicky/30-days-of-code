import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int N = scan.nextInt();
        while(N > 0) {
            String str = scan.next();
            StringBuilder evenStr = new StringBuilder();
            StringBuilder oddStr = new StringBuilder();
            for (int i = 0; i < str.length(); i++) {
                if (i % 2 == 0) {
                    evenStr.append(str.charAt(i));
                } else {
                    oddStr.append(str.charAt(i));
                }
            }
            System.out.println(evenStr + " " + oddStr);
            N--;
        }
    }
}
