// Campos de formulario
const nombre = document.forms[0][1];
const password = document.forms[0][2];

function validarPassword() {
    return nombre.value.trim().length >= 1;
}
function validarPassword() {
    return password.value.trim().length >= 8;
}
document.forms[0].addEventListener("submit", (e) => {
    let validado=validarCampoTexto() &&
        validarPassword();
    if (!validado) {
        e.preventDefault();
        console.log("No se pudo enviar el formulario");
    }
})