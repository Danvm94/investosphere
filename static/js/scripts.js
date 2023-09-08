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
    const CryptoAmountInput = document.getElementById("buy_dollars")
    if (CryptoAmountInput) {
        CryptoAmountInput.addEventListener("input", cryptoCalculator);
    }
}

function cryptoCalculator(event) {
    const usdAmount = document.getElementById(event.target.id + '_decimal').value
    const cryptoAmount = document.getElementById("buy_cryptos")
    const cryptoAmountDecimal = document.getElementById("buy_cryptos_decimal")
    const cryptoPrice = document.getElementById("crypto_price").value
    cryptoAmount.value = parseFloat(usdAmount) / parseFloat(cryptoPrice)
    cryptoAmountDecimal.value = parseFloat(usdAmount) / parseFloat(cryptoPrice)
}

// Function for usd amount calculation
function initializeUsdCalculator() {
    const CryptoAmountInput = document.getElementById("sell_cryptos")
    if (CryptoAmountInput) {
        CryptoAmountInput.addEventListener("input", usdCalculator);
    }
}

function usdCalculator(event) {
    const usdAmount = document.getElementById('sell_dollars')
    const usdAmountDecimal = document.getElementById('sell_dollars_decimal')
    const cryptoAmount = document.getElementById('sell_cryptos').value
    const cryptoAmountDecimal = document.getElementById('sell_cryptos_decimal').value
    const cryptoPrice = document.getElementById('sell-price').value
    usdAmount.value = (parseFloat(cryptoPrice) * parseFloat(cryptoAmount)).toLocaleString('en-US', {
        style: 'currency',
        currency: 'USD',
        minimumFractionDigits: 2
    });
    usdAmountDecimal.value = parseFloat(cryptoPrice) * parseFloat(cryptoAmount)
}

// Function to get crypto price
function initializeCryptoPriceRequest() {
    const buyCrypto = document.getElementById('id_crypto_select_buy');
    const sellCrypto = document.getElementById('id_crypto_select_sell');
    if (buyCrypto) {
        buyCrypto.addEventListener('change', cryptoPriceRequest);
        cryptoPriceRequest({target: buyCrypto});
    }
    if (sellCrypto) {
        sellCrypto.addEventListener('change', cryptoPriceRequest);
        cryptoPriceRequest({target: sellCrypto});
    }
}

async function cryptoPriceRequest(event) {
    const cryptoSelected = event.target.value;
    let cryptoPriceElement;
    let cryptoPriceTextElement;

    if (event.target.id === 'id_crypto_select_buy') {
        cryptoPriceElement = document.getElementById('crypto_price');
        cryptoPriceTextElement = document.getElementById('crypto-price-info-buy')
        document.getElementById('buy_dollars').value = '$.0'
        document.getElementById('buy_dollars_decimal').value = '0.00'
        document.getElementById('buy_cryptos').value = '0.00'
        document.getElementById('buy_cryptos_decimal').value = '0.00'

    } else if (event.target.id === 'id_crypto_select_sell') {
        cryptoPriceElement = document.getElementById('sell-price');
        cryptoPriceTextElement = document.getElementById('crypto-price-info-sell')
        document.getElementById('sell_dollars').value = '$.0'
        document.getElementById('sell_dollars_decimal').value = '0.00'
        document.getElementById('sell_cryptos').value = '0.00'
        document.getElementById('sell_cryptos_decimal').value = '0.00'
    }
    try {
        const response = await fetch(`/get_price/?crypto=${cryptoSelected}`);
        const data = await response.json();
        const symbol = data.symbol.toUpperCase();
        const price = data.current_price;
        cryptoPriceElement.value = price;
        cryptoPriceTextElement.textContent = `Where ${symbol} 1 = USD $${price}`
    } catch (error) {
        console.error("Error fetching crypto price:", error);
    }
}

// Function to show formatted USD on buy and sell
function initializeUsdFormatter() {
    const depositDollarForm = document.getElementById('deposit_dollars_form');
    const withdrawDollarForm = document.getElementById('withdraw_dollars_form');
    const buyCryptoForm = document.getElementById('buy_dollars')
    if (depositDollarForm) {
        depositDollarForm.addEventListener('input', usdFormatter);
    }
    if (withdrawDollarForm) {
        withdrawDollarForm.addEventListener('input', usdFormatter);
    }
    if (buyCryptoForm) {
        buyCryptoForm.addEventListener('input', usdFormatter)
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
    const decimalDollars = document.getElementById(inputElement.id + '_decimal');
    decimalDollars.value = unformattedInput

    // Update the input field with the formatted value
    inputElement.value = formattedInput;
}

// Function to toggleRow on a table
function toggleRow(button) {
    const hiddenRows = document.querySelectorAll('.d-none.hidden-row');
    if (hiddenRows) {
        for (let i = 0; i < Math.min(hiddenRows.length, 5); i++) {
            hiddenRows[i].classList.remove('d-none');
            hiddenRows[i].classList.remove('hidden-row');
        }
        const leftHiddenRows = document.querySelectorAll('.d-none.hidden-row');
        if (leftHiddenRows.length <= 0) {
            button.remove()
        }
    }
}

// Function to convert numbers to float
// Event Listener
document.addEventListener("DOMContentLoaded", function () {
    initializeNewsCarousel();
    initializeCryptoPriceRequest();
    initializeUsdFormatter();
    initializeCryptoCalculator();
    initializeUsdCalculator();

});

const successMessages = document.getElementsByClassName("alert-success");
fadeOutAndHideElementsAutomatically(successMessages, 8000, 2000);