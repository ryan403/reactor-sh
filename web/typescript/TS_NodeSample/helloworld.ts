//------------------------------
let message:string = "Hello World";
console.log(message);

//------------------------------
interface User{
    name:String;
    id:number
}

const user:User = {
    name:"Ryan",
    id:666
};

console.log("Hi!!"+user.name);

//------------------------------
type trafficTools = "Bike" | "Car" | "Scooter";

let myTrafficTool:trafficTools = "Bike";

console.log(myTrafficTool);

//------------------------------
function getLength(obj: string | string[]){
    if(typeof obj === "string"){
        return "來了一個勇者，叫做"+obj;
    }else{
        return "對方來了"+obj.length+"個人!";
    }
}

console.log(getLength("王小明"));
console.log(getLength(["張三","李四","王五"]));

//------------------------------
function getNumber(obj: number | string){
    if(typeof obj === "string"){
        return "國字的"+obj;
    }else{
        return obj+" + 3 = "+(obj+3);
    }
}

console.log(getNumber("七"));
console.log(getNumber(7));

//------------------------------
interface Point{
    x:number;
    y:number;
    z?:number;
}

function printPoint(p:Point){
    console.log(p.x+","+p.y);
}

const thisPoint:Point = {x:12, y:26};
printPoint(thisPoint);

const threePoint:Point = {x:12, y:26, z:89};
printPoint(threePoint);

//------------------------------
/*
type StringArray = Array<String>;
type NumberArray = Array<number>;
type ObjectWithNameArray = Array<{name:string}>;
*/

type StringArray = string[];
type NumberArray = number[];
type ObjectWithNameArray = {name:string}[];

let className:StringArray = ["HTML", "CSS", "JavaScript", "TypeScript"];
let audienceNumber:NumberArray = [666,777,888,999];
let instructors:ObjectWithNameArray = 
    [{name:"Ryan"},{name:"David"},{name:"John"},{name:"Marry"}];

console.log("在"+className[0]+"課中，有"+audienceNumber[0]+"人參與，講師是"+instructors[0].name);

//------------------------------

enum Days {星期天=7, 星期一=1, 星期二=2, 星期三=3, 星期四=4, 星期五=5, 星期六=6};

console.log("您預約的是"+Days[3]);

//------------------------------
class Person{
    name:String = "王小明";
    private phoneNumber:number = 7533967;
    constructor(name?: String, phoneNumber?:number){
        name ? this.name = name : null;
        phoneNumber ? this.phoneNumber = phoneNumber : null;
    }
    sayHi(){
        return `你好，我是${this.name}`;
    }
    checkNumber(password:String){
        if(password=="芝麻開門"){
            return `${this.name}的電話是${this.phoneNumber}`;
        }else{
            return "通關密碼錯誤";
        }
    }
}

/*
let david = new Person("李大衛", 8825252);
console.log(david.sayHi());
console.log(david.checkNumber("芝麻開門"));*/
let ming = new Person();
console.log(ming.sayHi());
console.log(ming.checkNumber("芝麻開門"));

//------------------------------

interface Alarm{
    alert();
}

class Door{

}

class SecurityDoor extends Door implements Alarm{
    alert(){
        console.log('門上的警報器響了!');
    }
}

class Car implements Alarm{
    alert(){
        console.log('汽車上的警報器響了!');
    }
}

let officeDoor = new SecurityDoor();
officeDoor.alert();
let myCar = new Car();
myCar.alert();