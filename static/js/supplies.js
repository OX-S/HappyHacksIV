// START CODE FOR THE MAP
const map = L.map('map').setView([40.8833, -74.0111], 12); //Bergen County, NJ

   L.tileLayer('https://{s}.basemaps.cartocdn.com/rastertiles/voyager/{z}/{x}/{y}{r}.png', {
        attribution: '© OpenStreetMap contributors'
    }).addTo(map);

const dropOffPoints = [
    {name: 'Drop-off Point 1', location: [40.852, -74.043]},
    {name: 'Drop-off Point 2', location: [40.901, -74.047]},
    {name: 'Drop-off Point 3', location: [40.912, -73.983]},
];
dropOffPoints.forEach(function(point) {
    L.marker(point.location).addTo(map).bindPopup(point.name);
});
// END CODE FOR THE MAP


// Function to update the values of the supplies to donate
function updateQuantity(itemName, change) {
    const inputElement = document.getElementById(itemName);
    const currentQuantity = parseInt(inputElement.value);
    const newQuantity = currentQuantity + change;

    if (newQuantity >= 0) {
        inputElement.value = newQuantity;
    }
}