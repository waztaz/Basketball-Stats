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
           cell1.innerHTML = data[key]["name"];
           cell2.innerHTML = data[key]["lineups"];
           cell3.innerHTML = data[key]["hotzones"];
           cell4.innerHTML = data[key]["bestq"];
           cell5.innerHTML = data[key]["asto"];
    
      }
}


function add() {

var data = {
  Player1: { "name":"Chris Dude",
  "lineups": "James Worthy Lebron James Kwame Brown",
  "hotzones": "1,3,5",
  "bestq": "3",
  "asto":".6"
},
Player2: {"name":"Chris Dude",
  "lineups": "James Worthy Lebron James Kwame",
  "hotzones": "1,3,5",
  "bestq": "3",
  "asto":".6"
}};

changetable(data)
}

function choose_game(clickedID){
    
http.onreadystatechange = function() {
  if (this.readyState == 4 && this.status == 200) {
    data  = this.responseText;
    changetable(data)


  }
};
xhttp.open("GET", "sample/url/to/analytics.view", true);
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