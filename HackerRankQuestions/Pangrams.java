import java.util.Scanner;


public class Pangrams {
    public static void main(String args[])
    {
        Scanner s = new Scanner(System.in);
        String stringToPlay = s.nextLine();

        if((stringToPlay.length()>=1)&&(stringToPlay.length()<=1000))
        {

            // first remove all the white spaces
            // Then convert the string into lower case
            stringToPlay = stringToPlay.replaceAll("\\s+","").toLowerCase();
            if(isPangram(stringToPlay))
                System.out.println("pangram");
            else
                System.out.println("not pangram");
        }

        else
        {

            System.exit(1);

        }

    }

    public static boolean isPangram(String str)
    {

        // removing the duplicates and then checking that the length of the string is 26 so we call it as pangram
        if(str.replaceAll("(.)(?=.*\\1)", "").length()==26)
            return true;
        else
            return false;

    }

}
