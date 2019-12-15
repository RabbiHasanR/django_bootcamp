// function hello(){
//   console.log("hello world!");
// }

function sleepin(weekday,vacation){
  return(!weekday||vacation)
}

function monkeytrouble(asmile,bsmile){
  return(asmile && bsmile)||(!asmile && !bsmile)
}

function stringtimes(str,n){
  var returnstrin=""
  var i=0
  while(i<n){
    returnstrin+=str
    i++
  }
  return returnstrin
}
function luckysum(a,b,c){
  if(a===13){
    return 0
  }
  if(b===13){
    return a
  }
  if(c===13){
    return a+b
  }
  return a+b+c
}

function caght_speeding(speed,is_birthday){
  if(is_birthday){
    speed-=5
  }
  if(speed<=60){
    return 0
  }
  if(60<speed<=80){
    return 1
  }
  return 2
}

function makebricks(small,big,goal){
  return goal%5>=0 && goal%5 - small <=0 && small + 5*big>=goal;
}
