// Custom JavaScript code here
console.log("Main JS loaded.");



document.getElementById("registrationForm").addEventListener("submit", function(event)
{
    event.preventDefault();
    var username = document.getElementById("username").value;
    var email = document.getElementById("email").value;
    var password = document.getElementById("password").value;
    // You can perform further validation or send the form data to a server here
    console.log("Username: " + username);
    console.log("Email: " + email);
    console.log("Password: " + password);
    alert("Registration successful!");
  });
// you can also save user name on chrome storage