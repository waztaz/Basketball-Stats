function changetable(data){

var table =  document.getElementById("table");
 var row;
 var cell1,cell2,cell3,cell4,cell5;
     for (var key in data){
           row = table.insertRow();
           row.insertCell(0);
           cell1 = row.insertCell(0);
           cell2 = row.insertCell(1);
           cell3 = row.insertCell(2);
           cell4 = row.insertCell(3);
           cell5 = row.insertCell(4);
           cell1.innerHTML = data[key]["number"];    
      }
}


function add() {
if (document.getElementById('sub').clicked == true){
   var x = document.getElementsByClassName("btn btn-primary btn-lg active").innerHTML
   console.log(x)

}

};

changetable(data)
}

function substituted_player(clickedID){
    
http.onreadystatechange = function() {
  if (this.readyState == 4 && this.status == 200) {
    data  = this.responseText;
    changetable(data)


  }
};
xhttp.open("GET", "sample/url/to/roster.view", true);
xhttp.send();
  


}

function substitute_player(clickedID){
    
http.onreadystatechange = function() {
  if (this.readyState == 4 && this.status == 200) {
    data  = this.responseText;
    changetable(data)


  }
};
xhttp.open("GET", "sample/url/to/roster.view", true);
xhttp.send();
  


}

function update(){
http.onreadystatechange = function() {
  if (this.readyState == 4 && this.status == 200) {
    data  = this.responseText;
    changetable(data)


  }
};
xhttp.open("GET", "sample/url/to/ingameupdateview", true);
xhttp.send();

}

window.onload = function iterator()
{
add()
   
}
