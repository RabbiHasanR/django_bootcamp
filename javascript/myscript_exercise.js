var roster=[]

function addName(){
  var newName=prompt("What name would you like to add?")
  roster.push(newName)
}

function remove(){
  var reName=prompt("What name would you like to remove?")
  var index=roster.indexOf(reName)
  roster.splice(index,1)
}

function display(){
  console.log(roster);
}

var start=prompt("Would you like to roster web app?y/n");
var request='empty';

if(start==='y'){
  while (request!=='quit') {
    request=prompt("Please select an action: add,remove,display or quit")
    if(request==='add'){
      addName();
    }else if (request==='remove') {
      remove();
    }else if (request==='display') {
      display();
    }else {
      alert("Not recognize!")
    }
  }
}

alert("Thanks for the web app!Please refresh to start over.")
