package prac04A;

import java.rmi.*;

public class ClientDate {
    public static void main(String[] args) throws Exception {
        String s1;
        InterDate h1 = (InterDate) Naming.lookup("RMI2");
        s1 = h1.display();
        System.out.println(s1);
    }
}
