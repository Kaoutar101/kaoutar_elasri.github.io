package hotel_agadir;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Scanner;
public class Client extends Profile {
    
    public Client(String fname, String lname, int age, String email_adress, String adress_info) {
        super(fname, lname, age, email_adress, adress_info);
    }
    
    public void personal_info(String fname,String lname,int age,String email_address, String address_info,CharSequence room_num){
        try{
            FileWriter var=new FileWriter("client_info.txt",true);
            var.write("first_name: "+fname+" last_name: "+lname+" age: "+age+" email_address: "+email_address+" address_information: "+address_info+" room_num: "+room_num+"\n");
            var.close();
        }catch(IOException e){
            System.out.println("An Error has Occured\n");
        }

    }

    public CharSequence make_resevation(){
        Scanner scan=new Scanner(System.in);
        Room mk_rsv=new Room();
        System.out.println("Choose the type of the room you want to book:\n");
        System.out.println("         1)Single\n         2)Double\n         3)Suite");
        CharSequence room_num=mk_rsv.find_room();
        return room_num;
        
    }
    
}

