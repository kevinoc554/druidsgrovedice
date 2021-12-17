$(document).ready(function () {
    autoFocusModal();
})

function autoFocusModal() {
    $('#searchModal').on('shown.bs.modal', function () {
        $('#product_search').trigger('focus')
    })
}