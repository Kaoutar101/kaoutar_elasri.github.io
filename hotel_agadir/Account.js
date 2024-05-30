const fs=require('fs');
const prompt=require('prompt-sync')({sigint: true})
class Account{
    constructor(email,password){
        this.email=email;
        this.password=password;
    }
    getemail(){
        return this.email;
    }
    setemail(email){
        this.email=email;
    }
    getpassword(){
        return this.password;
    }
    setpassword(){
        this.password=password;
    }

    managerLogin(email, password) {
        if (email === "manager@gmail.com" && password === "manager2024") {
            return true;
        } else {
            return false;
        }
    }

    create_account(email, password){
        try{
         fs.appendFileSync('data.txt','email: ${email} password: ${password}');
         console.log('Account created successfully')
        }catch(error){
         console.log('Wrong input');
         console.error(error);
        }
    }

    login(email,password){
        try{
            const data=fs.readFileSync('data.txt');
            const lines=data.split('\n');
            let found_email=false;
            let found_password=false;

            for(let i=0; i<lines.length;i++){
                const line=lines[i];
                if(line.includes('email: ')&& line.includes(email)){
                    found_email=true;
                    break;
                }
            }
            for(let i=0;i<lines.length;i++){
                const line=lines[i];
                if(line.includes('password:')&& line.includes(password)){
                    found_password=true;
                    break;
                }
            }
            return found_email && found_password;

        }catch(err){
            console.error('An error occured:',err);
            return false;
        }
    }
}
module.exports= Account;
