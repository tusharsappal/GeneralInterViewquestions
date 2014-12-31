import java.awt.font.NumericShaper;
import java.util.Scanner;


public class IndexLocator {
    public static void main (String args[])
    {

        System.out.println(findIndex());
    }


    public static int findIndex ()
    {
        Scanner s=new Scanner(System.in);
        int valueToBeSearched = Integer.parseInt(s.nextLine());
        int sizeOfArray = Integer.parseInt(s.nextLine());
        String numberString = s.nextLine();
        String[] numberStringArray = numberString.split("\\s+");

        int spaces= countSpaces(numberString);

        int [] ar =  new int[sizeOfArray];
        int mid = 0 ;

        if((sizeOfArray>=1)&&(sizeOfArray<=1000)&& (spaces+1 == sizeOfArray))
        {



            int start = 0;
            int end = sizeOfArray-1;

            // Populating the int array with the last line of string numbers , obviously converting them into integers first

            int tempIndex=0;
            for (String str : numberStringArray)
            {
                ar[tempIndex++]= Integer.parseInt(str);
            }


            // finding the element using the Binary Search Algorithm  Technique since the elements are arranged
            // in a particular order



            while ( start<=end )
            {
                mid= (int) (start+end)/2;

                if (ar[mid]== valueToBeSearched)
                    return mid;
                else if (ar[mid]< valueToBeSearched)
                    start = mid+1;
                else if (ar[mid] > valueToBeSearched)
                    end = mid-1;

            }


        }

        else
        {
            System.exit(1);
        }
        return mid;


    }

    public static int countSpaces (String sampleString)
    {
        int spaces=0;
        for(int i=0;i<sampleString.length()-1;i++)
        {
            if(sampleString.charAt(i)==' ')
            {
                spaces= spaces+1;
            }
        }
        return spaces;
    }

}
