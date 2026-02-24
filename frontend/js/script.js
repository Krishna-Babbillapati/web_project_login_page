async function getLoginCreds(event) {
    event.preventDefault();
    var username = document.getElementById("username").value;
    var password = document.getElementById("password").value;
    var message = document.getElementById("message");

    // Regex: At least 8 chars, one uppercase, one lowercase, one number, one special char
    const regex = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$/;

    if (regex.test(password)) {
        // proceed with login logic here
        try {
            const response = await fetch("/login", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ username: username, password: password })
            });

            const data = await response.json();
            console.log("Response:", data);

            if (data.success) {
                message.textContent = "Login successful!";
                message.className = "success";
                window.open("pages/login.html", "_blank");
            } else {
                message.textContent = "Login failed: " + data.message;
            }
        } catch (error) {
                console.error("Error:", error);
                message.textContent = "Network or server error";
        }
    } else {
        message.textContent = "Password must be at least 8 characters long, include uppercase, lowercase, number, and special character.";
        message.className = "error";
    }
}