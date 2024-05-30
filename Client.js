const fs=require('fs');
const Room=require('./Room');
const prompt=require('prompt-sync')({sigint: true})
class Client{
    constructor(fname, lname, age, email,adress_info){
        this.fname=fname;
        this.lname=lname;
        this.age=age;
        this.email=email;
        this.adress_info=adress_info;
    }
    personal_info(fname, lname, age, email,adress_info){
        try{
            fs.appendFileSync("first_name: "+fname+" last_name: "+lname+" age: "+age+" email_address: "+email_address+" address_information: "+address_info+" room_num: "+room_num+"\n");
        }catch(err){
            console.log("An error has occured");
        }
    }
    make_reservation(){
        const reserv=new Room();
        console.log("Choose the type of the room you want to book:\n");
        console.log("1)Single\n2)Double\n3)Suite");
        let room_num=reserv.find_room();
    }
}
module.exports=Client;