// Get elements
const foodSelect = document.getElementById("food_item");
const otherFoodDiv = document.getElementById("otherFoodDiv");

// Run only if the elements exist
if (foodSelect && otherFoodDiv) {

    foodSelect.addEventListener("change", function () {

        if (this.value === "Other") {

            otherFoodDiv.style.display = "block";

        } else {

            otherFoodDiv.style.display = "none";

        }

    });

}
