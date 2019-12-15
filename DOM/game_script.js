//restart game button
var restart=document.querySelector("#b")
//grab all the square
var squares=document.querySelectorAll("td")
//clear all the square
function clearboard(){
  for(i=0;i<squares.length;i++){
    squares[i].textContent="";
  }
}

restart.addEventListener('click',clearboard);
//check the square marker
function changeMarker(){
  if(this.textContent===''){
    this.textContent='X';
  }else if (this.textContent==='X') {
    this.textContent='0';
  }else {
    this.textContent='';
  }
}
//for loop to add event listners to all the square
for (var i = 0; i <squares.length; i++) {
squares[i].addEventListener('click',changeMarker);
}
