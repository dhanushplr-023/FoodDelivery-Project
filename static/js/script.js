// ================================
// DOM Elements
// ================================

const foodSelect = document.getElementById("food_item");
const otherFoodDiv = document.getElementById("otherFoodDiv");
const preview = document.getElementById("foodPreview");

// ================================
// Food Images
// ================================

const foodImages = {

    "Margherita Pizza": "pizza.png",

    "Farmhouse Pizza": "pizza.png",

    "Pepperoni Pizza": "pizza.png",

    "Veg Burger": "burger.png",

    "Chicken Burger": "burger.png",

    "French Fries": "fries.png",

    "White Sauce Pasta": "pasta.png",

    "Hakka Noodles": "noodles.png",

    "Mexican Wrap": "wrap.png",

    "Cold Coffee": "coffee.png",

    "Other": "default-food.png"

};

// ================================
// Dropdown Change
// ================================

if (foodSelect) {

    foodSelect.addEventListener("change", updateFoodPreview);

}

// ================================
// Update Preview
// ================================

function updateFoodPreview() {

    const selectedFood = foodSelect.value;

    if (selectedFood === "Other") {

        otherFoodDiv.style.display = "block";

    } else {

        otherFoodDiv.style.display = "none";

    }

    if (preview) {

        preview.src = "/static/images/" + foodImages[selectedFood];

    }

}

// ================================
// Menu Card Button
// ================================

function selectFood(foodName) {

    foodSelect.value = foodName;

    updateFoodPreview();

    document.getElementById("order").scrollIntoView({

        behavior: "smooth"

    });

}

// =========================
// Quantity Controls
// =========================

function increaseQty(){

    const qty=document.getElementById("quantity");

    if(parseInt(qty.value)<10){

        qty.value++;

    }

}

function decreaseQty(){

    const qty=document.getElementById("quantity");

    if(parseInt(qty.value)>1){

        qty.value--;

    }

}

// ==============================
// Loading Animation
// ==============================

const orderForm = document.querySelector("form");

if(orderForm){

orderForm.addEventListener("submit",function(){

const btn=document.getElementById("orderBtn");

const spinner=document.getElementById("loadingSpinner");

btn.disabled=true;

btn.innerHTML="Processing Order...";

spinner.style.display="block";

});

}
