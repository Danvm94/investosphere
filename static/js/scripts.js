/*jshint esversion: 8 */

/* global bootstrap */
/**
 * Allows only letters (A-Z, a-z) in the input element's value.
 * Replaces any non-letter characters with an empty string.
 *
 * @param {HTMLInputElement} inputElement - The input element to process.
 */
function allowOnlyLetters(inputElement) {
    inputElement.value = inputElement.value.replace(/[^a-zA-Z]/g, "");
}

/**
 * Automatically fades out and hides a list of HTML elements with a delay.
 *
 * @param {Array} elements - An array of HTML elements to fade out and hide.
 * @param {number} fadeDelay - The delay (in milliseconds) before starting the fade-out animation.
 * @param {number} hideDelay - The delay (in milliseconds) before hiding the elements completely after fading.
 */
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

/**
 * Change the opacity of an HTML element for show or hide effects.
 *
 * @param {string} type - The type of operation, either "hide" or "show".
 * @param {HTMLElement} element - The HTML element to apply the opacity change to.
 */
function opacityChange(type, element) {
    if (type === "hide") {
        // If type is "hide", set a timeout to add the 'd-none' class for hiding.
        setTimeout(() => {
            element.classList.add('d-none');
        }, 1800); // Delay before hiding: 1800 milliseconds (1.8 seconds)
    } else {
        // If type is "show", set a timeout to remove the 'd-none' class for showing.
        setTimeout(() => {
            element.classList.remove('d-none');
        }, 50); // Delay before showing: 50 milliseconds (0.05 seconds)
    }
}

/**
 * Initializes a Bootstrap Carousel component for displaying news items.
 *
 * Looks for an HTML element with the ID "newsCarousel" and sets up a carousel
 * to cycle through news items automatically.
 *
 * @remarks
 * This function uses the Bootstrap Carousel component for the news carousel.
 *
 */
function initializeNewsCarousel() {
    const newsCarouselElement = document.getElementById("newsCarousel");
    if (newsCarouselElement) {
        new bootstrap.Carousel(newsCarouselElement, {
            interval: 3000, // Change slide every 3 seconds
            wrap: true, // Set to false if you don't want to loop
        });
    }
}

/**
 * Initializes a cryptocurrency calculator by setting up event listeners.
 *
 * Looks for an HTML input element with the ID "buy_dollars" and adds an "input" event listener
 * to trigger the `cryptoCalculator` function when the input value changes.
 */
function initializeCryptoCalculator() {
    const CryptoAmountInput = document.getElementById("buy_dollars");
    if (CryptoAmountInput) {
        CryptoAmountInput.addEventListener("input", cryptoCalculator);
    }
}

/**
 * Calculates cryptocurrency amount based on a provided USD amount and crypto price.
 *
 * This function is designed to be triggered by an "input" event on an HTML input element.
 * It calculates the equivalent cryptocurrency amount and updates related input fields.
 *
 * @param {Event} event - The event object representing the "input" event.
 */
function cryptoCalculator(event) {
    const usdAmount = document.getElementById(event.target.id + '_decimal').value;
    const cryptoAmount = document.getElementById("buy_cryptos");
    const cryptoAmountDecimal = document.getElementById("buy_cryptos_decimal");
    const cryptoPrice = document.getElementById("crypto_price").value;
    cryptoAmount.value = parseFloat(usdAmount) / parseFloat(cryptoPrice);
    cryptoAmountDecimal.value = parseFloat(usdAmount) / parseFloat(cryptoPrice);
}

/**
 * Initializes a USD calculator by setting up event listeners.
 *
 * Looks for an HTML input element with the ID "sell_cryptos" and adds an "input" event listener
 * to trigger the `usdCalculator` function when the input value changes.
 */
function initializeUsdCalculator() {
    const CryptoAmountInput = document.getElementById("sell_cryptos");
    if (CryptoAmountInput) {
        CryptoAmountInput.addEventListener("input", usdCalculator);
    }
}

/**
 * Calculates the equivalent USD amount based on a provided cryptocurrency amount and price.
 *
 * This function is designed to be triggered by an "input" event on an HTML input element.
 * It calculates the equivalent USD amount and updates related input fields.
 *
 * @param {Event} event - The event object representing the "input" event.
 */
