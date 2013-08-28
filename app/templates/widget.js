function m(){
  $('#widget').prepend("<div>Widget</div><div>{{ note.text }}</div>");
}
$(document).ready(m);
