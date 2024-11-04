$(document).ready(function () {
    $('.languages').select2({
        minimumResultsForSearch: Infinity,
        containerCssClass: "error",
        dropdownCssClass: "test"
    });


    $('.close-btn').click(() => {
        $('#myModal').removeClass('show')
        $('#myModal').css({display: "none"});
        $('body').css({overflow: 'auto'});
        $('body').css({paddingRight: '0'});
        $('.modal-backdrop').removeClass('show').css({display: "none"});
    })
});


