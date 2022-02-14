/* script that fetches and prints how to say “Hello” depending on the language */
$(function (){
  $('INPUT#btn_translate').click(function () {
    const lang = $('INPUT#language_code').val();
    if (lang){
      $.get(`https://www.fourtonfish.com/hellosalut/?lang=${lang}`, function (data, status) {
        $('DIV#hello').text(data.hello);
      });
    } else{
      alert('Choose a lenguage between fr, en or es');
    }
  });
});
