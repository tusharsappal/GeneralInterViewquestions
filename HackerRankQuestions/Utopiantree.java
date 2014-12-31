import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Utopiantree {

    public static void main(String args[]) {
        int testCases;

        Scanner s = new Scanner(System.in);
        testCases = s.nextInt();
        if ((testCases >= 1) && (testCases <= 10)) {
            int cycles[] = new int[testCases];

            for (int i = 0; i < testCases; i++) {
                int temp = s.nextInt();
                if ((temp >= 0) && (temp <= 60)) {
                    cycles[i] = temp;
                } else {
                    System.exit(1);
                }
            }

            for (int i = 0; i < testCases; i++) {
                System.out.println(getHeight(cycles[i]));
            }


        } else {
            System.exit(1);
        }
    }


    public static int getHeight(int cycles) {

        int finalHeight = 1;

        for (int i = 1; i <= cycles; i++) {
            if (i % 2 != 0) {
                finalHeight = finalHeight * 2;
            } else {
                finalHeight = finalHeight + 1;
            }
        }

        return finalHeight;
    }
}