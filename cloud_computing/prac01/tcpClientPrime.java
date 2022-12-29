package prac01;

import java.net.*;
import java.io.*;

public class tcpClientPrime {
    public static void main(String[] args) {
        try {
            Socket cs = new Socket("127.0.0.1", 8001);
            System.out.print("Enter the number:");
            BufferedReader infu = new BufferedReader(new InputStreamReader(System.in));

            int a = Integer.parseInt(infu.readLine());
            DataOutputStream out = new DataOutputStream(cs.getOutputStream());
            out.writeInt(a);

            DataInputStream in = new DataInputStream(cs.getInputStream());
            System.out.println(in.readUTF());
            cs.close();

        } catch (Exception e) {
            System.out.println(e.toString());
        }
    }
}
