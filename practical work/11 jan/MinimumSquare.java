import java.util.*;
import java.io.*;

public class Main
{
    
static int getMinSquares(int n)
    {
        if (n <= 3)
            return n;
 
        int res = n; 
 
        for (int x = 1; x <= n; x++) 
        {
            int temp = x * x;
            if (temp > n)
                break;
            else
                res = Math.min(res, 1 + 
                          getMinSquares(n - temp));
        }
        return res;
    }
	public static void main(String[] args) {
	    Scanner sc = new Scanner(System.in);
	    System.out.println("Enter the number:");
	    int num = sc.nextInt();
	    
		System.out.println("Minimum Squares are: " + getMinSquares(num));
	}
}
