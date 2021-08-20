$(document).ready(function(){
    $('.sidenav').sidenav({edge: 'right'});
    $('.tooltipped').tooltip();
    $('select').formSelect();   
    $('.fixed-action-btn').floatingActionButton();
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
