'use strict';

let addCartBtn = $('.add-cart');
let cartNum = $('#cart-amount');

console.log(addCartBtn);

function addingCookieItems(productID, action){
    if(action == 'add'){
        !cart[productID]? cart[productID] = {'quantity': 1}: cart[productID]['quantity'] ++;
    }

    if(action == 'remove'){
        cart[productID]['quantity']--;
        if(cart[productID]['quantity'] <= 0){
            delete cart[productID]
        }
    }
    console.log(cart)
    document.cookie = 'cart=' + JSON.stringify(cart) + ";domain=;path=/"
    location.reload() //reload website
}


addCartBtn.on('click', function(){
    let prodId = this.dataset.product;
    let action = this.dataset.action;
    console.log('productID:', prodId, 'action: ', action);
    console.log(user)
    if(user !== "AnonymousUser"){
        updatingOrder(prodId, action);
    } else {
        console.log("User not logged in");
        addingCookieItems(prodId, action)
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