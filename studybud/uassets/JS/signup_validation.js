const username = document.querySelector(".username")
const email = document.querySelector(".email")
const password = document.querySelector(".password")


const form = document.querySelector("#signUpForm")
form.addEventListener("submit", async (e) => {
    e.preventDefault()
    await signUpRequest()
})


async function signUpRequest() {

    const data = new FormData();
    data.append('user_name', username.value)
    data.append('email', email.value)
    data.append('password', password.value)

    try {
        const response = await fetch('http://127.0.0.1:8000/user/signup', {
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


function outOfFocusUsr() {
    const usrName = isEmpty(username.value)

    const validationMsg = document.querySelector(".usernameValidation")

    if (usrName === 0) {
        validationMsg.classList.add("displayMsg")

    } else {
        validationMsg.classList.remove("displayMsg")
    }
}


function isEmpty(str) {
    return str.length;
}

function outOfFocusEmail() {
    const usrEmail = isEmpty(email.value)
    const passValidationMsg = document.querySelector(".emailValidation")
    if (usrEmail === 0) {
        passValidationMsg.classList.add("displayMsg")
    } else {
        passValidationMsg.classList.remove("displayMsg")
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