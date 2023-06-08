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
const roomUser = JSON.parse(document.getElementById('room-user').textContent);

const chatSocket = new WebSocket(
    'ws://'
    + window.location.host
    + '/ws/chat/'
    + roomName
    + '/'
);

chatSocket.onmessage = function(e) {
    const data = JSON.parse(e.data);

    msgpropio="<div class='card text-white border border-dark' style='width: 15%;margin-left: auto;margin-top: 10px;margin-bottom:10px;'>"+
    "<div class='card-header border border-dark fuentenegrita' style='background-color: rgb(208, 0, 210);text-align:right;'>"+
    data.nameUser+"</div><div class='card-body gradient fuente'>"+
    "<p style='text-align:right;'>"+data.message+"<p></div></div>"


    otromsg="<div class='card text-white border border-dark' style='width: 15%;margin-top: 10px;margin-bottom:10px;'>"+
    "<div class='card-header border border-dark fuentenegrita' style='background-color: rgb(0, 0, 0)'>"+
    data.nameUser+"</div><div class='card-body gradient2 fuente'>"+
    "<p style='text-align:left;'>"+data.message+"<p></div></div>"

    if(data.message){
        if (data.nameUser == roomUser){
            document.getElementById('chat-log').innerHTML += msgpropio;
        }
        else{
            document.getElementById('chat-log').innerHTML += otromsg;
        }
        scrollDiv();
    }
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


