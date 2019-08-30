
function updatePlayers(data){
document.getElementById('players')
var elementToAdd = document.createElement("input");
elementToAdd.name = "add";
elementToAdd.className="btn btn-primary btn-lg active";
elementToAdd.value = data.name
document.getElementById('players').appendChild(elementToAdd);

}


function getPlayers(){
const url = "url to get player"
var data = fetch(url).then(data=> {return data.json()}).then(response=> {console.log(response)})
return data
}

window.onload = function iterator()
{
updatePlayers(getPlayers())
   
}
