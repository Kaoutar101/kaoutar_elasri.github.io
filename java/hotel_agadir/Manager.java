package hotel_agadir;
import java.util.Scanner;

public class Manager {
    
    private Room_type new_room;
    public Manager(Room_type new_room){
        this.new_room=new_room;
    }
    public Room_type get_rm(){
        return new_room;
    }
    public void set_rm(Room_type new_room){
        this.new_room=new_room;
    }

    public void hotel_organize(){
    
    Scanner scan=new Scanner(System.in);
    Room constr=new Room();
    
    System.out.println("Do you want to add a new room or to update a room booking information? \n");
    System.out.println("    1)Add a new room to the system");
    System.out.println("    2)Modify book information");
    int choice=scan.nextInt();
    scan.nextLine();
    if(choice==1){
        System.out.println("What's the number of rooms you want to enter the infomation:");
        int x=scan.nextInt();
        scan.nextLine();
       
        for(int i=0; i<x; i++){
        System.out.println("Enter the following information\n");
        System.out.println("room size:\n");
        new_room.room_size=scan.nextLine();
        System.out.println("room number:\n");
        new_room.room_num=scan.nextInt();
        System.out.println("room floor:\n");
        new_room.floor_num=scan.nextInt();
        System.out.println("reservation status:\n");
        new_room.booked=scan.nextBoolean();
        constr.enter_rooms(new_room);
        scan.nextLine();
        }
    }
    else if(choice==2){
        System.out.println("enter room number:");
        CharSequence x=scan.nextLine();
        System.out.println("enter reservation status");
        Boolean y=scan.nextBoolean();
        constr.edit(x,y);
        
    }

    }
    
}
