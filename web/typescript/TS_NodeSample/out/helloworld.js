var __extends = (this && this.__extends) || (function () {
    var extendStatics = function (d, b) {
        extendStatics = Object.setPrototypeOf ||
            ({ __proto__: [] } instanceof Array && function (d, b) { d.__proto__ = b; }) ||
            function (d, b) { for (var p in b) if (Object.prototype.hasOwnProperty.call(b, p)) d[p] = b[p]; };
        return extendStatics(d, b);
    };
    return function (d, b) {
        extendStatics(d, b);
        function __() { this.constructor = d; }
        d.prototype = b === null ? Object.create(b) : (__.prototype = b.prototype, new __());
    };
})();
//------------------------------
var message = "Hello World";
console.log(message);
var user = {
    name: "Ryan",
    id: 666
};
console.log("Hi!!" + user.name);
var myTrafficTool = "Bike";
console.log(myTrafficTool);
//------------------------------
function getLength(obj) {
    if (typeof obj === "string") {
        return "來了一個勇者，叫做" + obj;
    }
    else {
        return "對方來了" + obj.length + "個人!";
    }
}
console.log(getLength("王小明"));
console.log(getLength(["張三", "李四", "王五"]));
//------------------------------
function getNumber(obj) {
    if (typeof obj === "string") {
        return "國字的" + obj;
    }
    else {
        return obj + " + 3 = " + (obj + 3);
    }
}
console.log(getNumber("七"));
console.log(getNumber(7));
function printPoint(p) {
    console.log(p.x + "," + p.y);
}
var thisPoint = { x: 12, y: 26 };
printPoint(thisPoint);
var threePoint = { x: 12, y: 26, z: 89 };
printPoint(threePoint);
var className = ["HTML", "CSS", "JavaScript", "TypeScript"];
var audienceNumber = [666, 777, 888, 999];
var instructors = [{ name: "Ryan" }, { name: "David" }, { name: "John" }, { name: "Marry" }];
console.log("在" + className[0] + "課中，有" + audienceNumber[0] + "人參與，講師是" + instructors[0].name);
//------------------------------
var Days;
(function (Days) {
    Days[Days["\u661F\u671F\u5929"] = 7] = "\u661F\u671F\u5929";
    Days[Days["\u661F\u671F\u4E00"] = 1] = "\u661F\u671F\u4E00";
    Days[Days["\u661F\u671F\u4E8C"] = 2] = "\u661F\u671F\u4E8C";
    Days[Days["\u661F\u671F\u4E09"] = 3] = "\u661F\u671F\u4E09";
    Days[Days["\u661F\u671F\u56DB"] = 4] = "\u661F\u671F\u56DB";
    Days[Days["\u661F\u671F\u4E94"] = 5] = "\u661F\u671F\u4E94";
    Days[Days["\u661F\u671F\u516D"] = 6] = "\u661F\u671F\u516D";
})(Days || (Days = {}));
;
console.log("您預約的是" + Days[3]);
//------------------------------
var Person = /** @class */ (function () {
    function Person(name, phoneNumber) {
        this.name = "王小明";
        this.phoneNumber = 7533967;
        name ? this.name = name : null;
        phoneNumber ? this.phoneNumber = phoneNumber : null;
    }
    Person.prototype.sayHi = function () {
        return "\u4F60\u597D\uFF0C\u6211\u662F" + this.name;
    };
    Person.prototype.checkNumber = function (password) {
        if (password == "芝麻開門") {
            return this.name + "\u7684\u96FB\u8A71\u662F" + this.phoneNumber;
        }
        else {
            return "通關密碼錯誤";
        }
    };
    return Person;
}());
/*
let david = new Person("李大衛", 8825252);
console.log(david.sayHi());
console.log(david.checkNumber("芝麻開門"));*/
var ming = new Person();
console.log(ming.sayHi());
console.log(ming.checkNumber("芝麻開門"));
var Door = /** @class */ (function () {
    function Door() {
    }
    return Door;
}());
var SecurityDoor = /** @class */ (function (_super) {
    __extends(SecurityDoor, _super);
    function SecurityDoor() {
        return _super !== null && _super.apply(this, arguments) || this;
    }
    SecurityDoor.prototype.alert = function () {
        console.log('門上的警報器響了!');
    };
    return SecurityDoor;
}(Door));
var Car = /** @class */ (function () {
    function Car() {
    }
    Car.prototype.alert = function () {
        console.log('汽車上的警報器響了!');
    };
    return Car;
}());
var officeDoor = new SecurityDoor();
officeDoor.alert();
var myCar = new Car();
myCar.alert();
//# sourceMappingURL=helloworld.js.map