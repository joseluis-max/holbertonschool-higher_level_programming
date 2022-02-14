/* script that fetches from https://fourtonfish.com/hellosalut/?lang=fr
and displays the value of hello from that fetch in the HTML tag DIV#hello */
$.get('https://fourtonfish.com/hellosalut/?lang=fr', function (data, status) {
  if (status == 'success'){
    $('DIV#hello').text(data.hello);
  } else {
    console.log('Error fetching API...');
  }
});
