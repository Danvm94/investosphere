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

        setTimeout(() => {
            element.classList.add('d-none');
        }, 1800);
    } else {

        setTimeout(() => {
            element.classList.remove('d-none');
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

function calculateCryptoAmount(event) {
    const value = event.target.value.replace(/,/g, ''); // User's input in USD
    const CryptoPrice = parseFloat(document.getElementById("price").getAttribute('data-price')); // Conversion rate (e.g., 0.00023)
    const CryptoAmount = document.getElementById("CryptoAmount");
    const Calculation = (value / CryptoPrice).toFixed(8); // Convert USD to cryptocurrency
    console.log(`${value}/${CryptoPrice} = ${Calculation}`)
    const result = Calculation.replace(/,/g, '');
    CryptoAmount.value = result
    console.log(result);
}

function initializeCryptoAmount() {
    const CryptoAmountInput = document.getElementById("USDAmount")
    if (CryptoAmountInput) {
        CryptoAmountInput.addEventListener("input", calculateCryptoAmount);
        console.log("here")
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
    const USDAmountInput = document.getElementById("USDAmount-Container")
    const CryptoAmountInput = document.getElementById("CryptoAmount-Container")
    try {
        const response = await fetch(`/get_price/?crypto=${selectedCrypto}`);
        const data = await response.json();
        const symbol = data.symbol.toUpperCase();
        const price = data.market_data.current_price.usd
        const priceInput = document.getElementById('price');
        priceInput.setAttribute('data-price', price)
        priceInput.textContent = `where 1 ${symbol} = USD $ ${price}`; // Update the UI with the fetched price
        opacityChange("show", USDAmountInput)
        opacityChange("show", CryptoAmountInput)
    } catch (error) {
        console.error("Error fetching crypto price:", error);
    }
}

document.addEventListener("DOMContentLoaded", function () {
    initializeNewsCarousel();
    initializeAmountInputFields();
    initializeCryptoChangeHandler();
    initializeCryptoAmount();
});

const successMessages = document.getElementsByClassName("alert-success");
fadeOutAndHideElementsAutomatically(successMessages, 8000, 2000);