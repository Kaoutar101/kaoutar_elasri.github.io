package hotel_agadir;
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Scanner;
class Room_type{
    String room_size;
    int room_num;
    int floor_num;
    boolean booked;
    public Room_type(String room_size,int room_num, int floor_num,boolean booked){
        this.room_size=room_size;
        this.room_num=room_num;
        this.floor_num=floor_num;
        this.booked=booked;
    }
}
public class Room {
    private ArrayList<Room_type> rooms;
    public Room(){
        this.rooms=new ArrayList<Room_type>();
    }

    public void addRoom(Room_type room){
        rooms.add(room);
    }

    public Room_type getroom(int index){
        return rooms.get(index);
    }

    public void setroom(int index,Room_type room){
        rooms.set(index, room);
    }

    public ArrayList<Room_type> getallrooms(){
        return rooms;
    } 

    public void enter_rooms(Room_type room){
        try{
            FileWriter write=new FileWriter("room.txt",true);
            write.write("floor_num: "+room.floor_num+" room_num: "+room.room_num+" room_size: "+room.room_size+" booked: "+room.booked+"\n");
            write.close();
        }catch(IOException e){
            System.out.println("wrong input");
            e.printStackTrace();
        }
        System.out.println("Room added successfully");
    }
    
    public void edit(CharSequence room_num, Boolean booked) {
        try {
            File inputFile = new File("room.txt");
            File tempFile = new File("tempRoom.txt");
    
            Scanner myReader = new Scanner(inputFile);
            FileWriter writer = new FileWriter(tempFile);
    
            while (myReader.hasNextLine()) {
                String line = myReader.nextLine();
                if (line.contains(" room_num: ") && line.contains(room_num)) {
                    if (booked==false) {
                        line = line.replace(" booked: true", " booked: false");
                    } else {
                        line = line.replace(" booked: false", " booked: true");
                    }
                }
                writer.write(line + System.getProperty("line.separator")); // Write the line to the temporary file
            }
            inputFile.delete();
            tempFile.renameTo(inputFile);
            myReader.close();
            writer.close();
            
    
            if (!inputFile.delete()) {
                System.out.println("Could not delete the original file");
                return;
            }
            if (!tempFile.renameTo(inputFile)) {
                System.out.println("Could not rename the temporary file");
                return;
            }
    
            System.out.println("Modification successful");
        } catch (IOException e) {
            System.out.println("An error occurred.");
        }

    }

    public CharSequence find_room() {
        try {
            File fl = new File("room.txt");
            Scanner reader = new Scanner(fl);
            Scanner scan=new Scanner(System.in);
            String rm_tp=scan.next();
            boolean roomFound = false; 
            CharSequence y=null;
            while (reader.hasNextLine()) {
                final String line = reader.nextLine();
                if (line.contains(rm_tp)&&line.contains(" booked: false")) {
                    String[] parts = line.split(" room_num: ");
                    if (parts.length >= 2) {
                        String roomNumStr = parts[1].split(" ")[0];
                        int roomNum = Integer.parseInt(roomNumStr);
                        System.out.println("Available room number: " + roomNum);
                        roomFound = true; 
                        y=String.valueOf(roomNum);
                        
                    }
                    break ;
                }
            }   
            reader.close();
            
                if (!roomFound) {
                System.out.println("No available rooms of type " + rm_tp);
                CharSequence x="no room number";
                return x;
            }
            else if(roomFound){
                return y;
            }
            
            
        } catch (IOException e) {
            System.out.println("An error occurred: " + e.getMessage());
        }
        return null;
    }
    
    
}

