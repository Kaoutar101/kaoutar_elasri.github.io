const fs=require('fs');
const prompt=require('prompt-sync')({sigint: true})
class Room_type{
    constructor(size,number,floor_number,booked){
        this.size=size;
        this.number=number;
        this.floor_number=floor_number;
        this.booked=booked;
    }
}
class Room{
    constructor(){
        this.room=[];
    }

    enter_rooms(room){
        try{
            fs.appendFileSync("room.txt", `floor_num: ${room.floor_number} room_num: ${room.number} room_size: ${room.size} booked: ${room.booked}\n`);
            console.log("room added successfully\n");
        }catch(err){
            console.log("wrong input");
        }
    }

    edit(number,booked){
        try{
            const inputfile=fs.readFileSync("room.txt",utf8);
            let lines=inputfile.split(/\r?\n/);
            lines=lines.map(line=>{
                if(line.includes("room_num: ")&& line.includes(number)){
                    return booked ? line.replace(" booked: false", " booked: true") : line.replace(" booked: true", " booked: false");

                }return line;
            });
            fs.writeFileSync("room.txt",lines.join('\n'));
            console.log("Modification successful");
        }catch(err){
            console.log("An error has occured");
        }
    }

    find_room(){
        try{
            const data=fs.readFileSync("room.txt","utf8");
            const roomtype=prompy("Enter room type: \n");
            const lines=data.split(/\r?\n/);
            let room_found=false;
            let room_number=null;
            for (const line of lines){
                if(line.includes(roomtype)&&line.includes("booked: false")){
                    const parts=line.split("room_num: ");
                    if (parts.length >= 2) {
                        room_number = parseInt(parts[1].split(" ")[0]);
                        console.log("Available room number: " + roomNum);
                        room_found = true;
                        break;
                    }
                }
            }
            if(!room_found){
                console.log("There are no available rooms of type ${roomtype}");

            }else{
                return room_number;
            }
        }catch(err){
            console.log('An error has occured');
        }return null;
    }
}
module.exports=Room;