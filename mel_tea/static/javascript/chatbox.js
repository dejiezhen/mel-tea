const chatSocket = new WebSocket(
    'ws://'
    + window.location.host
    + '/ws/chat'
);

chatSocket.onmessage = function(e) {
    const data = JSON.parse(e.data);
    document.querySelector('#main-chat').value += (data.message + '\n');
};

chatSocket.onclose = function(e) {
    console.error('Chat socket closed unexpectedly');
};

document.querySelector('#user-message').focus();
document.querySelector('#user-message').onkeyup = function(e) {
    if (e.keyCode === 13) {  // enter, return
        document.querySelector('#send-button').click();
    }
};


let currUser = $(".currentUser").text();
document.querySelector('#send-button').onclick = function(e) {
    const messageInputDom = document.querySelector('#user-message');
    const message = currUser + ": " + messageInputDom.value;
    chatSocket.send(JSON.stringify({
        'message': message
    }));
    messageInputDom.value = '';
};
