$(document).ready(function () {
    autoFocusModal();
    sortSelector();
    toTopBtn();
})

// Autofocus inputs on search modal
function autoFocusModal() {
    $('#searchModal').on('shown.bs.modal', function () {
        $('#product_search').trigger('focus')
    })
}

// Re-sort the Catalog page when select element is changed
function sortSelector() {
    $('#sort-selector').change(function () {
        let selector = $(this)
        let selectedValue = selector.val()
        let currentUrl = new URL(window.location)

        if (selectedValue != 'reset') {
            let sort = selectedValue.split('_')[0]
            let direction = selectedValue.split('_')[1]

            currentUrl.searchParams.set('sort', sort)
            currentUrl.searchParams.set('direction', direction)
            window.location.replace(currentUrl)
        } else {
            currentUrl.searchParams.delete('sort')
            currentUrl.searchParams.delete('direction')

            window.location.replace(currentUrl)
        }
    })
}

// Fade in Return to Top Button, smooth scroll to top on click, allow user to interrupt scroll with input
function toTopBtn() {
    $(window).scroll(function () {
        if ($(this).scrollTop() > 150) {
            $('#toTopBtn').fadeIn();
        } else {
            $('#toTopBtn').fadeOut();
        }
    });
    $('#toTopBtn').click(function () {
        $('html, body').stop().animate({
            scrollTop: 0
        }, 500);
    });
    $('html, body').on('scroll mousedown DOMMouseScroll mousewheel keyup touchstart', function (e) {
        if (e.which > 0 || e.type === 'mousedown' || e.type === 'mousewheel' || e.type === 'touchstart') {
            $('html, body').stop();
        }
    });
}