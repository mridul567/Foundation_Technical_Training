/******************************************************************************

                            Online Java Compiler.
                Code, Compile, Run and Debug java program online.
Write your code in this editor and press "Run" button to execute it.

*******************************************************************************/

import java.util.*;
import java.io.*;

public class Divisible7
{
    
static boolean isDivisibleBy7(int n)
    {
        if( n < 0 )
            return isDivisibleBy7( -n );
  
        if( n == 0 || n == 7 )
            return true;
        if( n < 10 )
            return false;
  
        return isDivisibleBy7( n / 10 - 2 * ( n - n / 10 * 10 ) );
    }
	public static void main(String[] args) {
	    Scanner sc = new Scanner(System.in);
	    System.out.println("Enter the number:");
	    int num = sc.nextInt();
	    
		if(isDivisibleBy7(num))
            System.out.println("Divisible");
        else
            System.out.println("Not Divisible");
	}
}

