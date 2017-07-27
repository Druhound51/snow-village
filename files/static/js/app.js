$(function () {
    $('.form-cart').submit(function (e) {
        e.preventDefault();
        var $form = $(this);
        $price = 0
        $form.find(':button[type="submit"]').prop('disabled', true);
        $.ajax({
            type: 'POST',
            url: $form.attr('action'),
            data: $(this).serialize(),
            success: function (data) {
                var obj = JSON.parse(data);
                obj.forEach(function (item, i) {
                    $price += item.price * item.quantity
                    $('#product_price-' + item.id).text(item.price * item.quantity);
                    $('.total_price').text($price);
                });
                $('#thx').show();
            }
        })
    });
});