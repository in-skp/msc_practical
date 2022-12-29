package prac01;

import java.net.*;
import java.io.*;

public class tcpServerPrime {
    public static void main(String[] args) {
        try {
            ServerSocket ss = new ServerSocket(8001);
            System.out.println("Server Started................");
            Socket s = ss.accept();

            DataInputStream in = new DataInputStream(s.getInputStream());
            int x = in.readInt();

            DataOutputStream out = new DataOutputStream(s.getOutputStream());
            int y = x / 2;

            if (x == 1 || x == 2 || x == 3) {
                out.writeUTF(x + " is Prime");
                System.exit(0);
            }

            boolean isPrime = true;

            for (int i = 2; i <= y; i++) {
                if (x % i == 0) {
                    out.writeUTF(x + " is not Prime, it is divisible by " + i);
                    isPrime = false;
                    break;
                }
            }

            if (isPrime) {
                out.writeUTF(x + " is Prime");
            }

            ss.close();
        } catch (Exception e) {
            System.out.println(e.toString());
        }
    }
}