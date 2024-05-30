const Account = require('./Account');
const Client = require('./Client');
const Manager = require('./Manager');
const Room = require('./Room');

// Function to save user information to local storage
function saveUserInfo(email, password) {
    localStorage.setItem('email', email);
    localStorage.setItem('password', password);
}

// Function to retrieve user information from local storage
function getUserInfo() {
    const email = localStorage.getItem('email');
    const password = localStorage.getItem('password');
    return { email, password };
}

let email = null;
let password = null;

console.log('Welcome to hotel Agadir\n');
console.log('Are you a Manager (1) or a Client (1)');
let answer = prompt("type your choice\n");
const account = new Account(email, password);

if (answer == 1) {
    // Manager login logic
} else if (answer == 2) {
    console.log("Welcome to Hotel Agadir, to browse our menu you can choose one of the following options:\n");
    let account_choice = prompt("1)login\n2)Create an account\n");
    console.log("Enter your credentials\n");
    email = prompt('Enter your email address\n');
    password = prompt('Enter your password\n');
    let created = false;
    let answ = false;

    if (account_choice == 2) {
        // Create account logic
        account.create_account(password, email);
        created = true;
        // Save user information
        saveUserInfo(email, password);
    } else if (account_choice == 1) {
        // Login logic
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
        // Client reservation logic
        const rm = new Room();
        console.log("Enter the following information about yourself:\n");
        let fname = prompt('First name:\n');
        let lname = prompt('Last name:\n');
        let age = prompt('Age:\n');
        let email_address = prompt('Email address;\n');
        let address_info = prompt('Address information:\n');
        const cl = new Client(fname, lname, age, email_address, address_info);
        let f = cl.make_reservation();
    }
}
