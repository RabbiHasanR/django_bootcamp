var employee={
  name: 'Rabbi Hasan',
  job: 'Programmer',
  age: 24,
  nameLength:function(){
    alert(this.name.length);
  },
  report:function(){
    alert("Name: "+this.name+" Job title: "+this.job+" Age: "+this.age);
  },
  lastName: function(){
    console.log(this.name.split(" ")[1]);
  }
}
