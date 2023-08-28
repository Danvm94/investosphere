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

// Function for carousel on bootstrap
function initializeNewsCarousel() {
    const newsCarouselElement = document.getElementById("newsCarousel");
    if (newsCarouselElement) {
        new bootstrap.Carousel(newsCarouselElement, {
            interval: 3000, // Change slide every 3 seconds (adjust as needed)
            wrap: true, // Set to false if you don't want to loop
        });
    }
}

// Function for crypto amount calculation
function initializeCryptoCalculator() {
    const CryptoAmountInput = document.getElementById("id_usd_amount")
    if (CryptoAmountInput) {
        CryptoAmountInput.addEventListener("input", cryptoCalculator);
    }
}

function cryptoCalculator(event) {
    const usdAmount = event.target.value
    const cryptoAmount = document.getElementById("id_crypto_amount")
    const cryptoPrice = document.getElementById("price").getAttribute('data-price')
    cryptoAmount.value = usdAmount / cryptoPrice
}

// Function to get crypto price
function initializeCryptoPriceRequest() {
    const cryptoSelect = document.getElementById('id_crypto');
    if (cryptoSelect) {
        cryptoSelect.addEventListener('change', cryptoPriceRequest);
    }
}

async function cryptoPriceRequest() {
    const cryptoSelected = this.value
    const usdDiv = document.getElementById('usd-div')
    const cryptoDiv = document.getElementById('crypto-div')
    try {
        const response = await fetch(`/get_price/?crypto=${cryptoSelected}`)
        const data = await response.json()
        const symbol = data.symbol.toUpperCase()
        const price = data.market_data.current_price.usd;
        const priceText = document.getElementById('price');
        priceText.setAttribute('data-price', price)
        priceText.textContent = `where 1 ${symbol} = USD$ ${price}`;
        opacityChange("show", usdDiv)
        opacityChange("show", cryptoDiv)
    } catch (error) {
        console.error("Error fetching crypto price:", error);
    }
}

// Function to convert numbers to float
// Event Listener
document.addEventListener("DOMContentLoaded", function () {
    initializeNewsCarousel();
    initializeCryptoPriceRequest();
    initializeCryptoCalculator();

});

const successMessages = document.getElementsByClassName("alert-success");
fadeOutAndHideElementsAutomatically(successMessages, 8000, 2000);