# Mathematical Chaos Visualization

This repository contains a Python implementation to compute and illustrate the idea of **mathematical chaos** using the logistic map function. The notebook visualizes various aspects of chaotic systems, including:

- Iterative calculations of the logistic map in two forms.
- A bifurcation diagram showing the evolution of chaos.
- A Lyapunov exponent plot to measure system divergence.
- Attractor visualization to highlight chaotic behavior.

## The Functions
The original logistic map function used is:

p_{next} = p + rp - rp^2

which can be equivalently written in two forms:
- **Function 1**:   p_next = p + rp(1 - p)
- **Function 2**:   p_next = (1 + r)p - rp^2
  
## Features
### Result Table
The notebook displays a comparison table of iterative results for both functions and their differences. Even with high precision, the results diverge quickly due to the chaotic nature of the system.

### Oscillation Diagram
The bifurcation diagram is generated for **Function 1** to illustrate how the value of (p) evolves as (r) changes. This provides a visual representation of the transition to chaos.

### Lyapunov Exponent Plot
The Lyapunov exponent measures the rate of divergence in the system:
- Positive values indicate chaotic behavior.
- Zero or negative values indicate stable or periodic behavior.

### Attractor Visualization
An attractor is plotted for (p[n]) vs. (p[n+1]), showing the system's long-term behavior for a specific (r)-value.

## Optimal Settings
The default parameters are:
- Initial value: (p = 0.01)
- Constant (r = 3.0)

These settings provide a clear demonstration of chaos. The comparison table (especially the difference column) highlights how rapidly the system becomes chaotic.

---

## Examples of Visualizations

1. **Bifurcation Diagram**:
   ![Bifurcation Diagram](https://github.com/user-attachments/assets/d0ea342d-4b25-4623-ab1b-42ed64e2287e)

3. **Lyapunov Exponent Plot**:

   ![Lyapunov Exponent](https://github.com/user-attachments/assets/243011d9-c8c0-4b2d-8613-30e70a941254)

---

## How to Run
1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/mathematical-chaos-visualization.git
2. or copy-paste and run in Jupyter Lab
