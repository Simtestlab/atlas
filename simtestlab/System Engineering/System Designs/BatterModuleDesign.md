# Interactive 3D Model Demo

See the interactive BESS module enclosure model below. You can rotate, zoom, and inspect the model right in your browser.

<!-- Load the model-viewer library -->
<script type="module" src="https://unpkg.com/@google/model-viewer/dist/model-viewer.min.js"></script>

<model-viewer
  src="/models/part.glb"
  alt="BESS module enclosure"
  camera-controls
  auto-rotate
  shadow-intensity="0.6"
  style="width:100%;max-width:800px;height:480px;--poster-color: #84c5adff;background-color:#013220;">
</model-viewer>

## Module Design Overview

Dimensions: 1200mm x 800mm x 600mm