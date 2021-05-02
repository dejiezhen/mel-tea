// 'use strict';

// Grabbing form fields and setting placeholders for each field in register page


const currHtml = window.location.pathname.split("/");
console.log("Current HTML Page " + currHtml[1]);
if (currHtml[1] == 'register'){
    let formFieldsRegis = $('#form-register input');
    let placeHolderRegis = ['Username', 
                            'Email', 
                            'Enter Password', 
                            'Re-enter Password'];
    for(let i = 0; i < placeHolderRegis.length; i++) {
        formFieldsRegis[i+1].placeholder = placeHolderRegis[i];
    }
}


// Setting placeholders for each field in log in page
if(currHtml[1] == 'login'){
    let formFieldsLogin = $('#form-login input');
    let placeHoldersLogin = ['Username', 'Password'];
    for(let i = 0; i < placeHoldersLogin.length; i++) {
        console.log("Running")
        formFieldsLogin[i+1].placeholder = placeHoldersLogin[i];
    }
}
