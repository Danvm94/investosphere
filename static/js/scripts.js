function allowOnlyLetters(inputElement) {
  inputElement.value = inputElement.value.replace(/[^a-zA-Z]/g, "");
}

var successMessages = document.getElementsByClassName("alert-success");

// Set the timeout to remove the div after 5 seconds (5000 milliseconds)
setTimeout(function () {
  for (var i = 0; i < successMessages.length; i++) {
    successMessages[i].style.opacity = "0"; // Fade out animation
  }
}, 8000); // Start fading after 800ms

setTimeout(function () {
  for (var i = 0; i < successMessages.length; i++) {
    successMessages[i].style.display = "none"; // Hide completely after animation
  }
}, 10000); // Hide completely after 10 seconds

function opacityChange(type, element) {
  if (type === "hide") {
    element.style.opacity = "0";
    setTimeout(() => {
      element.style.display = "none";
    }, 1800);
  } else {
    element.style.display = "flex";
    setTimeout(() => {
      element.style.opacity = "1";
    }, 50);
  }
}

var myCarousel = new bootstrap.Carousel(document.getElementById("myCarousel"), {
  interval: 3000, // Change slide every 3 seconds (adjust as needed)
  wrap: true, // Set to false if you don't want to loop
});
