var cities = cities;

var margin = {top: 10, right: 100, bottom: 10, left: 40};
var div = d3.select('#map').node().getBoundingClientRect();

var width = div.width - margin.left - margin.right,
  height = 700;

var proj = d3.geo.mercator()
.center([81, 27])
.scale(1200);

var path = d3.geo.path()
.projection(proj);

var zoom = d3.behavior.zoom()
  .on("zoom", zoomed);

var map = d3.select("#map")
.append("svg")
.attr("width", "100%")
.attr("height", "100%")
.attr("viewBox", "0 0 " + width + " " + height)
.attr("preserveAspectRatio", "xMinYMin");

// Make sure all elements load together
var q = d3_queue.queue();

q.defer(d3.json, "static/data/india-states.json")
	.await(makeMap);

var india = map.append("svg:g")
.attr("id", "india");

// Call the zoom function on svg
//map.call(zoom);

function makeMap(err, json) {
	if (err) console.error(err);

	var india_geojson = topojson.feature(json, json.objects.Admin2);

	// Make the map with state boundary lines
	india.selectAll("path")
	.data(india_geojson.features)
	.enter()
	.append("path")
	.attr("class", "state")
	.attr("d", path);

	// Plot the city points on the map
	india.selectAll("a")
	.data(cities)
	.enter()
	.append("a")
	.attr("xlink:href", function (d) { return 'cities/' + d.city; })
	.attr("xlink:target", "_blank")
	.attr("class", "city-dot")
	.append("circle")
	.attr("cx", function (d) { return proj([d.longitude,d.latitude])[0]; })
	.attr("cy", function (d) { return proj([d.longitude,d.latitude])[1]; })
	.attr("r", 7)
	.attr("class", "city-dot");
}

function zoomed() {
	india.attr("transform", "translate(" + d3.event.translate + ")scale(" + d3.event.scale + ")");
	india.selectAll("circle")
  .attr("d", path.projection(proj));
}

$('a[href^="#"]').on('click',function (e) {
    e.preventDefault();

    var target = this.hash;
    var $target = $(target);

    $('html, body').stop().animate({
        'scrollTop': $target.offset().top
    }, 900, 'swing', function () {
        window.location.hash = target;
    });
});