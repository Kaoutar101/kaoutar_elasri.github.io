package hotel_agadir;
//import java.io.BufferedReader;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileWriter;
import java.io.FileReader;
import java.io.IOException;
import java.util.Scanner;

public class Account {
    private String emailadress;
    private String password;
    
    public Account(String emailadress, String password){
        this.emailadress=emailadress;
        this.password=password;
    }

    public String get_email(){
        return emailadress;
    }
    public void set_email(String emailadress){
        this.emailadress=emailadress;
    }

    public String get_password(){
        return password;
    }
    public void set_password(String password){
        this.password=password;
    }

    public void create_account(String password, String emailadress){
        try{
            FileWriter write=new FileWriter("data.txt",true);
            write.write("email: "+emailadress+" password: "+password+"\n");
            write.close();
        }catch(IOException e){
            System.out.println("wrong input");
            e.printStackTrace();
        }
        System.out.println("account created successfully");
    }

    public boolean login(String emailAddress, String password) {
        try {
            File myObj = new File("data.txt");
            Scanner myReader = new Scanner(myObj);
            boolean found_email = false; 
            boolean found_password = false; 
    
            while (myReader.hasNextLine()) {
                String line = myReader.nextLine();
                if (line.contains("email:") && line.contains(emailAddress)) {
                    found_email = true;
                    break;
                }
            }
            myReader.close(); 
    
            myReader = new Scanner(myObj); 
    
            while (myReader.hasNextLine()) {
                String line = myReader.nextLine();
                if (line.contains("password:") && line.contains(password)) {
                    found_password = true;
                    break;
                }
            }
            myReader.close(); 

            if (found_email && found_password) {
                return true;
            } else {
                return false;
            }
    
        } catch (FileNotFoundException e) {
            System.out.println("An error occurred.");
            e.printStackTrace();
            return false; 
        }
    }
    
    public boolean manager_login(String emailAddress, String password) {
        
        if (emailAddress.equals("manager@gmail.com")&&password.equals("manager2024")){
            return true;
        }
        else {
            return false;
        }
        
    }
}

