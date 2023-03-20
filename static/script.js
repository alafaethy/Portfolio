// Abre e fecha menu mobile


const menuMobile = document.querySelector(".menu-mobile");
const body = document.querySelector("body");


menuMobile.addEventListener("click", () => {
    menuMobile.classList.contains('bi-list')
    ? menuMobile.classList.replace("bi-list","bi-x")
    : menuMobile.classList.replace("bi-x","bi-list")
    body.classList.toggle("menu-nav-active")
})


// Fechar o menu clicar em algum item e mudar o icone 


const navItem = document.querySelectorAll(".nav-item")
navItem.forEach(item =>{
    item.addEventListener("click", () => {
        if (body.classList.contains("menu-nav-active")) {
            body.classList.remove("menu-nav-active")
            menuMobile.classList.replace("bi-x","bi-list")
        }
    })
})

// Animar todos itens da tela com atributo data-anime

const item = document.querySelectorAll("[data-anime]")
const animeScroll = ()=>{
    const windowTop = window.pageYOffset + window.innerHeight * 0.80
    item.forEach((element) => {
        if(windowTop > element.offsetTop) {
            element.classList.add("animate")
        }else{
            element.classList.remove("animate")
        }
    })
}
animeScroll()
window.addEventListener("scroll", ()=>{
    animeScroll()
})


// Ativar o botao de carregamento 

const btnEnviar = document.querySelector("#btn-enviar")
const btnLoader = document.querySelector("#btn-loader")

btnEnviar.addEventListener("click", ()=>{
    btnLoader.style.display = "block"
    btnEnviar.style.display = "none"
})