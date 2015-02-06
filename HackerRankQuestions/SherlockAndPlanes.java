import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Scanner;


public class SherlockAndPlanes {

    @SuppressWarnings("unused")
    public static void main (String args[]) throws NumberFormatException, IOException
    {
        // asking users about the number of test cases ,he wishes to execute

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // asking for input
        int testCases = Integer.parseInt(br.readLine());
        if ((testCases>=1)&& (testCases<=10000))

        {

            for (int i=1;i<=testCases;i++)
            {

                int a []  = new int[3];
                int b []  = new int[3];
                int c []  = new int[3];
                int d []  = new int[3];

                // Now asking the user to enter the each point , as  a string and extracting each string to fetch points

                for (int j=1;j<=4;j++)
                {
                    String tempString = br.readLine();

                    if (j==1)
                    {
                        int tempCounter=0;
                        //aString  = tempString.split(" ");
                        for (String st : tempString.split(" "))
                        {
                            if ((Integer.parseInt(st)>=-1000)&& (Integer.parseInt(st)<=1000))
                                a[tempCounter++]= Integer.parseInt(st);
                            else
                                System.exit(1);
                        }

                    }
                    else if (j==2)
                    {
                        int tempCounter=0;
                        //bString = tempString.split(" ");
                        for (String st : tempString.split(" "))
                        {
                            if ((Integer.parseInt(st)>=-1000)&& (Integer.parseInt(st)<=1000))
                                b[tempCounter++]= Integer.parseInt(st);
                            else
                                System.exit(1);
                        }
                    }

                    else if (j==3)
                    {
                        int tempCounter=0;
                        //cString  = tempString.split(" ");
                        for (String st : tempString.split(" "))
                        {
                            if ((Integer.parseInt(st)>=-1000)&& (Integer.parseInt(st)<=1000))
                                c[tempCounter++]= Integer.parseInt(st);
                            else
                                System.exit(1);
                        }

                    }

                    else if (j==4)
                    {
                        //dString = tempString.split(" ");
                        int tempCounter=0;
                        for (String st : tempString.split(" "))
                        {
                            if ((Integer.parseInt(st)>=-1000)&& (Integer.parseInt(st)<=1000))
                                d[tempCounter++]= Integer.parseInt(st);
                            else
                                System.exit(1);
                        }
                    }
                }

                // Now checking for common values in all the integer arrays

                int flagValue =0;

                for (int j=0 ;j<a.length;j++)
                {
                    int aVal = a[j];
                    if ((aVal == b[j])&& (aVal == c[j]) && (aVal == d[j]))
                    {
                        flagValue=1;
                        break;
                    }

                }

                if (flagValue== 1)
                {
                    System.out.println("YES");
                }

                else if (flagValue ==0)
                {
                    System.out.println("NO");
                }

            }


        }
        else
        {
            System.exit(1);
        }

    }
}
