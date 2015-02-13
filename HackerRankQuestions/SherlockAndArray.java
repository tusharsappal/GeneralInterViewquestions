import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;


public class SherlockAndArray {
    public static void main (String args[]) throws NumberFormatException, IOException
    {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int testCases = Integer.parseInt(br.readLine());
        if (testCases>=1 && testCases<=10)
        {


            String [] resultArray  = new String [testCases];

            for (int i =0; i< testCases;i++)
            {

                int numberOfEntries = Integer.parseInt(br.readLine());
                if (numberOfEntries>=1 && numberOfEntries<=100000)
                {
                    int [] entryArray = new int[numberOfEntries];
                    String values = br.readLine();
                    //values = values.replaceAll("\\s+", "");
                    String [] tempCharArray = values.split("\\s+");
                    int counter=0;

                    for (String c : tempCharArray)
                    {
                        if (Integer.parseInt(c)>=1 && Integer.parseInt(c)<=20000)
                        {
                            entryArray[counter++]= Integer.parseInt(c);
                        }
                        else
                        {
                            System.exit(1);

                        }
                    }
                    // Now we have an array we can find the equilibrium index

                    resultArray[i] = equilibrium(entryArray, entryArray.length);
                }
                else
                {
                    System.exit(1);
                }
            }

            // Now printing the Output Array

            for (String s : resultArray)
            {
                System.out.println(s);
            }
        }
        else
        {
            System.exit(1);
        }
    }


    public static String equilibrium (int [] arr, int arr_size)
    {
        int sum=0;
        int leftSum =0;
        int i;
        boolean isEqui = false;
        //Finding the sum of all the elements by iterating the array

        for (i=0;i<arr_size;i++)
        {

            sum = sum + arr [i];
        }

        // Now we have the sum we subtract , we iterate through the array deducting the current value of array index
        // Will check that the sum == leftsum if so we will return the index and
        // if not we will add the index value to the left sum

        for (i =0 ; i<arr_size;i++)
        {
            sum = sum-arr[i];

            if (sum==leftSum)
            {
                isEqui=true;
                break;

            }
            leftSum= leftSum+arr[i];
        }

        if (isEqui == true)
            return "YES";
        else
            return "NO";
    }


}
