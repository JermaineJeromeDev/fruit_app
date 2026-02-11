const url = "http://127.0.0.1:8000/fruit_app/";

async function loadFruits() {
    try {
        const response = await fetch(url);
        const data = await response.json();
        console.log("Daten empfangen:", data);

        const listElement = document.getElementById('fruit-list');
        
        // Daten im HTML rendern
        data.forEach(fruit => {
            const li = document.createElement('li');
            li.innerText = `${fruit.name} (${fruit.farbe}) - ${fruit.gewicht}g`;
            listElement.appendChild(li);
        });

    } catch (error) {
        console.error("Fehler beim Laden:", error);
    }
}

loadFruits();