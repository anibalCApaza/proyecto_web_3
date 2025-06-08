// Campos de formulario
const nombre = document.forms[0][1];
const apellido = document.forms[0][2];
const usuario = document.forms[0][3];
const email = document.forms[0][4];
const contrasenia1 = document.forms[0][5];
const contrasenia2 = document.forms[0][6];
const campos = [nombre, apellido, usuario]
const contrasenias = [contrasenia1, contrasenia2]
contrasenia2.disabled = true;
// Validacion del formulario
function validarCamposTexto() {
    return campos.every(campo => campo.value.trim() !== "");
}

function validarEmail() {
    const regexCorreo = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return regexCorreo.test(email.value.trim());
}

function validarContrasenia1() {
    return contrasenia1.value.trim().length >= 8;
}

function validarContrasenia2() {
    return (
        contrasenia2.value.trim().length >= 8 &&
        contrasenia2.value === contrasenia1.value
    );
}
campos.forEach(x => {
    x.addEventListener("blur", (e) => {
        
    })
})
email.addEventListener("blur", () => {
})
contrasenia1.addEventListener("blur", () => {
    if (validarContrasenia1()) {
        contrasenia2.disabled = false;
    } else {
        contrasenia2.disabled = true;
    }
});
contrasenia2.addEventListener('blur', () => {
})
document.forms[0].addEventListener("submit", (e) => {
    let validado=validarCamposTexto() &&
        validarEmail() &&
        validarContrasenia1() &&
        validarContrasenia2();
    if (!validado) {
        e.preventDefault();
        console.log("No se pudo enviar el formulario");
    }
})
