import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;
import java.util.Scanner;


public class FindDigits {

    public static void main(String[] args) {
        int number, count;
        Scanner s = new Scanner(System.in);

        number = s.nextInt();

        int[] numb = new int[number];
        for (int i = 0; i < number; ++i)
            numb[i] = s.nextInt();
        for (int i = 0; i < number; ++i) {
            int temp = numb[i];
            count = 0;
            while (temp > 0) {
                int rem = temp % 10;
                temp = temp / 10;
                if (rem != 0) {
                    if (numb[i] % rem == 0)
                        ++count;
                }

            }
            System.out.println(count);

        }


    }
}
