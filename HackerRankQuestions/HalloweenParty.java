import java.util.Scanner;


public class HalloweenParty {
    public static void main (String args[])
    {
        Scanner s = new Scanner(System.in);
        // Taking input the number of the test Cases
        int testCases = s.nextInt();
        if ((testCases>=1) && (testCases<=10))
        {

            String [] outputArray = new String[testCases];
            for (int i=0;i<testCases;i++)
            {
                long horizontalLines =0;
                long verticalLines = 0;
                long inputNumber = s.nextLong();
                if (inputNumber>=2&&inputNumber<=10000000)
                {
                    // Checking that the number entered is even or odd
                    // if it is odd , calulating the quotient and the remainder values
                    // If it is even , then calculating the remainder and using the remainder values

                    if (inputNumber%2==0)
                    {
                        horizontalLines = inputNumber /2;
                        verticalLines = inputNumber/2;
                    }
                    else if (inputNumber%2!=0)
                    {

                        verticalLines =  inputNumber/2;
                        horizontalLines = inputNumber-verticalLines;
                    }

                    outputArray[i]= String.valueOf(horizontalLines*verticalLines);
                }
                else
                {
                    System.exit(1);
                }
            }

            // Iterating over the output array values
            for (String value : outputArray)
            {
                System.out.println(value);
            }

        }
        else
        {
            System.exit(1);
        }

    }


}
