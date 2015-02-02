import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Hashtable;
import java.util.Map.Entry;
import java.util.Scanner;


public class IceCreamParlor {

    public static void main(String args []) throws NumberFormatException, IOException

    {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // Taking the note of the number of the test cases

        int testCases = Integer.parseInt(br.readLine());
        String [] resultArray = new String [testCases];
        for (int i=0;i<=testCases-1;i++)
        {
            int sumExpected = Integer.parseInt(br.readLine());
            int lengthOfArray = Integer.parseInt(br.readLine());
            int [] arrayOfNumbers = new int[lengthOfArray];

            int tempCounter =0;
            String tempString = br.readLine();

            for (String st : tempString.split(" "))
            {
                arrayOfNumbers[tempCounter++]= Integer.parseInt(st);
            }

            // Now storing the values in the hashmap

            Hashtable<Integer, Integer> hashTab = new Hashtable<Integer, Integer>();

            for (int j=0 ;j<arrayOfNumbers.length;j++)
            {
                hashTab.put(arrayOfNumbers[j], j);

            }

            // Now determining the index values
            int index1=0;
            int index2=0;

            for (Entry<Integer, Integer> entry : hashTab.entrySet())
            {
                int diff = sumExpected-entry.getKey();

                if (hashTab.containsKey(diff))
                {
                    index1=entry.getValue()+1;
                    index2= hashTab.get(diff)+1;
                    break;
                }
            }


            // The indices values may be in any random fashion so arranging them in ascending order

            int temp = 0;
            if (index1>=index2)
            {
                temp =index2;
                index2 = index1;
                index1= temp;
            }
            else if (index2 > index1)
            {
                temp= index1;
                index1 = index2;
                index2 = temp;
            }

            resultArray[i] = index1 + " " + index2;

        }


        for (String s : resultArray)
        {
            System.out.println(s);
        }

    }

}
