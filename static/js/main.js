$(document).ready(function () {
    autoFocusModal();
    sortSelector();
})

function autoFocusModal() {
    $('#searchModal').on('shown.bs.modal', function () {
        $('#product_search').trigger('focus')
    })
}

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