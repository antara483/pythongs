const BASE_URL = "http://127.0.0.1:5000";

async function login() {
    const username = document.getElementById("login-username").value;
    const password = document.getElementById("login-password").value;

    const response = await fetch(`${BASE_URL}/login`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ username, password })
    });

    const result = await response.json();
    alert(result.message);

    if (response.status === 200) {
        window.location.href = "index.html"; // Redirect after successful login
    }
}

async function signup() {
    const username = document.getElementById("signup-username").value;
    const password = document.getElementById("signup-password").value;

    const response = await fetch(`${BASE_URL}/signup`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ username, password })
    });

    const result = await response.json();
    alert(result.message);

    if (response.status === 201) {
        window.location.href = "login.html"; // Redirect after successful signup
    }
}

// DO NOT wrap this in an IIFE or module unless you export it
async function logout() {
    const response = await fetch(`${BASE_URL}/logout`, {
        method: "POST",
        credentials: "include"
    });

    const result = await response.json();
    alert(result.message);
    if (response.status === 200) {
        window.location.href = "login.html";
    }
}

