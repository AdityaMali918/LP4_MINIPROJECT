document.getElementById("logout-btn").addEventListener("click", function() {
    alert("You have been logged out!");
    window.location.href = "index.html";  // Redirect to login page
});

// Array of items to display in cards
const items = [
    {
        name: "Sneakers",
        image: "images/sneaker.jpg"
    },
    {
        name: "Bag",
        image: "images/bag.jpg" 
    },
    {
        name: "Watch",
        image: "images/watch.jpg" 
    },
    {
        name: "Mouse",
        image: "images/mouse.jpg" 
    },
    {
        name: "Mobile cover",
        image: "images/cover.jpg" 
    }
];


function displayItems() {
    const itemContainer = document.getElementById('item-container');

 
    itemContainer.innerHTML = '';

    items.forEach(item => {
        
        const card = document.createElement('div');
        card.classList.add('item-card');

        
        const img = document.createElement('img');
        img.src = item.image;
        img.alt = item.name;

        
        const h3 = document.createElement('h3');
        h3.textContent = item.name;


        card.appendChild(img);
        card.appendChild(h3);

        itemContainer.appendChild(card);
    });
}


window.onload = displayItems;

