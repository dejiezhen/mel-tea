function grabCookie(name) {
    let cookieArray = document.cookie.split(";");

    for(let i = 0; i < cookieArray.length; i++){
        let cookiePair = cookieArray[i].split("=")
        if(name = cookiePair[0].trim()){ //Compare name to cookie with white space removed
            return decodeURIComponent(cookiePair[1]); //Decoding the cookie value and return
        }
    }

    //if no cookies are found, return null
    return null
}
let cart = JSON.parse(getCookie('cart'))

// If we don't have that cookie 
if (!cart){
    cart = {};
    console.log("A cart has be created for the guest user", cart);
    document.cookie = 'cart=' + JSON.stringify(cart) + ";domain=;path=/";
}

console.log("Cart: ", cart);

