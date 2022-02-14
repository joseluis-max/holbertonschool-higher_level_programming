/* script that adds, removes and clears LI elements from a list when the user clicks */
$(function () {
  $('DIV#add_item').click(function () {
    $('UL.my_list').append('<li>Item</li>')
  });
  $('DIV#remove_item').click(function (event) {
    console.log($('UL.my_list:first-child').prevObject);
    $('LI:first-child').remove()
  });
  $('DIV#clear_list').click(function () {
    $('UL.my_list').empty();
  });
});
