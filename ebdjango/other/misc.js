$('.basicAutoComplete').autoComplete({
    minLength: 1
});
$(function () {
    $('[data-toggle="popover"]').popover()
    $('#ShowTipsBtn').on('click', function () {
        $('.tip-container').popover('toggle');
        $('#help-post').toggle();
    });
})