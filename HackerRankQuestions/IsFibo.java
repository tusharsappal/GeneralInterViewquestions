import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class isFibo {

    /*For finding if a number is fibonacci or not
    I have followed the following approach
    Given a number 'n', how to check if n is a Fibonacci number.

    A simple way is to generate Fibonacci numbers until the generated number is greater than or equal to ‘n’.
    Following is an interesting property about Fibonacci numbers that can also be used to check if a given number is Fibonacci or not.
    A number is Fibonacci if and only if one or both of (5*n2 + 4) or (5*n2 – 4) is a perfect square (Source: Wiki).
    
      */
    public static void main (String args[])
    {
        int testCases;

        Scanner s=new Scanner(System.in);
        testCases= s.nextInt();
        if((testCases>=1)&&(testCases<=100000))
        {
            // Creating an array to store the integers
            long [] numbers= new long[testCases];
            for(int i=0;i<testCases;i++)
            {
                long temp = s.nextLong();
                if((temp>=1)&&(temp<=Math.pow(10, 10)))
                    numbers[i]= temp;

            }


            for(int i=0;i<testCases;i++)
            {
                boolean res = isFibbonaci(numbers[i]);
                if(res==true)
                    System.out.println("IsFibo");
                else
                    System.out.println("IsNotFibo");

            }

        }
        else
        {
            System.exit(1);
        }

    }


    public static boolean isFibbonaci(long n)
    {
        return isPerfectSquare(5*n*n + 4) ||
                isPerfectSquare(5*n*n - 4);

    }


    private static boolean isPerfectSquare(long x) {
        long s = (long) Math.sqrt(x);
        return (s*s == x);
    }

}