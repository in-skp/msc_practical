package prac01B;

import java.net.*;
import java.io.*;

public class ChatServer {
    public static void main(String[] args) {
        try {
            ServerSocket ss = new ServerSocket(8000);
            System.out.println("Waiting for client to connect..");
            Socket s = ss.accept();
            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
            DataOutputStream out = new DataOutputStream(s.getOutputStream());
            DataInputStream in = new DataInputStream(s.getInputStream());
            BufferedReader br2 = new BufferedReader(new InputStreamReader(in));
            String receive, send;
            while ((receive = br2.readLine()) != null) {
                if (receive.equals("STOP")) {
                    break;
                }
                System.out.println("Client Says : " + receive);
                System.out.print("Server Says : ");
                send = br.readLine();
                out.writeBytes(send + "\n");
            }

            br.close();
            br2.close();
            in.close();
            out.close();
            s.close();
            ss.close();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
