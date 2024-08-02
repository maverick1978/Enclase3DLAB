function createUser() {
    const form = document.getElementById('create-user-form');
    const formData = new FormData(form);
    fetch('/create_user', {
        method: 'POST',
        body: formData
    }).then(response => {
        if (response.ok) {
            alert('Usuario creado exitosamente');
            location.reload();
        } else {
            alert('Error al crear usuario');
        }
    });
}

function createClass() {
    const form = document.getElementById('create-class-form');
    const formData = new FormData(form);
    fetch('/create_class', {
        method: 'POST',
        body: formData
    }).then(response => {
        if (response.ok) {
            alert('Clase creada exitosamente');
            location.reload();
        } else {
            alert('Error al crear clase');
        }
    });
}

function openClassModal(classId) {
    // Implement class editing logic
}
