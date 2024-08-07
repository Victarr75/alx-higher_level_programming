i$(document).ready(function() {
  // Function to fetch and display the translation
  function fetchTranslation() {
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
  }

  // Attach the click event handler to the button
  $('#btn_translate').click(fetchTranslation);

  // Attach the keypress event handler to the input field
  $('#language_code').keypress(function(event) {
    // Check if the ENTER key is pressed
    if (event.which === 13) {
      fetchTranslation();
    }
  });
});

