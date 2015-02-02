
import  java.util.*;
public class PalindromeIndex {
    public static void main (String args[])

    {
        String inputString;
        Scanner s = new Scanner(System.in);

        //System.out.println("Input a string");

        // Taking input the number of the test cases
        int testCases = s.nextInt();

        if((testCases<1)&& (testCases>20))
        {
            System.exit(1);

        }

        else

        {

            // Creating the String Array and storing the test cases

            String strArray [] = new String [testCases];

            // Now storing the individual string values in the string array

            for (int i=0;i<testCases;i++)


            {
                strArray[i]= s.next();

            }


            // Now checking the individual element length that it does not exceed


            for (int i=0;i<testCases;i++)
            {
                int strlength =strArray[i].length();

                if((strlength<1)&&(strlength>100005))
                {
                    System.exit(1);
                }

            }


            // Now sending the individual values for evaluation


            for (int i=0;i<testCases;i++)
            {
                System.out.println(returnPalindromeIndex(strArray[i]));
            }
        }


    }

    public static int returnPalindromeIndex(String inputString)
    {

        int length  = inputString.length();
        int i, begin, end, middle;
        int returnValue=-1;

        begin  = 0;
        end    = length - 1;
        middle = (begin + end)/2;

        for (i = begin; i <= middle; i++) {
            if (inputString.charAt(begin) == inputString.charAt(end)) {
                begin++;
                end--;
            }
            else {
                returnValue =begin;
                break;
            }
        }
        if (i == middle + 1) {
            returnValue= -1;
        }

        return returnValue;
    }
}
