import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;


public class PlusMinus 
{
    @SuppressWarnings("null")
    public static void main(String args[]) throws NumberFormatException, IOException 
    {
        int sizeOfArray = 0;
        int iterator = 0;
        float positiveCount = 0.0f;
        float negativeCount = 0.0f;
        float zeroCount = 0.0f;

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        // Taking input the number of the testCases

        sizeOfArray = Integer.parseInt(br.readLine());
        int[] itemsToOperate = new int[sizeOfArray];

        if (sizeOfArray > 100 && sizeOfArray < 1) 
        {
            System.exit(1);
        } 
        else 
        {
            String [] splitted = br.readLine().split("\\s+");

            for (String str : splitted)
            {
                itemsToOperate[iterator] = Integer.parseInt(str);
                if (itemsToOperate[iterator] > 0)
                {
                    positiveCount++;
                }
                else if (itemsToOperate[iterator] < 0)
                {
                    negativeCount++;
                }
                else if (itemsToOperate[iterator] == 0)
                {
                    zeroCount++;
                }
            }
            
            
            String positivePercent = String.format("%.3f",(positiveCount / sizeOfArray));
            String negativePercent = String.format("%.3f", (negativeCount / sizeOfArray));
            String zeroPercent = String.format("%.3f", (zeroCount / sizeOfArray));
            
            System.out.println(positivePercent);
            System.out.println(negativePercent);
            System.out.println(zeroPercent);
            
            

        }
    }
}    