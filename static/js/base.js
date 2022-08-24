const myModal = document.getElementById('exampleModal')
const myInput = document.getElementById('exampleModalLabel')

myModal.addEventListener('shown.bs.modal', () => {
  myInput.focus()
})



