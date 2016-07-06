// Transitions for forms
$(document).ready(function(){
  $(".option1").click(function(){
   $("#form1").css("display", "block");
 });
  $(".option1").click(function(){
    $("#default-present").css("display","none");
  });
  $(".option1").click(function(){
   $("#form2").css("display", "none");
 });
  $(".option1").click(function(){
   $("#form3").css("display", "none");
 });
  $(".option1").click(function(){
    $("#form5").css("display", "none");
  });
  $("#cancel-btn-1").click(function(){
    $("#form1").hide(1);
    $("#default-present").slideDown("slow");
  });
  $(".option1").click(function(){
   $("#form4").css("display", "none");
 });
  $(".option2").click(function(){
   $("#form2").css("display", "block");
 });
  $(".option2").click(function(){
    $("#default-present").css("display","none");
  });
  $(".option2").click(function(){
   $("#form1").css("display", "none");
 });
  $(".option2").click(function(){
   $("#form3").css("display", "none");
 });
  $(".option2").click(function(){
   $("#form4").css("display", "none");
 });
  $(".option2").click(function(){
    $("#form5").css("display", "none");
  });
  $("#cancel-btn-2").click(function(){
    $("#form2").hide(1);
    $("#default-present").slideDown("slow");
  });
  $(".option3").click(function(){
   $("#form3").css("display", "block");
 });
  $(".option3").click(function(){
    $("#default-present").css("display","none");
  });
  $(".option3").click(function(){
   $("#form1").css("display", "none");
 });
  $(".option3").click(function(){
   $("#form2").css("display", "none");
 });
  $(".option3").click(function(){
   $("#form4").css("display", "none");
 });
  $(".option3").click(function(){
    $("#form5").css("display", "none");
  });
  $("#cancel-btn-3").click(function(){
    $("#form3").hide(1);
    $("#default-present").slideDown("slow");
  });
  $(".option4").click(function(){
   $("#form4").css("display", "block");
 });
  $(".option4").click(function(){
    $("#default-present").css("display","none");
  });
  $(".option4").click(function(){
   $("#form1").css("display", "none");
 });
  $(".option4").click(function(){
   $("#form2").css("display", "none");
 });
  $(".option4").click(function(){
   $("#form3").css("display", "none");
 });
  $("#cancel-btn-4").click(function(){
    $("#form4").hide(1);
    $("#default-present").slideDown("slow");
  });
  $(".option4").click(function(){
    $("#form5").css("display", "none");
  });
  $(".option5").click(function(){
    $("#form5").css("display", "block");
  });
  $(".option5").click(function(){
    $("#default-present").css("display","none");
  });
  $(".option5").click(function(){
    $("#form2").css("display", "none");
  });
  $(".option5").click(function(){
    $("#form3").css("display", "none");
  });
  $("#cancel-btn-5").click(function(){
    $("#form5").hide(1);
    $("#default-present").slideDown("slow");
  });
  $(".option5").click(function(){
    $("#form4").css("display", "none");
  });
});

function check_preferred_media(){
  var preferred_media=document.getElementById("preferred_media").value;  
  if (preferred_media==4) {
    document.getElementById("other-hidden-textarea").style.display = "block";   
  }  
  else{
    document.getElementById("other-hidden-textarea").style.display = "none"; 
  }
}


function found_us(){
  var others=document.getElementById("others").checked;
  var friends=document.getElementById("friends").checked;
  var internet=document.getElementById("internet").checked;
  var teachers=document.getElementById("teachers").checked;
  var colleague=document.getElementById("colleague").checked;
  if (others) {
    document.getElementById("foundus-hidden-textarea").style.display = "block";     
  }
  if(friends||internet||teachers||colleague){
    document.getElementById("foundus-hidden-textarea").style.display = "none"; 
  }
}

function check_recommendation(){
  var norecommendation = document.getElementById("no_recommendation").checked;
  var yesrecommendation = document.getElementById("yes_recommendation").checked;
  if (norecommendation) {
    document.getElementById("no-hidden-textarea").style.display = "block";      
  }
  if (yesrecommendation) {
    document.getElementById("no-hidden-textarea").style.display = "none";    
  }
}