export class MapManager {
  constructor(canvasId) {
    this.canvas = document.getElementById(canvasId);
    this.ctx = this.canvas.getContext("2d");
    this.layer = "map"; // Default
    // Further map, object, and token rendering code here...
  }

  setLayer(layer) {
    this.layer = layer;
    // Redraw as needed...
  }

  // Add methods to draw grid, handle tokens, objects, etc.
}