

let now = new Date()
let different = new Date("2022-08-06T09:53:15.338Z")

different.setDate(now.getDate())
different.setMonth(now.getMonth())
different.setFullYear(now.getFullYear())
console.log(different);
console.log(now);