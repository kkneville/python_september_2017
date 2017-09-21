

$(document).ready(function(){
  // $('form').hide();
});

// $(document).on("click", "button", function() {
//       if ($("this").siblings('form').is(":hidden")) {
//         $("this").siblings('form').show();
//       }
//       else {
//         $("this").siblings('form').hide();
//       }
// });

$(document).on("click", ".enter", function() {
      $("this").siblings('form').show();
});
