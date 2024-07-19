const username = document.querySelector('#username').value
const password = document.getElementById("password")
const form = document.querySelector("#loginForm")
form.addEventListener("submit", async (e) => {
    e.preventDefault()
    await fetchTodos()
})
const url = "http://127.0.0.1:8000/home"

async function fetchTodos() {
    const request = await fetch("http://127.0.0.1:8000/home")
    const todos = await request.json()
    console.log(todos[0])
    console.log(username)
    console.log(password)

}

function outOfFocus() {
    let usrName = username.value
    if (usrName == null) {
        console.log("Username out of focus")
    }
}
