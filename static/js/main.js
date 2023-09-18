function validateRecipeForm() {
    var searchQuery = document.getElementsByName("search_query")[0].value;
    var errorMessage = document.getElementById("recipe-error-message");

    if (searchQuery.trim() === "") {
        errorMessage.innerText = "Please enter a search query\n(e.g., Yassa, Lasagne.. .)\n🔥👇🏿🔥";
        return false; // Prevent form submission
    } else {
        errorMessage.innerText = ""; // Clear the error message
        return true; // Allow form submission
    }
}

function validateNutriForm() {
    var ingredients = document.getElementById("nutri-ingredients").value;
    var errorMessage = document.getElementById("nutri-error-message");

    if (ingredients.trim() === "") {
        errorMessage.innerText = "Please enter a recipe or ingredients\n(e.g., 109g Paella, 19g Sugar.. .)\n🔥👇🏿🔥";
        return false; // Prevent form submission
    } else {
        errorMessage.innerText = ""; // Clear the error message
        return true; // Allow form submission
    }
}
