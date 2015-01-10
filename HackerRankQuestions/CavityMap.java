import java.util.Scanner;


public class CavityMap {
    @SuppressWarnings("resource")
    public static void main (String args[])
    {
        int dimensions;
        Scanner s=new Scanner(System.in);
        dimensions= s.nextInt();
        if(dimensions>=1 && dimensions<=100)
        {
            int [][] a= new int[dimensions][dimensions];

            // taking the input from the user and then printing it to make sure we have a two dimensional array

            for(int i=0;i<dimensions;i++)
            {
                String stringInput= s.next();

                for(int j=0;j<dimensions;j++)
                {
                    int temp =  Character.getNumericValue(stringInput.charAt(j));
                    a[i][j]= temp;
                }

            }


            // Now printing the array in 2-D format

            for(int i=0;i<dimensions;i++)
            {

                for(int j=0;j<dimensions;j++)

                {
                    if((i==0)||(i==dimensions-1)||(j==0)||(j==dimensions-1))
                    {
                        System.out.print(a[i][j]);
                        continue;
                    }

                    else
                    {

                        if ((a[i][j]>a[i-1][j])&&(a[i][j]>a[i+1][j])&&(a[i][j]>a[i][j-1])&&(a[i][j]>a[i][j+1]))
                        {
                            System.out.print('X');
                        }
                        else
                        {
                            System.out.print(a[i][j]);
                        }
                    }

                }

                System.out.print("\n");

            }
        }
        else
        {
            System.exit(1);
        }

    }

}
