import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class ClosestNumbers {

    public static void main(String[] args) {
        /*
        first find the minimum difference present and  now print only those pairs
        which satisfy the criteria

        */

        Scanner s = new Scanner(System.in);

        int n = s.nextInt();
        if ((n < 2) && (n > 200000))
            System.exit(1);
        else {

            int[] a = new int[n];

            for (int i = 0; i < n; i++) {
                int temp = s.nextInt();

                if ((temp < -10000000) && (temp > 10000000)) {
                    System.exit(1);
                } else {

                    a[i] = temp;
                }
            }


            // Now arranging the array in the ascending order


            int len = a.length;
            for (int j = 1; j < len; j++) {
                int key = a[j];
                int i = j - 1;
                while ((i > -1) && (a[i] > key)) {
                    a[i + 1] = a[i];
                    i--;
                }
                a[i + 1] = key;

            }


            int minDiff = Math.abs(a[0] - a[(a.length) - 1]);
            for (int i = 0; i < (a.length) - 1; i++) {
                int diff = Math.abs(a[i] - a[i + 1]);
                if (diff < minDiff) {
                    minDiff = diff;
                }
            }

            System.out.println("The minimum Difference is " + minDiff);


            for (int i = 0; i < (a.length - 1); i++) {
                int diff = Math.abs(a[i] - a[i + 1]);
                if (diff == minDiff) {
                    System.out.print(a[i]);
                    System.out.print(" ");
                    System.out.print(a[i + 1]);
                    System.out.print(" ");
                }

            }

        }

    }


}


