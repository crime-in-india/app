$(document).ready( function () {
    // var map = L.map('map', { scrollWheelZoom: false })
    // .setView([21, 78], 4);

    // var mapquestLayer = new L.tileLayer('http://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}.png', 
    //       {
    //         attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, &copy; <a href="http://cartodb.com/attributions">CartoDB</a>',
    //         maxZoom: 18
    //       });
    // map.addLayer(mapquestLayer);

    var margin = {top: 10, right: 10, bottom: 10, left: 10};
    var div = d3.select('#map').node().getBoundingClientRect();

    var width = div.width - margin.left - margin.right,
	    height = div.height - margin.top - margin.bottom;

	var proj = d3.geo.mercator()
	.center([85, 27])
    .scale(1000);
	
	var path = d3.geo.path()
	.projection(proj);

	var s = proj.scale();
	
	var map = d3.select("#map")
	.append("svg")
	.attr("width", width)
	.attr("height", 630)
	//.call(initialize)

	var india = map.append("svg:g")
	.attr("id", "india")
	.attr("tranform", "translate(-200,0)");

	d3.json("India.json", function (err, json) {
		if (err) throw err;

		var india_geojson = topojson.feature(json, json.objects.Admin2);

		india.selectAll("path")
		.data(india_geojson.features)
		.enter()
		.append("path")
		.attr("class", "state")
		.attr("d", path);
	});

	india.append("a")
	.attr("xlink:href", "/crime-page.html")
	.append("circle")
	.attr("cx", proj([72.8826100,19.0728300])[0])
	.attr("cy", proj([72.8826100,19.0728300])[1])
	.attr("r", 15)
	.attr("fill", "darkred")
	.attr("stroke", "black");
	;

});