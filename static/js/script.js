$(document).ready(function(){
    $('.sidenav').sidenav({edge: 'right'});
    $('.tooltipped').tooltip();
    $('select').formSelect();   
    $('.fixed-action-btn').floatingActionButton();
    $('.chips').chips();
    $('.modal').modal();
    });



// compare password and confirm password fields
    $("#password").on("focusout", function (e) {
        if ($(this).val() != $("#passconf").val()) {
            $("#passconf").removeClass("valid").addClass("invalid");
        } else {
            $("#passconf").removeClass("invalid").addClass("valid");
        }
    });
    
    $("#passconf").on("keyup", function (e) {
        if ($("#password").val() != $(this).val()) {
            $(this).removeClass("valid").addClass("invalid");
        } else {
            $(this).removeClass("invalid").addClass("valid");
        }
    });
  
    
// create and remove controls dynamically
function GetLastStepNo(container){
    searchstr = "ing_";
    if (container != "ingredients-container" )
        {
            searchstr = "meth_";
        }

  Cont = document.getElementById(container)

  divChildren = Cont.childNodes;


  let x = 0;
  if (divChildren.length == 0) {
    return 0;
  }
  else {
    for (var i=0; i < divChildren.length; i++) {
      let str = divChildren[i].id;
      if (typeof str !== 'undefined'){
        if (str.includes(searchstr)) {
          x++;
        } 
      }
    }
  }
  return x;
}
    function addIngredient(num,container){
        //use this function to add form control for both
        //ingredients and method steps
        let arr= 'ing';
        let button_delete = 'but_';
        let button_add ='but_add_';
        let br_element = "br_";
        let placeholder_text = "add your ingredient here";
        if (container != 'ingredients-container'){
            arr = 'meth';
            button_delete = 'mbut_';
            button_add = 'mbut_add_';
            br_element = "mbr_";
            placeholder_text = "add your method step here";
        }

        ingCont = document.getElementById(container)
        // Create a break line element
        let br = document.createElement("br"); 
        br.setAttribute("id",br_element + num);

        let no = document.createElement("input");
        no.setAttribute("type", "text");
        no.setAttribute("id", arr + "_" + num);
        no.setAttribute("name", arr +"[]");
        no.setAttribute("placeholder", placeholder_text);
        no.setAttribute("minlength","5");
        no.setAttribute("maxlength","200");
        no.setAttribute("class","validate required");
        

        let but = document.createElement("button")
        but.setAttribute("type","button")
        but.setAttribute("id",button_delete + num)
        but.setAttribute("name", button_delete + num);
        but.setAttribute("onclick","removeIngredient(" + num +",'" + container +"');")
        but.setAttribute("class","btn-floating btn-small waves-effect waves-light red")
        but.innerHTML= "<i class='far fa-minus-square'></i>"

        let butAdd = document.createElement("button")
        butAdd.setAttribute("type","button")
        butAdd.setAttribute("id",button_add + num)
        butAdd.setAttribute("name", button_add + num);
        butAdd.setAttribute("onclick","addIngredient(GetLastStepNo('" + container +"')+1,'" + container +"');")
        butAdd.setAttribute("class","btn-floating btn-small waves-effect waves-light green")
        butAdd.innerHTML= "<i class='far fa-plus-square'></i>"

        
        ingCont.appendChild(br);
        ingCont.appendChild(no);
        ingCont.appendChild(but);
        ingCont.appendChild(butAdd);
        
    }

    function removeIngredient(stepno,container){
        let arr= 'ing_';
        let button_delete = 'but_';
        let button_add ='but_add_';
        let bre = "br_";

        
        if (container != "ingredients-container"){
            arr= 'meth_';
            button_delete = 'mbut_';
            button_add ='mbut_add_';
            bre = "mbr_";
        }
        document.getElementById(arr + stepno).remove();
        document.getElementById(button_delete + stepno).remove();
        document.getElementById(button_add + stepno).remove();
        document.getElementById(bre + stepno).remove();
    }