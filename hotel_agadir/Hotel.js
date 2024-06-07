const Account = require('./Account');
const Client = require('./Client');
const Manager = require('./Manager');
const Room = require('./Room');
const prompt=require('prompt-sync')({sigint: true})

let email = null;
let password = null;

console.log('Welcome to hotel Agadir\n');
console.log('Are you a Manager (1) or a Client (1)');
let answer = prompt("type your choice\n");
const account = new Account(email, password);

if (answer == 1) {
    let accnt=false;
    let i=0;
    while(!accnt && i<3){
        console.log("enter your credentials\n");
        email=prompt("email adress:\n");
        password=prompt("email adress:\n");
        accnt=account.managerLogin(email,password);

        if(accnt){
            i=3;
        }
        else{
            console.log("wrong credentials");
            i++;
        }
    }
    let again='yes';
    while(again=='yes'){
        if(accnt){
            const manager=new Manager();
            manager.hotel_organize();
            console.log('Do you want to add another room information\n');
            again=prompt('yes/no\n');
        }
    }
    

} else if (answer == 2) {
    console.log("Welcome to Hotel Agadir, to browse our menu you can choose one of the following options:\n");
    let account_choice = prompt("1)login\n2)Create an account\n");
    console.log("Enter your credentials\n");
    email = prompt('Enter your email address\n');
    password = prompt('Enter your password\n');
    let created = false;
    let answ = false;

    if (account_choice == 2) {
        account.create_account(password, email);
        created = true;
        
    } 
    else if (account_choice == 1) {
        let i = 0;
        while (i < 3) {
            answ = account.login(password, email);
            if (answ) {
                console.log("logged in successfully\n");
                i = 3;
            } else {
                console.log("login failed. Please try again\n");
                i++;
            }
        }
    }

    if (answ == true && created == true) {
        const rm = new Room();
        console.log("Enter the following information about yourself:\n");
        let fname = prompt('First name:\n');
        let lname = prompt('Last name:\n');
        let age = prompt('Age:\n');
        let email_address = prompt('Email address;\n');
        let address_info = prompt('Address information:\n');
        const cl = new Client(fname, lname, age, email_address, address_info);
        let room_number = cl.make_reservation();
        rm.edit(room_number,true);
        
    }
}
