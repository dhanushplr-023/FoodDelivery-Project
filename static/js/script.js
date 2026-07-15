const foodSelect=document.getElementById("food_item");

const otherFoodDiv=document.getElementById("otherFoodDiv");

const preview=document.getElementById("foodPreview");

const images={

"Margherita Pizza":"pizza.png",

"Farmhouse Pizza":"pizza.png",

"Pepperoni Pizza":"pizza.png",

"Veg Burger":"burger.png",

"Chicken Burger":"burger.png",

"French Fries":"fries.png",

"White Sauce Pasta":"pasta.png",

"Hakka Noodles":"noodles.png",

"Mexican Wrap":"wrap.png",

"Cold Coffee":"coffee.png",

"Other":"default-food.png"

};

foodSelect.addEventListener("change",function(){

if(this.value==="Other"){

otherFoodDiv.style.display="block";

}else{

otherFoodDiv.style.display="none";

}

preview.src="/static/images/"+images[this.value];

});
