const URL = "http://127.0.0.1:8000/";

const email = document.querySelector(".email");
const password = document.querySelector(".password");

const handleSign = async (email, password, URI) => {
  const body = { email, password };

  try {
    const response = await fetch(URL + URI, {
      method: "POST",
      body: JSON.stringify(body),
      headers: {
        "Content-Type": "application/json",
      },
    });
    if (!response.ok) {
      throw Error("failed to post");
    }

    const data = await response.json();
    localStorage.setItem("auth", JSON.stringify(data));
    if (URI === "auth/login/") window.location.pathname = "/";
  } catch (e) {
    console.log(e.message);
  }
};

if (window.location.pathname === "/auth/signup/") {
  const signUp = document.querySelector(".up");

  signUp.addEventListener("click", signUpUser);

  function signUpUser() {
    if (email.value === "") {
      console.log("email is required");
    } else if (!/^\w+([.-]?\w+)@\w+([.-]?\w+)(.\w{2,3})+$/.test(email.value)) {
      console.log("invalid email");
    } else if (password.length < 8) {
      console.log("password must be at least 8 characters long");
    } else if (email.value && password.value) {
      handleSign(email.value, password.value, "auth/register/");
      handleSign(email.value, password.value, "auth/login/");
    }
  }
} else if (window.location.pathname === "/auth/signin/") {
  const signIn = document.querySelector(".in");

  signIn.addEventListener("click", signInUser);

  function signInUser() {
    if (email.value === "") {
      console.log("email is required");
    } else if (!/^\w+([.-]?\w+)@\w+([.-]?\w+)(.\w{2,3})+$/.test(email.value)) {
      console.log("invalid email");
    } else if (password.length < 8) {
      console.log("password must be at least 8 characters long");
    } else if (email.value && password.value) {
      handleSign(email.value, password.value, "auth/login/");
    }
  }
}
