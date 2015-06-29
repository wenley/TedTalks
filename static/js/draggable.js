backgroundDraggable = function(svg) {
  // Create container that responds to events on background
  var container = svg.append("g");

  var rect = container.append("rect")
  .attr("width", 1200)
  .attr("height", 800)
  .style("fill", "none")
  .style("pointer-events", "all");

  var zoomed = function() {
    container.attr("transform", "translate(" + d3.event.translate + ")scale(" + d3.event.scale + ")");
  }

  var zoom = d3.behavior.zoom()
  .scaleExtent([0.1, 10])
  .on("zoom", zoomed)

  return container.call(zoom);
}

nodeDraggable = function(svg) {
}

draggable = function(svg) {
  var drag = d3.behaviour.drag()
  .origin(function(d) { return d; })
  .on("dragstart", dragstarted)
  .on("drag", dragged)
  .on("dragend", dragended)
}
