let user_name, user_email, phone, address, city, state, zipcode;

if(user !== "AnonymousUser"){
    const userInfo = 
        `<h5> 
            Hello ${user}, please enter your shipping information below.
        </h5>
        <div class="form-field">
            <input required class="form-control" type="phone" name="phone" placeholder="Phone..">
        </div>`
    $('#user-info').html(userInfo)
}


function submitOrderForm(){
    let formData  = $("#checkoutForm")

    // Grab value from forms
    user ? user_name = user: user_email = formData.find('input[name="name"]').val();
    email ? user_email = email: email = formData.find('input[name="email"]').val();
    phone = formData.find('input[name="phone"]').val()
    address = formData.find('input[name="address"]').val()
    city = formData.find('input[name="city"]').val()
    state = formData.find('input[name="state"]').val()
    zipcode = formData.find('input[name="zipcode"]').val()
    console.log(user_name, user_email, phone)
    console.log(address, city, state, zipcode)


    // Checkout user data
    let userData = {
        'name': user_name,
        'email': user_email,
        'total': null

    }

    // Shipping data
    let shippingData = {
        'address': address,
        'city': city,
        'state': state,
        'zipcode': zipcode
    }

    formData.find('input:required').each(function() {
        formData.validate();
        if ($(this).val() === ''){
            alert('error please fill all fields!');
        }else{
            $("#payment").css('visibility', 'visible');
        }
      });
}

$('#form-button').click(function(e){
    e.preventDefault();
    submitOrderForm();

})