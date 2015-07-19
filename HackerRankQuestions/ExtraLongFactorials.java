import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.math.BigInteger;

public class ExtraLongFactorials
{
	public static void main (String args []) throws NumberFormatException, IOException
	{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		// Taking input the number as input of which the factorial is to be calculated 

		int numberToBeOperatedOn = Integer.parseInt(br.readLine());

		if ((numberToBeOperatedOn <1) && (numberToBeOperatedOn > 100))
		{
			System.exit(1);
		}
		else
		{
			BigInteger fact = new CalculateFactorial().factorial(new BigInteger(String.valueOf(numberToBeOperatedOn)));
            System.out.println(fact);
		}
	}

}

class CalculateFactorial 
{
	public BigInteger factorial (BigInteger bigNum)
	{
		if ((bigNum.compareTo(BigInteger.ONE) == 0) || ( bigNum.compareTo(BigInteger.ZERO)== 0))
		{
			return BigInteger.ONE;
		}

		else 
		{
			BigInteger result = bigNum.multiply(factorial(bigNum.subtract(new BigInteger("1"))));
			return result;
		}
	}

}
