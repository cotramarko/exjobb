$( document ).ready(function() {
    console.log( "ready!" );


      $(function() {
    $('.error').hide();
    $(".button").click(function() {
      // validate and process form here

      $('.error').hide();
      var from = $("input#from").val();
      if (from == "") {
        $("label#from_error").show();
        $("input#from").focus();
        return false;
      }
      var dest = $("input#dest").val();
      if (dest == "") {
        $("label#dest_error").show();
        $("input#dest").focus();
        return false;
      }
      

  var time = $("select#time").val();
  var team = $("select#team").val();
  var car = $("select#car").val();

  // Check availability
  var TimeToCol = {"08:00" : 0, "09:00" : 1, "10:00" : 2, "11:00" : 3, "12:00" : 4, "13:00" : 5, "14:00" : 6, "15:00" : 7, "16:00" : 8, "17:00" : 9};
  var table = $("table tbody")[0];
  console.log(table.rows[car-1].cells[TimeToCol[time]].classList.contains( "clicked"));
  if(table.rows[car-1].cells[TimeToCol[time]].classList.contains( "clicked")) {
    $("label#submit_error").show();
    $("input#time").focus();
    return false;
  }
  var dataString = 'from=' + from + '&dest=' + dest + '&time=' + time + '&team=' + team + '&car=' + car;
  // alert (dataString);return false;

  $.ajax({
    type: "POST",
    url: "http://localhost:3000/searching",
    data: dataString,
    success: function(data) {
      //console.log(data)
      Updatetransport();
      $('#contact_form').html("<div id='message'></div>");
      $('#message').html("<h2>Contact Form Submitted!</h2>")
      .hide()
      .fadeIn(1500, function() {
        //$('#message').append("<img id='checkmark' src='images/check.png' />");
      $('#message').append("<p>We will be in touch soon.</p>")
      .hide()
      });
    }
  });
  return false;

    });
  });



  

  });
    


$(function(){
 $('#search').on('keyup', function(e){
   if(e.keyCode === 13) {
     var parameters = { search: $(this).val() };
       $.get( '/searching',parameters, function(data) {
       $('#results').html(data);
     });
    };
 });
});

function Updatetransport() {

$.ajax({
    type: "GET",
    url: "http://localhost:3000/transport",
    success: function(data) {
      var transports = $.parseJSON (JSON.stringify(data));
      //console.log(transports);
      var booked = [];
      $.each(transports, function(index, data) {
                //$('#customers').append(data.firstName);
                //console.log(data.time)
                booked.push([data.car,data.time])
                
      });
                //console.log(booked);

                
                // var cell = table.rows[1].cells[1]; // This is a DOM "TD" element
                // var $cell = $(cell); // Now it's a jQuery object.
                var table = $("table tbody")[0];
                var testdata = [[1,"8"],[3,"10"],[2,"13"]];
               
               var TimeToCol = {"08:00" : 0, "09:00" : 1, "10:00" : 2, "11:00" : 3, "12:00" : 4, "13:00" : 5, "14:00" : 6, "15:00" : 7, "16:00" : 8, "17:00" : 9};
                
                $.each(booked, function(index, data) {
                cell = table.rows[data[0]-1].cells[TimeToCol[data[1]]];
                cell.className='clicked';
                //console.log(cell)
                });
    }
  });
  return false;

}



