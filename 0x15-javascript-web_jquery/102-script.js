$(document).ready(function() {
  $('#btn_translate').on('click', function() {
    const languageCode = $('#language_code').val();
    const url = `https://www.fourtonfish.com/hellosalut/hello/?lang=${languageCode}`;

    $.get(url, function(data) {
      $('#hello').text(data.hello);
    });
  });
});
