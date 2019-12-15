// Grab the Header with h1
var myHeader=document.querySelector("h1")

// Interface with the style.
//You will see a ton of options show up!
myHeader.style.color = 'red'
//rendom color generator
function getRandomColor() {
  var letters = '0123456789ABCDEF';
  var color = '#';
  for (var i = 0; i < 6; i++) {
    color += letters[Math.floor(Math.random() * 16)];
  }
  return color;
}

//simple function for change color
function changeHeaderColor(){
  colorInput=getRandomColor()
  myHeader.style.color=colorInput;
}

// Now perform the action over intervals (milliseocnds):
setInterval("changeHeaderColor()",500);
