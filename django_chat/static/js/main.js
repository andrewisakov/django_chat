document.querySelector('li.room-link').onclick = function(e) {
    var roomName = e.attr('data-room-id');
    window.location.pathname = '/chat/' + roomName + '/';
};
