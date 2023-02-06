package prac04B;

import java.rmi.*;
import java.rmi.server.*;

public class ServerConvert extends UnicastRemoteObject implements InterConvert {

    protected ServerConvert() throws Exception {
    }

    public String convertDigit(String no) throws Exception {
        String str = "";
        for (int i = 0; i < no.length(); i++) {
            int p = no.charAt(i);
            switch (p) {
                case 48:
                    str += "zero ";
                    break;
                case 49:
                    str += "one ";
                    break;
                case 50:
                    str += "two ";
                    break;
                case 51:
                    str += "three ";
                    break;
                case 52:
                    str += "four ";
                    break;
                case 53:
                    str += "five ";
                    break;
                case 54:
                    str += "six ";
                    break;
                case 55:
                    str += "seven ";
                    break;
                case 56:
                    str += "eight ";
                    break;
                case 57:
                    str += "nine ";
                    break;
                default:
                    str += "infinity ";
                    break;
            }
        }
        return str;
    }

    public static void main(String[] args) throws Exception {
        ServerConvert s1 = new ServerConvert();
        Naming.bind("WRD", s1);
        System.out.println("Object registered...");
    }

}
