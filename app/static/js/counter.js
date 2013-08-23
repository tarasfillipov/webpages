$(function() {
$(".countered textarea").keyup(function count(){
number = $(".countered textarea").val().length;
$("#counter_area").html("Total: "+number);
});
});