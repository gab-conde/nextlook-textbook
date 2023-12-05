import { Component, AfterViewInit } from '@angular/core';
import { IonApp, IonRouterOutlet, IonSearchbar, IonSegment, IonSegmentButton, IonLabel, IonContent, IonHeader, IonToolbar, IonTitle } from '@ionic/angular/standalone';
// import * as d3 from 'd3';

@Component({
  selector: 'app-root',
  templateUrl: 'app.component.html',
  standalone: true,
  imports: [IonApp, IonRouterOutlet, IonSearchbar, IonSegment, IonSegmentButton, IonLabel, IonContent, IonHeader, IonToolbar, IonTitle],
})
export class AppComponent {
  constructor() {}
}

// Visualization of graph with physics to be implemented later
// // Define interfaces for Node and Link
// interface Node {
//   id: string;
//   x?: number;
//   y?: number;
// }
//
// interface Link {
//   source: string;
//   target: string;
// }
//
// export class HomePage implements AfterViewInit {
//
//   constructor() {}
//
//   ngAfterViewInit() {
//     this.createGraph();
//   }
//
//   createGraph() {
//     // Example adjacency list
//     const adjacencyList = {
//       'Node1': ['Node2', 'Node3'],
//       'Node2': ['Node3'],
//       'Node3': ['Node1'],
//       // Add more nodes and edges as needed
//     };
//
//     // Convert adjacency list to nodes and links
//     let nodes: Node[] = [];
//     let links: Link[] = [];
//     for (const [key, values] of Object.entries(adjacencyList)) {
//       nodes.push({ id: key });
//       values.forEach(value => {
//         links.push({ source: key, target: value });
//       });
//     }
//
//     const width = 800, height = 600;
//
//     const svg = d3.select('#graph')
//       .attr('width', width)
//       .attr('height', height);
//
//     // Create links (lines)
//     svg.selectAll('line')
//       .data(links)
//       .enter()
//       .append('line')
//       .style('stroke', '#999')
//       .style('stroke-opacity', 0.6)
//       .style('stroke-width', 2);
//
//     // Create nodes (circles)
//     svg.selectAll('circle')
//       .data(nodes)
//       .enter()
//       .append('circle')
//       .attr('r', 5)
//       .style('fill', '#69b3a2');
//
//     // Add labels to nodes
//     svg.selectAll('text')
//       .data(nodes)
//       .enter()
//       .append('text')
//       .text(d => d.id)
//       .style('fill', 'black')
//       .attr('x', 6)
//       .attr('y', 3);
//
//     // Implement force simulation
//     const simulation = d3.forceSimulation(nodes as any)
//       .force('link', d3.forceLink(links as any).id((d: any) => d.id))
//       .force('charge', d3.forceManyBody())
//       .force('center', d3.forceCenter(width / 2, height / 2));
//
//     simulation.on('tick', () => {
//       svg.selectAll('line')
//         .attr('x1', d => (d as any).source.x)
//         .attr('y1', d => (d as any).source.y)
//         .attr('x2', d => (d as any).target.x)
//         .attr('y2', d => (d as any).target.y);
//
//       svg.selectAll('circle')
//         .attr('cx', d => (d as any).x)
//         .attr('cy', d => (d as any).y);
//
//       svg.selectAll('text')
//         .attr('x', d => (d as any).x)
//         .attr('y', d => (d as any).y);
//     });
//   }
// }
