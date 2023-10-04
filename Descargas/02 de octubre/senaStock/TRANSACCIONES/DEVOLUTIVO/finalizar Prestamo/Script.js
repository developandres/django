const showModalBtn = document.getElementById("show-modal-btn");
const modal = document.getElementById("modal");
const closeModal = document.getElementById("btn-no-guardar");
const closeModal1 = document.getElementById("btn-guardar");


showModalBtn.addEventListener("click", () => {
  modal.style.display = "block";
});

closeModal.addEventListener("click", () => {
  modal.style.display = "none";
});
closeModal1.addEventListener("click", () => {
  modal.style.display = "none";
});

window.addEventListener("click", (event) => {
  if (event.target === modal) {
    modal.style.display = "none";
  }
});
function sumar(a, b){
  console.log(a +b)
}

sumar(4,5)