/* Nicolas Eldering
Comp Sci 1 M/W 12pm
2/17/2016
Assignment 3 page 185
*/

import java.util.Scanner;
import java.lang.Math;

public class BMIcalculatorNCE
{
	public static void main( String [] args ) {
		double height, weight, BMI;
		Scanner kb = new Scanner(System.in);
		
		System.out.println("In this program I will calculate your BMI.");
		System.out.println("Then I will determine your weight category.");
		
		// output: display instruction | Input: height 
		System.out.print("Please enter your height in inches. > ");
		height = kb.nextDouble();
		System.out.println();
		
		// output: display instruction | Input: weight
		System.out.print("Please enter your weight in pounds. > ");
		weight = kb.nextDouble();
		System.out.println();
		
		// Process: BMI and placing it in BMI variable
		BMI = (weight*703)/(Math.pow(height, 2));
		
		//optimal weight 18.5 - 25
		if ( 18.5 <= BMI <= 25)
			System.out.println("Your BMI is: " + BMI + " Which is an Optimal Weight.");
		
		//underweight <18.5
		else if ( BMI < 18.5 )
			System.out.println("Your BMI is: " + BMI + " Which is Underweight.");
		
		// else weight must be overweight > 25
		else
			System.out.println("Your BMI is: " + BMI + " Which is Overweight.");
		
	}
}
