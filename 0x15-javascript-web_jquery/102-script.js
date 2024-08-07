$(document).ready(function() {
  $('#btn_translate').click(function() {
    // Get the language code from the input field
    const languageCode = $('#language_code').val();

    // Fetch the translation
    $.get('https://www.fourtonfish.com/hellosalut/hello/', { lang: languageCode }, function(data) {
      // Display the translation in the #hello div
      $('#hello').text(data.hello);
    }).fail(function() {
      // Handle errors (e.g., if the language code is invalid)
      $('#hello').text('Error: Could not fetch translation.');
    });
  });
});

