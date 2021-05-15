'use strict';

let addCartBtn = $('.add-cart');
let cartNum = $('#cart-amount');

console.log(addCartBtn);


addCartBtn.on('click', function(){
    let prodId = this.dataset.product;
    let action = this.dataset.action;
    console.log('productID:', prodId, 'action: ', action);
    console.log(user)
    if(user !== "AnonymousUser"){
        updatingOrder(prodId, action);
    } else {
        console.log("User not logged in");
    }
})

function updatingOrder(prodId, action){
    console.log('User logged in')
    // Where we will send our data to
    let url = '/update_item/';

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            // Adding CSRF token because of POST method
            'X-CSRFToken': csrftoken,
        }, 
        // Sending prodId and Action as a string
        body:JSON.stringify({
            'prodId': prodId,
            'action': action})
    })

    .then((response)=> {
        // Turn into json value
        return response.json();
    }) 
    .then((data) => {
        console.log('data: ', data);
        // Reload data everytime it is updated
        location.reload();
    })
}