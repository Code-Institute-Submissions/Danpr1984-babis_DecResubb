const myModal = document.getElementById('exampleModal')
const myInput = document.getElementById('exampleModalLabel')

myModal.addEventListener('shown.bs.modal', () => {
  myInput.focus()
})

const postModal = document.getElementById('postModal')
const postInput = document.getElementById('postModalLabel')

postModal.addEventListener('shown.bs.modal', () => {
  postInput.focus()
})