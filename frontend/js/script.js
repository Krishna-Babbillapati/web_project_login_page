async function getLoginCreds(event) {
    event.preventDefault();
    var username = document.getElementById("username").value;
    var password = document.getElementById("password").value;

    try {
        const response = await fetch("/login", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ username: username, password: password })
        });

        const data = await response.json();
        console.log("Response:", data);

        if (data.success) {
            alert("Login successful!");
            window.open("pages/login.html", "_blank");
        } else {
            alert("Login failed: " + data.message);
        }
    } catch (error) {
        console.error("Error:", error);
        alert("Network or server error");
    }
}