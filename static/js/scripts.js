// Function for only letters in the input
function allowOnlyLetters(inputElement) {
    inputElement.value = inputElement.value.replace(/[^a-zA-Z]/g, "");
}

// Function to hide elements
function fadeOutAndHideElementsAutomatically(elements, fadeDelay, hideDelay) {
    setTimeout(function () {
        for (let i = 0; i < elements.length; i++) {
            elements[i].style.opacity = "0"; // Fade out animation
        }

        setTimeout(function () {
            for (let i = 0; i < elements.length; i++) {
                elements[i].style.display = "none"; // Hide completely after animation
            }
        }, hideDelay); // Hide completely after specified delay
    }, fadeDelay); // Start fading after specified delay
}

// Function for opacity change
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

function initializeNewsCarousel() {
    const newsCarouselElement = document.getElementById("newsCarousel");
    if (newsCarouselElement) {
        new bootstrap.Carousel(newsCarouselElement, {
            interval: 3000, // Change slide every 3 seconds (adjust as needed)
            wrap: true, // Set to false if you don't want to loop
        });
    }
}

function initializeAmountInputFields() {
    const amountInputFields = document.getElementsByClassName("balance-modal");
    for (const amountInputField of amountInputFields) {
        amountInputField.addEventListener("input", handleAmountInput);
        amountInputField.closest("form").addEventListener("submit", handleAmountSubmit);
    }
}

function handleAmountInput(event) {
    const value = event.target.value;
    const digits = value.replace(/\D/g, "");
    const amount = parseFloat(digits) / 100;
    const sanitizedAmount = isNaN(amount) ? 0 : amount;
    const formattedAmount = sanitizedAmount.toLocaleString(undefined, {
        minimumFractionDigits: 2,
        maximumFractionDigits: 2,
    });
    event.target.value = formattedAmount;
}

function handleAmountSubmit(event) {
    const amountInputField = event.target.querySelector(".balance-modal");
    const formattedValue = amountInputField.value;
    const decimalValue = parseFloat(formattedValue.replace(/[^0-9.-]/g, ""));
    amountInputField.value = decimalValue.toFixed(2); // Set the value back to decimal format
}

function initializeCryptoChangeHandler() {
    const cryptoSelect = document.getElementById('crypto');
    if (cryptoSelect) {
        cryptoSelect.addEventListener('change', handleCryptoChange);
    }
}

async function handleCryptoChange() {
    const selectedCrypto = this.value;
    try {
        const response = await fetch(`/get_price/?crypto=${selectedCrypto}`);
        const data = await response.json();
        const priceInput = document.getElementById('price');
        priceInput.textContent = data.id; // Update the UI with the fetched price
    } catch (error) {
        console.error("Error fetching crypto price:", error);
    }
}

document.addEventListener("DOMContentLoaded", function () {
    initializeNewsCarousel();
    initializeAmountInputFields();
    initializeCryptoChangeHandler();
});

const successMessages = document.getElementsByClassName("alert-success");
fadeOutAndHideElementsAutomatically(successMessages, 8000, 2000);