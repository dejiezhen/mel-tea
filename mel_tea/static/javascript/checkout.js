if(user !== "AnonymousUser"){
    const userInfo = `<h5> Hello ${user}, please enter your
    shipping information below.
    </h5>`
    $('#user-info').html(userInfo)
}


function submitOrderForm(){
    let formData  = $("#checkoutForm")
    console.log(formData.find('input[name="city"]').val());
    // Checkout user data
    let userData = {
        'name': null,
        'email': null,
        'total': null

    }

    // Shipping data
    let shippingData = {
        'address':null,
        'city': null,
        'state': null,
        'zipcode': null
    }


}

$('#form-button').submit(function(e) {
    e.preventDefault();
    let formData  = $("#checkoutForm")
    console.log(formData.find('input[name="city"]').val());

});