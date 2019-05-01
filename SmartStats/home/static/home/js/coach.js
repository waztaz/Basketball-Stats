
var url ='coachhome/'
var toggle = true
var select_sub = true
var current_player = null
var shot_value = null
var shot_result = null
function add(id,cls){
  console.log(toggle)
 
    if(cls != 'btn btn-primary btn-lg' && current_player != null){
    console.log(current_player)
    
    data = {'current_player':current_player,'id':id,'selector':'stat'}
    var xhr = new XMLHttpRequest();
// we defined the xhr

xhr.onreadystatechange = function () {
    if (this.readyState != 4) return;

    if (this.status == 200) {
        console.log("successfull")    // we get the returned data
    }

   // end of state change: it can be after some time (async)
};

xhr.open('POST',url+'stat', true);
xhr.send(JSON.stringify(data));
current_player = null;


}
}


function get_make_or_miss(id){
    console.log(current_player,shot_value,shot_result)
    shot_result = id

}




function get_shot_location(id,shot_value){

  if(current_player != null && shot_result != null){
    console.log(current_player)
    
    data = {'current_player':current_player,'shot_value':shot_value,'court_location':id,'selector':'shot','shot_result':shot_result}
    var xhr = new XMLHttpRequest();
// we defined the xhr

xhr.onreadystatechange = function () {
    if (this.readyState != 4) return;

    if (this.status == 200) {
        console.log("successfull")    // we get the returned data
    }

   // end of state change: it can be after some time (async)
};

xhr.open('POST',url+'shot', true);
xhr.send(JSON.stringify(data));
current_player = null
shot_value = null
shot_result =  null
}

}


function get_p(){
if (toggle == true)  
current_player = (event.srcElement.id)
else{
  console.log(event.srcElement.className)
  if(event.srcElement.className == "btn btn-primary btn-lg btn-danger active" || event.srcElement.className == "btn btn-primary btn-lg btn-danger active focus"){
    console.log("switch")
  event.srcElement.className = "btn btn-primary btn-lg"
}
  else{
  event.srcElement.className = "btn btn-primary btn-lg btn-danger"
 console.log("red")
}
}


}

function get_subs(){
  
 var x = document.getElementsByClassName("btn btn-primary btn-lg btn-danger")
 var subs = []
 var xhr = new XMLHttpRequest();
 for (var i =0;i<x.length;i++){
      subs.push(x[i].innerText)
  


 }
xhr.onreadystatechange = function () {
    if (this.readyState != 4) return;

    if (this.status == 200) {
        console.log("successfullsubs")    // we get the returned data
    }

   // end of state change: it can be after some time (async)
};

var sub_send = {'selector':'subs','sub_list':subs}
xhr.open('POST',url+'subs', true);
xhr.send(JSON.stringify(sub_send));
console.log(JSON.stringify(sub_send))
var x = document.getElementsByClassName("btn btn-primary btn-lg btn-danger")
while(x.length != 0){
  x[0].className = "btn btn-primary btn-lg" 
}
 toggle = true
}



function substitute(){
  toggle = false
  console.log(toggle)

  //var buttons = document.getElementsByClassName("btn btn-primary btn-lg")
  //console.log("helloooo")
  //for (var j =0;j<buttons.length;j++){
   // console.log(buttons[j].className)
    //buttons[j].className = "bt
}//

function set_line_up(){



}

