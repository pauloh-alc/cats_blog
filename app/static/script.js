document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('olho').addEventListener('mouseup', function() {
        document.getElementById('pass').type = 'password';
    });

    document.getElementById('olho').addEventListener('mousedown', function() {
        document.getElementById('pass').type = 'text';
    });

    // Para que o password não fique exposto após mover a imagem.
    document.getElementById('olho').addEventListener('mousemove', function() {
        document.getElementById('pass').type = 'password';
    });
});
