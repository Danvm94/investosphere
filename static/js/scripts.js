function allowOnlyLetters(inputElement) {
  inputElement.value = inputElement.value.replace(/[^a-zA-Z]/g, "");
}
