async function fetchDBLP() {
  const url = 'https://dblp.org/pid/68/7553-1.html';
  const res = await fetch(url);
  const text = await res.text();
  const parser = new DOMParser();
  const doc = parser.parseFromString(text, 'text/html');
  
  const publications = [];
  
  doc.querySelectorAll('.data').forEach(div => {
    const authors = Array.from(div.querySelectorAll('.author')).map(a => a.textContent.trim());
    if(authors.length > 0) publications.push(authors);
  });
  
  return publications;
}

function buildGraph(publications, centerName="Daniel de Oliveira") {
  const nodesMap = new Map();
  const links = [];

  publications.forEach(authors => {
    if (!authors.includes(centerName)) return;
    authors.forEach(name => {
      if (!nodesMap.has(name)) nodesMap.set(name, { id: name, isCenter: name===centerName });
    });
    authors.forEach(a1 => {
      authors.forEach(a2 => {
        if(a1!==a2) links.push({ source: a1, target: a2 });
      });
    });
  });

  return { nodes: Array.from(nodesMap.values()), links };
}

async function renderGraph() {
  const publications = await fetchDBLP();
  const { nodes, links } = buildGraph(publications);

  const width = 900, height = 600;
  const svg = d3.select("#graph")
                .append("svg")
                .attr("width", width)
                .attr("height", height);

  const simulation = d3.forceSimulation(nodes)
      .force("link", d3.forceLink(links).id(d=>d.id).distance(120))
      .force("charge", d3.forceManyBody().strength(-300))
      .force("center", d3.forceCenter(width/2, height/2));

  const link = svg.append("g")
    .selectAll("line")
    .data(links)
    .enter().append("line")
    .attr("stroke","#999").attr("stroke-opacity",0.6);

  const node = svg.append("g")
    .selectAll("circle")
    .data(nodes)
    .enter().append("circle")
    .attr("r", d=>d.isCenter?10:6)
    .attr("fill", d=>d.isCenter?"orange":"steelblue")
    .call(d3.drag()
      .on("start", dragstarted)
      .on("drag", dragged)
      .on("end", dragended));

  node.append("title").text(d=>d.id);

  simulation.on("tick", ()=>{
    link
      .attr("x1", d=>d.source.x)
      .attr("y1", d=>d.source.y)
      .attr("x2", d=>d.target.x)
      .attr("y2", d=>d.target.y);

    node
      .attr("cx", d=>d.x)
      .attr("cy", d=>d.y);
  });

  function dragstarted(event,d){
    if(!event.active) simulation.alphaTarget(0.3).restart();
    d.fx = d.x; d.fy = d.y;
  }

  function dragged(event,d){
    d.fx = event.x; d.fy = event.y;
  }

  function dragended(event,d){
    if(!event.active) simulation.alphaTarget(0);
    d.fx = null; d.fy = null;
  }
}

renderGraph();
