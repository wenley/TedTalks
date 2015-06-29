initialize = function() {
  var width = 1200;
  var height = 800;
  var color = d3
    .scale
    .category20();

  console.log("In context")
  return {
    width: width,
    height: height,
    color: color,
  }
}

drawGraph = function(svg, context) {
  console.log("Drawing graph")

  var baseLinkLength = 50
  var linkValueCutoff = 1.2

  svg = backgroundDraggable(svg);

  var force = d3
    .layout
    .force()
    .charge(-120)
    .linkDistance(function(link) {
      return baseLinkLength * link.value;
    })
    .size([context.width, context.height]);

  d3.json("edges.json", function(error, graph) {
    if (error) throw error;

    // Only make relevant links strong
    linksToInclude = graph.links.filter(function(link) {
      return link.value >= linkValueCutoff;
    });

    force.nodes(graph.nodes)
    .links(linksToInclude)
    .start();

    var link = svg.append("g")
    .attr("class", "links")
    .selectAll(".link")
    .data(graph.links)
    .enter().append("line")
    .attr("class", "link")
    .style("stroke-width", function(d) { return Math.sqrt(d.value); });

    var node = svg.append("g")
    .attr("class", "nodes")
    .selectAll(".node")
    .data(graph.nodes)
    .enter().append("circle")
    .attr("class", "node")
    .attr("r", 5)
    .style("fill", function(d) { return context.color(d.group); })
    // .call(force.drag);

    node.append("title")
    .text(function(d) { return d.name; });

    force.on("tick", function() {
      link.attr("x1", function(d) { return d.source.x; })
          .attr("y1", function(d) { return d.source.y; })
          .attr("x2", function(d) { return d.target.x; })
          .attr("y2", function(d) { return d.target.y; });

      node.attr("cx", function(d) { return d.x; })
          .attr("cy", function(d) { return d.y; });
    });
  });
}

run_graph = function() {
  var context = initialize();
  var svg = d3
    .select("body")
    .append("svg")
    .attr("width", context.width)
    .attr("height", context.height);

  drawGraph(svg, context);
}

window.onload = run_graph;

