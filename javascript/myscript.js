// alert("Welcome to your bank!");
// var deposit=prompt("How much do you like to deposte today?");
// alert("You deposited:"+deposit);
// console.log("You are a cool person!");

var firstName=prompt("First Name Please: ");
var lastName=prompt("Last Name Please: ");
var age=prompt("How old are you? ");
var height=prompt("What is your height?");
var petName=prompt("What is you per name?");

//for condition
var namecond=null;
var agecond=null;
var heightcond=null;
var petcond=null;

//Name condition

if(firstName[0]===lastName[0]){
  namecond=true;
}
else {
  namecond=false;
}

//age condition

if(age>20 && age<30){
  agecond=true;
}
else {
  agecond=false
}

//height condition
if(height>=170){
  heightcond=true;
}
else {
  heightcond=false;
}

//pet condition
if(petName[petName.length-1]==="y"){
  petcond=true;
}
else {
  petcond=false;
}

if(namecond && agecond && heightcond && petcond){
  console.log('Welcome spy!');
}else {
  console.log('Noting to see here!');
}
