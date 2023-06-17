package prac04B;

import java.io.*;
import java.rmi.*;

public class ClientConvert {
    public static void main(String[] args) throws Exception {
        InterConvert h1 = (InterConvert) Naming.lookup("WRD");
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        System.out.println("Enter a number:\t");
        String no = br.readLine();

        String ans = h1.convertDigit(no);
        System.out.println("The word representation of the entered digit is: " + ans);
    }
}
