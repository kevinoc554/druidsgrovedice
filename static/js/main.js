$(document).ready(function () {
    checkQtyInputsOnLoad();
    checkQtyInputsOnChange();
    incrementQty();
    decrementQty();
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

// Increment the quantity input by one when the Plus icon is clicked
function incrementQty() {
    $('.increment-qty').click(function (e) {
        e.preventDefault();
        let itemId = $(this).data('item_id');
        let currentValue = parseInt($(`.id_qty_${itemId}`).val())
        let newValue = currentValue + 1
        $(`.id_qty_${itemId}`).val(newValue)
        enableDisableQuantityInputs(itemId)
    })
}


// Decrement the quantity input by one when the Minus icon is clicked
function decrementQty() {
    $('.decrement-qty').click(function (e) {
        e.preventDefault();
        let itemId = $(this).data('item_id');
        let currentValue = parseInt($(`.id_qty_${itemId}`).val())
        let newValue = currentValue - 1
        $(`.id_qty_${itemId}`).val(newValue)
        enableDisableQuantityInputs(itemId)
    })
}


// Disable +/- buttons to prevent users from inputting
// a value below 1, or above 99
function enableDisableQuantityInputs(itemId) {
    let currentValue = parseInt($(`.id_qty_${itemId}`).val())
    let minusDisabled = currentValue < 2
    let plusDisabled = currentValue > 98

    $(`.increment-qty_${itemId}`).prop('disabled', plusDisabled)
    $(`.decrement-qty_${itemId}`).prop('disabled', minusDisabled)
}

// Check input elements on load and disable +/- buttons as needed
function checkQtyInputsOnLoad() {
    let allQuantityInputs = $('.qty_input');
    for (let i = 0; i < allQuantityInputs.length; i++) {
        let itemId = $(allQuantityInputs[i]).data('item_id');
        enableDisableQuantityInputs(itemId);
    }
}

// Check input elements on change of input value and disable +/- buttons as needed
// Handles direct user inputs
function checkQtyInputsOnChange() {
    $('.qty_input').change(function() {
        let itemId = $(this).data('item_id');
        enableDisableQuantityInputs(itemId);
    })
}

// Enable Bootstrap tooltips
$(function () {
    $('[data-toggle="tooltip"]').tooltip()
  })