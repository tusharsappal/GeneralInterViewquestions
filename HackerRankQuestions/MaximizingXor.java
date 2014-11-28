import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {


    static int maxXor(int l, int r) {
        if(((l<1)&&(l>1000))||((r<1)&&(r>1000)))
            System.exit(1);
        int max=0;
        int result=0;

        for(int i=l; i<=r ; i++)
        {
            for(int j=l; j<=r; j++)
            {
                result= i ^ j;

                if(result> max)
                {
                    max= result;
                }
            }

        }
        return (max);


    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int res;
        int _l;
        _l = Integer.parseInt(in.nextLine());

        int _r;
        _r = Integer.parseInt(in.nextLine());

        res = maxXor(_l, _r);
        System.out.println(res);

    }
}