function usdCalculator(event) {
    const usdAmount = document.getElementById('sell_dollars');
    const usdAmountDecimal = document.getElementById('sell_dollars_decimal');
    const cryptoAmount = document.getElementById('sell_cryptos').value;

    const cryptoPrice = document.getElementById('sell-price').value;
    usdAmount.value = (parseFloat(cryptoPrice) * parseFloat(cryptoAmount)).toLocaleString('en-US', {
        style: 'currency',
        currency: 'USD',
        minimumFractionDigits: 2
    });
    usdAmountDecimal.value = parseFloat(cryptoPrice) * parseFloat(cryptoAmount);
}

/**
 * Initializes cryptocurrency price request functionality by setting up event listeners.
 *
 * This function looks for HTML select elements with IDs "id_crypto_select_buy" and "id_crypto_select_sell,"
 * adds "change" event listeners to them, and triggers the `cryptoPriceRequest` function when the selection changes.
 */
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

/**
 * Sends an asynchronous request to fetch the price of a selected cryptocurrency
 * and updates the corresponding input fields and price information.
 *
 * @param {Event} event - The event object representing the "change" event on a cryptocurrency selection.
 *                        The target of the event should be a select element with cryptocurrency options.
 */
async function cryptoPriceRequest(event) {
    const cryptoSelected = event.target.value;
    let cryptoPriceElement;
    let cryptoPriceTextElement;

    if (event.target.id === 'id_crypto_select_buy') {
        cryptoPriceElement = document.getElementById('crypto_price');
        cryptoPriceTextElement = document.getElementById('crypto-price-info-buy');
        document.getElementById('buy_dollars').value = '$.0';
        document.getElementById('buy_dollars_decimal').value = '0.00';
        document.getElementById('buy_cryptos').value = '0.00';
        document.getElementById('buy_cryptos_decimal').value = '0.00';

    } else if (event.target.id === 'id_crypto_select_sell') {
        cryptoPriceElement = document.getElementById('sell-price');
        cryptoPriceTextElement = document.getElementById('crypto-price-info-sell');
        document.getElementById('sell_dollars').value = '$.0';
        document.getElementById('sell_dollars_decimal').value = '0.00';
        document.getElementById('sell_cryptos').value = '0.00';
        document.getElementById('sell_cryptos_decimal').value = '0.00';
    }
    try {
        const response = await fetch(`/get_price/?crypto=${cryptoSelected}`);
        const data = await response.json();
        const symbol = data.symbol.toUpperCase();
        const price = data.current_price;
        cryptoPriceElement.value = price;
        cryptoPriceTextElement.textContent = `Where ${symbol} 1 = USD $${price}`;
    } catch (error) {
        console.error("Error fetching crypto price:", error);
    }
}

/**
 * Initializes USD input formatters by setting up event listeners.
 *
 * Looks for HTML input elements with IDs "deposit_dollars_form," "withdraw_dollars_form," and "buy_dollars,"
 * and adds "input" event listeners to trigger the `usdFormatter` function when the input values change.
 */
function initializeUsdFormatter() {
    const depositDollarForm = document.getElementById('deposit_dollars_form');
    const withdrawDollarForm = document.getElementById('withdraw_dollars_form');
    const buyCryptoForm = document.getElementById('buy_dollars');
    if (depositDollarForm) {
        depositDollarForm.addEventListener('input', usdFormatter);
    }
    if (withdrawDollarForm) {
        withdrawDollarForm.addEventListener('input', usdFormatter);
    }
    if (buyCryptoForm) {
        buyCryptoForm.addEventListener('input', usdFormatter);
    }
}

/**
 * Formats a USD input field by removing non-numeric characters, leading zeros,
 * adding commas as a thousand separators, and formatting as a currency with a dollar sign.
 *
 * This function is designed to be triggered by an "input" event on an HTML input element.
 * It formats the input value as a currency amount in USD.
 *
 * @param {Event} event - The event object representing the "input" event on an HTML input element.
 */
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
    const unformattedInput = integerPart + '.' + decimalPart;
    const decimalDollars = document.getElementById(inputElement.id + '_decimal');
    decimalDollars.value = unformattedInput;

    // Update the input field with the formatted value
    inputElement.value = formattedInput;
}

