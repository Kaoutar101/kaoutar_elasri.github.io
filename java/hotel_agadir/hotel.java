package hotel_agadir;
import java.util.Scanner;
public class hotel{
public static void main(String[] args){
    Scanner scan=new Scanner(System.in);
    
    String email=null;
    String password=null;
    Account acc=new Account(email, password);


    System.out.println("Welcome to Hotel Agadir\n");// Written in a movement motion than it disappears to check boxes
    System.out.println("Are you a Manager (1) or a client(2)\n"); //check box to choose
    int ans=scan.nextInt();
    scan.nextLine();

    if (ans==1){
        Boolean accnt=false;
        int i=0;
        //shows two boxes to write the email adress and password
        while(!accnt && i <3){
        System.out.println("enter your credentials");
        System.out.println("email adress:\n");
        email=scan.nextLine();
        System.out.println("password: \n");
        password=scan.nextLine();
        accnt=acc.manager_login(email, password);

        if(accnt){
            i=3;
        }
        else{
            System.out.println("Wrong Credentials!\nTry again");
            i++;
        }
    }
    String again="yes";
    while(again.equals("yes")){
        if(accnt){
            //shows the box to write the room number with a loop next to it
            Room_type x=new Room_type(null, 0, 0, false);
            Manager test=new Manager(x);
            test.hotel_organize();
            System.out.println("Do you want to add another room's information or edit the reservation of an existing one?\n");
            System.out.println("yes/no\n");
            again=scan.nextLine();
        }
    }
    }




    else if(ans==2){

        //shows two boxes to click on to login or create account
    System.out.println("Welcome to Hotel Agadir, to browse our menu you can choose one of the following options:\n");
    System.out.println("    1)Login");
    System.out.println("    2)Create an account");
    
    int account_choice=scan.nextInt();
    scan.nextLine();

    
    System.out.println("enter your credentials");
    System.out.println("email adress:\n");
    email=scan.nextLine();
    System.out.println("password: \n");
    password=scan.nextLine();
    Boolean created=false;
    Boolean answ=false;

    if(account_choice==2){
    acc.create_account(password, email);
    created=true;
    }
    
    else if(account_choice==1){
    int i=0;
    while(i<3){
    answ=acc.login(password, email);
        if (answ) {
            System.out.println("Logged in successfully");
            i=3;
        } else {
            System.out.println("Login failed. Please check your credentials.");
            i++;
        }
    }}
    if(answ || created==true){
        Room rm=new Room();
        System.out.println("Enter the following information about yourself:\n");
        System.out.println("First name:\n");
        String fname=scan.nextLine();
        System.out.println("Last name:\n");
        String lname=scan.nextLine();
        System.out.println("Age:\n");
        int age=scan.nextInt();
        scan.nextLine();
        System.out.println("email adress:\n");
        String email_address=scan.nextLine();
        System.out.println("adress_info:\n");
        String address_info=scan.nextLine();
        Client cl=new Client(fname,lname,age,email_address, address_info);
        CharSequence f=cl.make_resevation();
        
        scan.close();

        if (f != null && !f.equals("no room number") ) {
            rm.edit(f,true);
            cl.personal_info(fname, lname, age, email_address, address_info, f);
        }
    
    }
}
    }

}