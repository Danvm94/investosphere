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

// Function for usd amount calculation
function initializeUsdCalculator() {
    const CryptoAmountInput = document.getElementById("id_usd_amount_sell")
    if (CryptoAmountInput) {
        CryptoAmountInput.addEventListener("input", usdCalculator);
    }
}

function usdCalculator(event) {
    const usdAmount = event.target.value
    const cryptoAmount = document.getElementById("id_crypto_amount")
    const cryptoPrice = document.getElementById("price").getAttribute('data-price')
    cryptoAmount.value = usdAmount / cryptoPrice
}

// Function to get crypto price
function initializeCryptoPriceRequest() {
    const buyCrypto = document.getElementById('id_buy_crypto');
    const sellCrypto = document.getElementById('id_sell_crypto');
    if (buyCrypto) {
        buyCrypto.addEventListener('change', cryptoPriceRequest);
    }
    if (sellCrypto) {
        sellCrypto.addEventListener('change', cryptoPriceRequest);
    }
}

async function cryptoPriceRequest() {
    const cryptoSelected = this.value
    let hiddenDivs;
    let priceText;
    if (this.id === 'id_buy_crypto') {
        hiddenDivs = document.getElementsByClassName('buy-modal-price')
        priceText = document.getElementById('buy-price');
    } else if (this.id === 'id_sell_crypto') {
        hiddenDivs = document.getElementsByClassName('sell-modal-price')
        priceText = document.getElementById('sell-price');
    }
    try {
        const response = await fetch(`/get_price/?crypto=${cryptoSelected}`)
        const data = await response.json()
        const symbol = data.symbol.toUpperCase()
        const price = data.market_data.current_price.usd;
        priceText.setAttribute('data-price', price)
        priceText.textContent = `where 1 ${symbol} = USD$ ${price}`;
        for (const hiddenDiv of hiddenDivs) {
            opacityChange('show', hiddenDiv);
        }
    } catch (error) {
        console.error("Error fetching crypto price:", error);
    }

}

// Function to show formatted USD on buy and sell
function initializeUsdFormatter() {
    const depositDollarForm = document.getElementById('deposit_dollars_form_text');
    if (depositDollarForm) {
        depositDollarForm.addEventListener('input', usdFormatter);
    }
}

function usdFormatter(event) {
    const inputElement = event.target;
    const inputValue = inputElement.value;

    // Remove non-numeric characters and leading zeros
    const numericValue = inputValue.replace(/[^0-9]/g, '').replace(/^0+/, '');

    // If the value is empty, set it to 0
    const formattedValue = numericValue.length === 0 ? '0' : numericValue;

    // Split the numeric value into integer and decimal parts
    const decimalPart = (formattedValue.length > 2) ? formattedValue.slice(-2) : formattedValue;
    const integerPart = formattedValue.slice(0, -2);
    // Format the integer part with commas
    const formattedIntegerPart = integerPart.replace(/\B(?=(\d{3})+(?!\d))/g, ',');

    // Combine the formatted integer and decimal parts with a decimal point
    const formattedInput = '$' + formattedIntegerPart + '.' + decimalPart;
    const unformattedInput = integerPart + '.' + decimalPart
    const decimalDollars = document.getElementById('deposit_dollars_form_decimal');
    decimalDollars.value = unformattedInput

    // Update the input field with the formatted value
    inputElement.value = formattedInput;
}

// Function to convert numbers to float
// Event Listener
document.addEventListener("DOMContentLoaded", function () {
    initializeNewsCarousel();
    initializeCryptoPriceRequest();
    initializeCryptoCalculator();
    initializeUsdCalculator();
    initializeUsdFormatter();

});

const successMessages = document.getElementsByClassName("alert-success");
fadeOutAndHideElementsAutomatically(successMessages, 8000, 2000);