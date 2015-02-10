import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class SherlockAndSquares {
    public static void main (String args[]) throws NumberFormatException, IOException
    {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // Taking input the number of testCases that we need to handle
        int testCases = Integer.parseInt(br.readLine());
        if ((testCases>=1)&&(testCases<=100))
        {  int [] outputArray  = new int[testCases];
            for (int i =0 ; i< testCases; i++)
            {

                String [] splitted = br.readLine().split("\\s+");
                int lowerLimit = Integer.parseInt(splitted[0]);
                int upperLimit = Integer.parseInt(splitted[1]);
                if ((lowerLimit>=1)&&(upperLimit>=1)&&(lowerLimit<=upperLimit)&&(upperLimit<=1000000000))
                {

                    outputArray[i]=(((int)Math.sqrt(upperLimit)-(int)Math.sqrt(lowerLimit)));
                    if (isPerfectSquare(lowerLimit))
                    {
                        outputArray[i]= outputArray[i]+1;
                    }
                }
                else {
                    System.exit(1);
                }

            }

            for (int val : outputArray)
            {
                System.out.println(val);
            }
        }
        else
        {
            System.exit(1);
        }
    }

    public static boolean isPerfectSquare (int lowerLimit)
    {
        if (lowerLimit < 0)
            return false;

        switch((int)(lowerLimit & 0xF))
        {
            case 0: case 1: case 4: case 9:
            long tst = (long)Math.sqrt(lowerLimit);
            return tst*tst == lowerLimit;

            default:
                return false;
        }
    }

}
