// main.js

var sio = io();

 function sendButtonCommand(note, velocity) {
     // Function to send button click command to the server
     sio.emit('button_click', {'note': note, 'velocity': velocity});
}

function sendSliderCommand(id, value) {
    // Function to send slider change command to the server
    sio.emit('fader_change', {'id': id, 'value': value});
}
