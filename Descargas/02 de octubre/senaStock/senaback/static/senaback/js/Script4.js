
//--------------------------- Editar Elemento---------------------------------------------------------

const btnGuardarEditar = document.getElementById("btn-guardar-editar");
const btnCancelarEditar = document.getElementById("btn-no-guardar-editar");

// Obtén una referencia al formulario de editar elemento
const formularioEditarElemento = document.getElementById("formulario-editar-elemento-link");

// Función para cerrar el formulario emergente
function cerrarFormularioEditar() {
    document.getElementById("formulario-editar-elemento").style.display = "none";
}

// Agrega un evento de clic al botón "Cancelar" para cerrar el formulario
btnCancelarEditar.addEventListener("click", cerrarFormularioEditar);

// Agrega un evento de clic al botón "Guardar" para cerrar el formulario
btnGuardarEditar.addEventListener("click", cerrarFormularioEditar);



document.getElementById("formulario-editar-elemento-link").addEventListener("click", () => {
    document.getElementById("formulario-editar-elemento").style.display = "flex";
    
});

document.addEventListener("DOMContentLoaded", function () {
    const formEditarElemento = document.getElementById("formulario-editar-elemento");

    // Función para abrir el formulario de editar elemento
    function abrirFormularioEditar() {
        formEditarElemento.style.display = "flex";
    }

    // Agregar eventos de clic a los enlaces correspondientes
    const enlacesEditarElemento = document.querySelectorAll("[data-formulario='editar-elemento']");

    enlacesEditarElemento.forEach(function (enlace) {
        enlace.addEventListener("click", function (e) {
            e.preventDefault();
            abrirFormularioEditar();
        });
    });

//-------------------------------------------------------------------------------------------


//------------------------ Crear elemento -------------------------------------------------------


const btnGuardarCrear = document.getElementById("btn-guardar-crear");
const btnCancelarCrear = document.getElementById("btn-no-guardar-crear");

const formularioCrearElemento = document.getElementById("formulario-crear-elemento");

function abrirFormularioCrear() {
    document.getElementById("formulario-crear-elemento").style.display = "flex";
}
document.getElementById("formulario-crear-elemento-link").addEventListener("click", abrirFormularioCrear);


function cerrarFormularioCrear() {
    document.getElementById("formulario-crear-elemento").style.display = "none";
}

btnCancelarCrear.addEventListener("click", cerrarFormularioCrear);

btnGuardarCrear.addEventListener("click", cerrarFormularioCrear);

document.getElementById("formulario-crear-elemento-link").addEventListener("click", () => {
    document.getElementById("formulario-crear-elemento").style.display = "flex";
});

//------------------------ Otorgar Elemento ----------------------------------------

const btnGuardarOtorgar = document.getElementById("btn-guardar-otorgar");
const btnCancelarOtorgar = document.getElementById("btn-no-guardar-otorgar");

const formularioOtorgarElemento = document.getElementById("formulario-otorgar-elemento");



function cerrarFormularioOtorgar() {
    formularioOtorgarElemento.style.display = "none";
}

btnCancelarOtorgar.addEventListener("click", cerrarFormularioOtorgar);

btnGuardarOtorgar.addEventListener("click", cerrarFormularioOtorgar);

document.getElementById("formulario-otorgar-elemento-link").addEventListener("click", () => {
    document.getElementById("formulario-otorgar-elemento").style.display = "flex";
});
})

//-------------------------- Finalizar Prestamo Elemento ------------------------------------------