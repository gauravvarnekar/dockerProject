// JavaScript code to change the text when button is clicked
document.getElementById("changeTextBtn").addEventListener("click", function() {
    alert("You clicked the button! The text will change now.");
    document.querySelector("main h2").textContent = "Text has been changed!";
});

