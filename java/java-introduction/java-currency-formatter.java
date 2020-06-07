import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {
    
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        double payment = scanner.nextDouble();
        scanner.close();

        Locale locale = new Locale("en", "IN");
        NumberFormat UScurrencyFormatter = NumberFormat.getCurrencyInstance(Locale.US);
        String us = UScurrencyFormatter.format(payment);
        NumberFormat INcurrencyFormatter = NumberFormat.getCurrencyInstance(locale);
        String india = INcurrencyFormatter.format(payment);
        NumberFormat CHINAcurrencyFormatter = NumberFormat.getCurrencyInstance(Locale.CHINA);
        String china = CHINAcurrencyFormatter.format(payment);
        NumberFormat FRcurrencyFormatter = NumberFormat.getCurrencyInstance(locale.FRANCE);
        String france = FRcurrencyFormatter.format(payment);   
        
         System.out.println("US: " + us);
        System.out.println("India: " + india);
        System.out.println("China: " + china);
        System.out.println("France: " + france);
    }
}


