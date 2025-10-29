// Smooth scrolling for nav links (extracted from home.html)
$(document).ready(function () {
    // Added smooth scrolling to all links with a class of 'nav-link'
    $(".nav-link").on('click', function (event) {

        if (this.hash !== "") {
            event.preventDefault();
            var hash = this.hash;

            $('html, body').animate({
                scrollTop: $(hash).offset().top
            }, 800, function () {

                window.location.hash = hash;
            });
        }
    });
});
