// //homework 1
// const me = {
//     person:{
//         name:'roba',
//         age:14,
//         height:153  
//     },
//     greet:function(greating){
//         return(me.person.name = 'როგორ ხარ?')
//     }
// }
// //homework 2
// let x = 10
// //homework 3
// let y = me.person.name
// console.log(y, x)

function fly (flyingcode,flyingstatus){
    this.code = flyingcode;
    this.status = flyingstatus;
}
let plane = new fly('NGT700', 'landed')
let plane2 = new fly('NGT600', 'flying')

console.log(plane,plane2)