package prac02;

import java.net.*;
import java.io.*;

public class ChatClient {
    public static void main(String[] args) {
        try {
            Socket s = new Socket("Localhost", 8000);
            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
            DataOutputStream out = new DataOutputStream(s.getOutputStream());
            DataInputStream in = new DataInputStream(s.getInputStream());
            BufferedReader br2 = new BufferedReader(new InputStreamReader(in));
            String msg;
            System.out.println("To stop chatting with server type STOP");
            System.out.print("Client Says : ");
            while ((msg = br.readLine()) != null) {
                out.writeBytes(msg + "\n");
                if (msg.equals("STOP")) {
                    break;
                }
                System.out.println("Server Says : " + br2.readLine());
                System.out.print("Client Says : ");
            }

            br.close();
            br2.close();
            in.close();
            out.close();
            s.close();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
