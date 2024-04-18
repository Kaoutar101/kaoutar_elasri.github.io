package hotel_agadir;
public class Profile {
    protected String fname;
    protected String lname;
    protected int age;
    protected String email_adress;
    protected String adress_info;

    public Profile(String fname,String lname,int age, String email_adress,String adress_info){
        this.fname=fname;
        this.lname=lname;
        this.age=age;
        this.email_adress=email_adress;
        this.adress_info=adress_info;
    }


    public String get_fname(){
        return fname;
    }
    public void set_fname(String fname){
        this.fname=fname;
    }


    public String get_lname(){
        return lname;
    }
    public void set_lname(String lname){
        this.lname=lname;
    }

    public int get_age(){
        return age;
    }
    public void set_age(int age){
        this.age=age;
    }


    public String get_email_adress(){
        return email_adress;
    }
    public void set_email_adress(String email_adress){
        this.email_adress=email_adress;
    }


    public String get_adress_info(){
        return adress_info;
    }
    public void set_adress_info(String adress_info){
        this.adress_info=adress_info;
    }

    

}


