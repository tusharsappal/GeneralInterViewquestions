import java.util.Scanner;

public class LoveLetterMystery {
    public static void main(String args[]) {
        int t, i;
        Scanner s = new Scanner(System.in);
        t = s.nextInt();
        String[] strArray = new String[t];

        for (int j = 0; j < t; j++) {
            strArray[j] = s.next();
        }


        for (int j = 0; j < t; j++) {

            int steps = 0;
            for (i = 0; i < strArray[j].length() / 2; i++) {
                steps += Math.abs(strArray[j].charAt(i) - strArray[j].charAt(strArray[j].length() - i - 1));
            }
            System.out.println(steps);

        }

    }
}