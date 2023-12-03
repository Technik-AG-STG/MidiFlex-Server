document.addEventListener('DOMContentLoaded', function() {
    var socket = io.connect('http://' + document.domain + ':' + location.port);

    socket.on('connect', function() {
        socket.emit('join_room', {room: '{{ current_user.id }}'});
    });

    socket.on('disconnect', function() {
        socket.emit('leave_room', {room: '{{ current_user.id }}'});
    });

    function sendButtonCommand(note, velocity) {
        socket.emit('button_click', {note: note, velocity: velocity, room: '{{ current_user.id }}'});
    }

    function sendSliderCommand(id, value) {
        socket.emit('fader_change', {id: id, value: value, room: '{{ current_user.id }}'});
    }
});