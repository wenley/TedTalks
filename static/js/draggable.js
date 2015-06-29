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

nodeDraggable = function(nodes, force) {
  var dragstarted = function(d) {
    d3.event.sourceEvent.stopPropagation();
    d3.select(this).classed("dragging", true);
  }
  var dragged = function(d) {
    d3.select(this).attr("cx", d.x = d3.event.x).attr("cy", d.y = d3.event.y);
  }
  var dragended = function(d) {
    d3.select(this).classed("dragging", false);
    // d3.select(this).classed("fixed", true);
    force.start();
  }

  var drag = d3.behavior.drag()
  .origin(function(d) { return d; })
  .on("dragstart", dragstarted)
  .on("drag", dragged)
  .on("dragend", dragended)

  return nodes.call(drag);
}

