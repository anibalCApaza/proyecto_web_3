const contenedor_secundario = document.querySelector(".contenedor_secundario");
const footer=document.querySelector(".footer");

window.addEventListener("load", () => {
  if (sessionStorage.getItem("animacionVista")) {
    contenedor_secundario.style.display = "none";
    return;
  }
  document.querySelector(".logo").classList.add("activo");
  setTimeout(() => {
    contenedor_secundario.classList.add("invisible");
    setTimeout(() => {
      sessionStorage.setItem("animacionVista", "true"); // guardamos que ya la viste
    }, 1000);
  }, 3000);
});
if(window.location.pathname!='/proyecto/index/'){
    footer.classList.add("oculto");
}else{
    footer.classList.remove("oculto");
}
