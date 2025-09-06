const d3 = require('d3');

function generateCollaborationGraph(publications) {
  const nodes = [];
  const links = [];

  publications.forEach(pub => {
    pub.authors.forEach((author, i) => {
      // Add author nodes
      if (!nodes.some(n => n.name === author)) {
        nodes.push({ id: author });
      }
      // Create links between authors
      pub.authors.slice(i + 1).forEach(coauthor => {
        links.push({ source: author, target: coauthor });
      });
    });
  });

  // Set up the SVG canvas dimensions
  const width = 800;
  const height = 600;

  const svg = d3.select('body').append('svg')
    .attr('width', width)
    .attr('height', height);

  const simulation = d3.forceSimulation(nodes)
    .force('link', d3.forceLink(links).id(d => d.id).distance(100))
    .force('charge', d3.forceManyBody().strength(-200))
    .force('center', d3.forceCenter(width / 2, height / 2));

  const link = svg.append('g')
    .selectAll('.link')
    .data(links)
    .enter().append('line')
    .attr('class', 'link')
    .attr('stroke', '#999')
    .attr('stroke-opacity', 0.6);

  const node = svg.append('g')
    .selectAll('.node')
    .data(nodes)
    .enter().append('circle')
    .attr('class', 'node')
    .attr('r', 5)
    .attr('fill', '#1f77b4')
    .call(d3.drag()
      .on('start', dragstarted)
      .on('drag', dragged)
      .on('end', dragended));

  node.append('title')
    .text(d => d.id);

  simulation.on('tick', () => {
    link
      .attr('x1', d => d.source.x)
      .attr('y1', d => d.source.y)
      .attr('x2', d => d.target.x)
      .attr('y2', d => d.target.y);

    node
      .attr('cx', d => d.x)
      .attr('cy', d => d.y);
  });

  function dragstarted(event) {
    if (!event.active) simulation.alphaTarget(0.3).restart();
    event.subject.fx = event.subject.x;
    event.subject.fy = event.subject.y;
  }

  function dragged(event) {
    event.subject.fx = event.x;
    event.subject.fy = event.y;
  }

  function dragended(event) {
    if (!event.active) simulation.alphaTarget(0);
    event.subject.fx = null;
    event.subject.fy = null;
  }
}
