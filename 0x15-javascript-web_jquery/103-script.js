$(document).ready(function() {
  function fetchHello() {
    const languageCode = $('#language_code').val();
    const url = `https://www.fourtonfish.com/hellosalut/hello/?lang=${languageCode}`;

    $.get(url, function(data) {
      $('#hello').text(data.hello);
    });
  }

  $('#btn_translate').on('click', function() {
    fetchHello();
  });

  $('#language_code').on('keypress', function(event) {
    if (event.key === 'Enter') {
      fetchHello();
    }
  });
});
