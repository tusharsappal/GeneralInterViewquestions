import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class CutTheStick {
    public static void main (String args[]) throws IOException
    {
        // Taking input the number of the sticks from the user
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int numberOfSticks = Integer.parseInt(br.readLine());
        if (numberOfSticks>=1 && numberOfSticks<=1000)
        {
            int [] sticks = new int[numberOfSticks];
            String stickLen = br.readLine();
            String sticksStringArray [] = stickLen.split("\\s+");
            int counter=0;
            for (String str : sticksStringArray)
            {
                if (Integer.parseInt(str)>=1 && Integer.parseInt(str)<=1000)
                {
                    sticks[counter++] = Integer.parseInt(str);
                }
                else
                {
                    System.exit(1);
                }

            }

            // Now we have the array , we will sort the array using Insertion Sort
            for (int j =1;j<sticks.length;j++)
            {

                int key = sticks[j];
                int i = j-1;
                while ( (i > -1) && ( sticks [i] > key ) ) {
                    sticks [i+1] = sticks[i];
                    i--;
                }
                sticks[i+1] = key;

            }

            for (int i =0; i<sticks.length;i++)
            {
                if (sticks[i]==0)
                    continue;
                int count=0;
                int temp=sticks[i];
                for (int j=i;j<sticks.length;j++)
                {
                    if (sticks[j]==0)
                    {
                        continue;
                    }
                    else
                    {
                        sticks[j]= sticks[j]-temp;
                        count++;
                    }

                }
                System.out.println(count);
            }

        }
        else
        {
            System.exit(1);
        }
    }

}
