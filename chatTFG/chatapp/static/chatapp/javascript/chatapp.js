var miDiv = document.getElementById("chat-log"); 
function pauseDiv() {
    miDiv='';
}

function resumeDiv() {
    miDiv = document.getElementById("chat-log");
}
setInterval(function scrollDiv() {    
    miDiv.scrollTop = miDiv.scrollHeight - miDiv.clientHeight;
},200);

const roomName = JSON.parse(document.getElementById('room-name').textContent);

const chatSocket = new WebSocket(
    'ws://'
    + window.location.host
    + '/ws/chat/'
    + roomName
    + '/'
);

chatSocket.onmessage = function(e) {
    const data = JSON.parse(e.data);
    document.getElementById('chat-log').innerHTML += ('<p>'+data.nameUser + ': ' + data.message + '<p/>');
};

chatSocket.onclose = function(e) {
    console.error('Chat socket closed unexpectedly');
};

document.getElementById('chat-message-input').focus();
document.getElementById('chat-message-input').onkeyup = function(e) {
    if (e.keyCode === 13) {  // enter, return
        document.getElementById('chat-message-submit').click();
    }
};

document.getElementById('chat-message-submit').onclick = function(e) {
    const messageInputDom = document.getElementById('chat-message-input');
    const message = messageInputDom.value;
    if(message!=''){
        chatSocket.send(JSON.stringify({
            'message': message,
        }));

    messageInputDom.value = '';
    }
    else{
        messageInputDom.style = "background-color: red;";
        setTimeout(function() {
            messageInputDom.style = "";
        }, 300);
    }
};


