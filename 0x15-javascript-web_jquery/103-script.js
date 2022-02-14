/* script that fetches and prints how to say “Hello” depending on the language with enter on focus */
function hello () {
    const lang = $('INPUT#language_code').val();
    if (lang) {
        $.get(`https://www.fourtonfish.com/hellosalut/?lang=${lang}`, function (data, status) {
            $('DIV#hello').text(data.hello);
        });
    } else {
        alert('Choose a lenguage between fr, en or es');
    }
};

$(function () {
    $('INPUT#btn_translate').click(hello);
    $(document).on('keypress', function (event) {
        if (event.which === 13){
            if ($('INPUT#language_code').is(':focus')){
                hello();
            }
        }
    });
});
