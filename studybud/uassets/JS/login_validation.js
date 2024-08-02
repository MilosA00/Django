var username = document.getElementById('username')
var password = document.getElementById("password")

var url = "http://127.0.0.1:8000/home"

function login_validation() {


}

async function fetchTodos() {
    const request = await fetch("http://127.0.0.1:8000/home").then(res => res.json())
    console.log(request)

}
