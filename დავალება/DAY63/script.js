// //homework 0 
// function student(name,surname,points){
//     this.name0 = name;
//     this.surname0 = surname;
//     this.points0 = points;
// }

// let student0 = new student('roba',14,10)
// console.log(student0)

function car(brand,model,engine){
    this.brand0 = brand;
    this.model0 = model;
    this.engine0 = engine;
}

let Car = new car('BMW','M5',3.0)
console.log(Car)

function myComputer(CPU,GPU,RAM){
    this.cpu0 = myComputer;
    this.gpu0 = myComputer;
    this.ram0 = myComputer;
}

let Pc = new myComputer('I5 12400F','GTX 1070',32)
console.log(Pc)

function myPhone(brand,model,ram){
    this.brand0 = myPhone;
    this.model0 = myPhone;
    this.ram0 = myPhone;
}

let Phone = new myPhone('xiaomi','note 8',4)
console.log(Phone)

function myMonitor(model,inch,hz){
    this.model0 = myMonitor;
    this.inch0 = myMonitor;
    this.hz0 = myMonitor;
}

let Monitor = new myMonitor('2E',27,75)
console.log(Monitor)