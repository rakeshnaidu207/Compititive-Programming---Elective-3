// Write a class called Dog that has two properties: name and age. Write a constructor that takes three arguments self, name and age and set these to the object properties.
// Now write a function sayHI(dog) where dog is the dog class object that returns a Hi, my name is <dog’s name> and I am <age> years old!

// sayHi(d1) # Hi, my name is Dot and I am 4 years old!
// sayHi(d2) # Hi, my name is Elf and I am 3 years old!


public class SayHi {
    String name;
    int age;
    SayHi(String n, int i){
        name=n;
        age=i;
    }
    public void Display(){
        System.out.println("Hi"+","+"my name is"+" "+name+" "+"and"+" "+"I am "+age+" "+"years old!" );
    }

    public static void main(String args[]) {
        SayHi d1=new SayHi("Dot",4);
        SayHi d2=new SayHi("ELF",3);
        d1.Display();
        d2.Display();
        
    }
}
