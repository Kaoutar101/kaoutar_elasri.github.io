const fs=require('fs');
const Room=require('./Room');
const prompt=require('prompt-sync')({sigint: true})
class Manager{
    constructor(new_room){
        this.new_room=new_room;
    }
    hotel_organize(){
        const room=new Room();
        let new_room={size:'null',number:0,floor_number:0, booking_status:false};
        console.log("Do you want to add a new room or to update a room booking information? \n");
        let choice=prompt("1)Add a new room to the system 2)Modify book information\n");

        if(choice===1){
            let x=prompt("What's the number of rooms you want to enter the infomation:\n");
            for(let i=0;i<x;i++){
                console.log("Enter the following information\n");
                new_room.size=prompt("room size:\n");
                new_room.number=prompt("room number:\n");
                new_room.floor_number=prompt("floor number:\n");
                new_room.booked=prompt('reservation status:\n');
                room.enter_rooms(new_room);
            }
        }
        else if(choice===2){
            let x=prompt("Enter room number: ");
            let y=prompt("Enter reservation status: ");
            room.edit(x,y);
        }
    }
}
module.exports=Manager;