/**
 * Toggles the visibility of hidden rows in a table by removing the "d-none" and "hidden-row" classes.
 *
 * This function is designed to be triggered by a button click to reveal hidden rows.
 * If there are more than 5 hidden rows, it reveals the first 5, and if there are no more hidden rows left,
 * it removes the triggering button.
 *
 * @param {HTMLElement} button - The button element that triggers the row toggling action.
 */
function toggleRow(button) {
    const hiddenRows = document.querySelectorAll('.d-none.hidden-row');
    if (hiddenRows) {
        for (let i = 0; i < Math.min(hiddenRows.length, 5); i++) {
            hiddenRows[i].classList.remove('d-none');
            hiddenRows[i].classList.remove('hidden-row');
        }
        const leftHiddenRows = document.querySelectorAll('.d-none.hidden-row');
        if (leftHiddenRows.length <= 0) {
            button.remove();
        }
    }
}

/**
 * Initializes a confirmation dialog for a specified HTML element by setting up a form submission event listener.
 *
 * This function looks for an HTML element with the given ID, adds a "submit" event listener to it,
 * and displays a confirmation dialog with a message generated by the provided message function.
 * If the user confirms, the form submission proceeds; otherwise, it's prevented.
 *
 * @param {string} elementId - The ID of the HTML element that triggers the confirmation dialog.
 * @param {function(): string} messageFunction - A function that generates the confirmation message.
 */
function initializeConfirmation(elementId, messageFunction) {
    const element = document.getElementById(elementId);
    if (element) {
        element.addEventListener('submit', function (event) {
            const confirmationMessage = messageFunction();
            const confirmed = confirm(confirmationMessage);
            if (!confirmed) {
                event.preventDefault(); // Prevent form submission
            }
        });
    }
}

/**
 * Initializes confirmation dialogs for actions such as deposit, withdrawal, buying, selling, and crypto deletion.
 *
 * This function sets up event listeners for form submissions and displays confirmation dialogs with appropriate messages.
 * - For deposit and withdrawal, it confirms the action with the provided amount.
 * - For buying and selling cryptocurrencies, it confirms the action with the selected cryptocurrency, USD amount, and crypto amount.
 * - For crypto deletion, it confirms the action with the specified cryptocurrency, warning about its removal from all users' wallets.
 *
 * Note: The confirmation dialogs allow users to confirm or cancel their actions.
 */
function initializeConfirmations() {
    initializeConfirmation('deposit', () => {
        const amount = document.getElementById('deposit_dollars_form').value;
        return `Are you sure you want to deposit ${amount} ?`;
    });

    initializeConfirmation('withdraw', () => {
        const amount = document.getElementById('withdraw_dollars_form').value;
        return `Are you sure you want to withdraw ${amount} ?`;
    });

    initializeConfirmation('buy', () => {
        const crypto = document.getElementById('id_crypto_select_buy').value;
        const usdAmount = document.getElementById('buy_dollars').value;
        const cryptoAmount = document.getElementById('buy_cryptos').value;
        return `Are you sure you want to buy ${crypto} ${cryptoAmount} for ${usdAmount}`;
    });

    initializeConfirmation('sell', () => {
        const crypto = document.getElementById('id_crypto_select_sell').value;
        const usdAmount = document.getElementById('sell_dollars').value;
        const cryptoAmount = document.getElementById('sell_cryptos').value;
        return `Are you sure you want to sell ${crypto} ${cryptoAmount} for ${usdAmount}`;
    });

    const dellButtons = document.querySelectorAll(".btn-delete");
    if (dellButtons) {
        dellButtons.forEach(function (button) {
            const form = button.closest('form');
            const crypto = button.id;
            form.addEventListener('submit', function (event) {
                const message = `Are you sure you want to delete ${crypto}? This action will result in the removal of this cryptocurrency from all users' wallets, and it will disappear from the system permanently. Please confirm your decision.`;
                const confirmed = confirm(message);
                if (!confirmed) {
                    event.preventDefault(); // Prevent form submission
                }
            });
        });
    }
}

// Event Listener
document.addEventListener("DOMContentLoaded", function () {
    initializeNewsCarousel();
    initializeCryptoPriceRequest();
    initializeUsdFormatter();
    initializeCryptoCalculator();
    initializeUsdCalculator();
    initializeConfirmations();

});

const successMessages = document.getElementsByClassName("alert-success");
fadeOutAndHideElementsAutomatically(successMessages, 8000, 2000);