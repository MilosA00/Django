const username = document.querySelector('#username');
const password = document.getElementById("password");


const form = document.querySelector("#loginForm")
form.addEventListener("submit", async (e) => {
    e.preventDefault()
    await fetchTodos()
})
const url = "http://127.0.0.1:8000/home"

async function fetchTodos() {


    const data = new FormData();
    data.append('username', username.value)
    data.append('password', password.value)

    try {
        const response = await fetch('http://127.0.0.1:8000/user/login', {
            method: "post",
            body: data
        })
        const parsedResponse = await response.json()
        console.log(parsedResponse)
        if (parsedResponse.status === true) {
            window.location.replace("http://127.0.0.1:8000/home")
        }

    } catch (error) {
        console.error(error)
    }

}

function isEmpty(str) {
    return str.length;
}

function outOfFocusUsr() {
    const usrName = isEmpty(username.value)

    const validationMsg = document.querySelector(".usernameValidation")

    if (usrName === 0) {
        validationMsg.classList.add("displayMsg")

    } else {
        validationMsg.classList.remove("displayMsg")
    }


}

function outOfFocusPass() {
    const usrPass = isEmpty(password.value)
    const passValidationMsg = document.querySelector(".passwordValidation")
    if (usrPass === 0) {
        passValidationMsg.classList.add("displayMsg")
    } else {
        passValidationMsg.classList.remove("displayMsg")
    }
}