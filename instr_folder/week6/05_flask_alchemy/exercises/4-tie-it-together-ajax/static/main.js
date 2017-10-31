$(document).ready(function() {
  console.log('ready!');

  // make the person form use AJAX
  $('#person-form').on('submit', function(event) {
    event.preventDefault();
    data = $('person-form').serialize();
    $.ajax({
      method: 'POST',
      url: '/add-person',
      data: data,
      success: function(response) {
        console.log(response);
      }
    });
  });

  // make the thinkpad form use AJAX
});
