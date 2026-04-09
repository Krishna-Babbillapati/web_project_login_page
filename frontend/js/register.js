/**
 * Registration form handler
 * Validates registration data and calls the registration API
 */
async function handleRegister(event) {
    event.preventDefault();
    
    // Get form values
    const fullName = document.getElementById("full_name").value.trim();
    const email = document.getElementById("email").value.trim();
    const username = document.getElementById("username").value.trim();
    const password = document.getElementById("password").value;
    const rePassword = document.getElementById("re_password").value;
    const role = document.getElementById("admin").checked ? "admin" : "user";
    const city = document.getElementById("city").value.trim();
    const state = document.getElementById("state").value.trim();
    const country = document.getElementById("country").value.trim();
    
    // Get message element
    const message = document.getElementById("message");

    // Validation: Check if passwords match
    if (password !== rePassword) {
        message.textContent = "Passwords do not match!";
        message.className = "error";
        return;
    }

    // Validation: Check password requirements (same regex as login)
    const passwordRegex = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$/;
    if (!passwordRegex.test(password)) {
        message.textContent = "Password must be at least 8 characters, include uppercase, lowercase, number, and special character (@$!%*?&)";
        message.className = "error";
        return;
    }
    
    // Validation: Check required fields
    if (!fullName || !email || !username || !city || !state || !country || !password || !role || !rePassword) {
        message.textContent = "All fields are required!";
        message.className = "error";
        return;
    }
    
    // Call registration API
    try {
        const response = await fetch("/admin/register", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ username: username, password: password, role: role })
        });
        
        const data = await response.json();
        console.log("Registration response:", data);
        
        if (data.success) {
            message.textContent = "Registration successful! Redirecting to login...";
            message.className = "success";
            // Redirect to login page after 2 seconds
            setTimeout(() => {
                window.location.href = "login.html";
            }, 2000);
        } else {
            message.textContent = "Registration failed: " + data.message;
            message.className = "error";
        }
    } catch (error) {
        console.error("Error:", error);
        message.textContent = "Network or server error";
        message.className = "error";
    }
}
