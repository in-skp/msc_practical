// A RMI based application program to display current date and time.
package prac04A;

import java.rmi.*;

public interface InterDate extends Remote {
    public String display() throws Exception;
}
