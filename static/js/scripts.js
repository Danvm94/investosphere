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

document.addEventListener("DOMContentLoaded", function () {
  var newsCarouselElement = document.getElementById("newsCarousel");
  // Check if the newsCarousel element exists
  if (newsCarouselElement !== null) {
    var newsCarousel = new bootstrap.Carousel(newsCarouselElement, {
      interval: 3000, // Change slide every 3 seconds (adjust as needed)
      wrap: true, // Set to false if you don't want to loop
    });
  }

  const amountInputFields = document.getElementsByClassName("balance-modal");
  if (amountInputFields !== null) {
    for (const amountInputField of amountInputFields) {
      let inputBuffer = "0.00";

      amountInputField.addEventListener("input", function (event) {
        const value = event.target.value;

        // Remove non-digit characters from the input
        const digits = value.replace(/\D/g, "");

        // Convert the digits into a floating-point number
        const amount = parseFloat(digits) / 100;

        // If amount is NaN, set it to 0
        const sanitizedAmount = isNaN(amount) ? 0 : amount;

        // Format the number as currency with two decimal places
        const formattedAmount = sanitizedAmount.toLocaleString(undefined, {
          minimumFractionDigits: 2,
          maximumFractionDigits: 2,
        });

        // Update the input value
        event.target.value = formattedAmount;
      });
      // Handle form submission to convert the formatted value back to decimal before sending
      amountInputField.closest("form").addEventListener("submit", function () {
        const formattedValue = amountInputField.value;
        const decimalValue = parseFloat(
          formattedValue.replace(/[^0-9.-]/g, "")
        );
        amountInputField.value = decimalValue.toFixed(2); // Set the value back to decimal format
      });
    }
  }
});
