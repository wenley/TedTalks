
backgroundDraggable = function(svg) {
  var container = svg.append("g");

  var zoomed = function() {
    container.attr("transform", "translate(" + d3.event.translate + ")scale(" + d3.event.scale + ")");
  }

  var zoom = d3.behavior.zoom()
  .scaleExtent([0.1, 10])
  .on("zoom", zoomed)

  svg.call(zoom)
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
