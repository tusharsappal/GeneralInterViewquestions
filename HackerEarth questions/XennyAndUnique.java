import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;


public class XennyAndUnique {

    public static void main(String args[])
    {
        Scanner s = new Scanner(System.in);
        // Defining the number of inputs to be taken
        int numOfInputs = s.nextInt();

        if (numOfInputs>1000)
        {
            System.exit(1);
        }

        else
        {
            // Now putting the values received in the Hash Map

            HashMap<String, Integer> hMap = new HashMap<String, Integer>();

            for (int i =1;i<=numOfInputs;i++)
            {

                String tempString = s.next();
                if (tempString.length()>1000)
                {
                    System.exit(1);
                }
                else

                {


                    if(!(hMap.containsKey(tempString)))
                    {
                        hMap.put(tempString,1);
                    }

                    else if (hMap.containsKey(tempString))
                    {
                        int inValue=  hMap.get(tempString);
                        inValue++;
                        hMap.put(tempString, inValue);
                    }
                }

            }

            System.out.println(hMap.size());
        }
    }

}
