$(document).ready( function () {
    var map = L.map('map', { scrollWheelZoom: false })
    .setView([21, 78], 4);

    var mapquestLayer = new L.tileLayer('http://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}.png', 
          {
            attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, &copy; <a href="http://cartodb.com/attributions">CartoDB</a>',
            maxZoom: 18
          });
    map.addLayer(mapquestLayer);
});