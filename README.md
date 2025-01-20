# Hocus: A 3D Puzzle Solver

### Authors
- **Maheen Ahmed** (429551)  
- **Taha Shah** (408351)  
- **Zain Ali** (405704)  

---

## Table of Contents
1. [Introduction](#introduction)
2. [Problem Statement](#problem-statement)
3. [Methodology](#methodology)
4. [Technologies Used](#technologies-used)
5. [Results](#results)
6. [Conclusion](#conclusion)
7. [References](#references)

---

## Introduction
Hocus is a 3D puzzle-solving project aimed at automating the solution for puzzles in the **Hocus** app. The game features a maze-like structure with a movable box that must be inserted into a target goal.  
The solver uses a **static image of the puzzle**, extracts a graph representation, and generates a sequence of moves to automatically solve the puzzle in real-time.

---

## Problem Statement
The challenge involves:
- Interfacing with a mobile device to capture puzzle screenshots and send swipe signals.
- Extracting the 3D graph structure from the screenshot using image processing techniques.
- Finding the optimal path using **A*** or **BFS** algorithms, depending on the graph's nature.
- Translating the solution into swipe actions to solve the puzzle automatically.

---

## Methodology
### Steps:
1. **Screenshot Capturing:**  
   Use **ADB (Android Debug Bridge)** to capture and crop the puzzle image.
   
2. **Image Processing:**  
   - Create a mask to filter grayscale pixels.
   - Apply contours to outline red objects (box and goal).
   - Segment the maze into a hexagonal grid.

3. **Graph Construction:**  
   - Build a six-dimensional graph based on hexagon connections and intersections.
   - Define special nodes (e.g., portals) for multidimensional transitions.

4. **Pathfinding:**  
   - Use **A*** or **BFS** to traverse the graph and identify the optimal path.

5. **Execution:**  
   - Map the solution path to swipe actions.
   - Send swipe commands to the device in sequence to solve the puzzle.

---

## Technologies Used
- **Programming Languages:** Python  
- **Libraries:** OpenCV, ADB  
- **Algorithms:** A*, BFS, Image Segmentation, Graph Construction  
- **Tools:** Excalidraw (for visualization)

---

## Results
- **Accuracy:** 100% (solved all 40 puzzles in the Hocus app).  
- **Speed:** 1-2 seconds to extract and solve each puzzle.

---

## Conclusion
The Hocus Puzzle Solver demonstrates the potential for real-time automation in gaming by integrating **AI**, **image processing**, and **graph theory**. Its generalized design enables applicability to other puzzle-solving scenarios where access to source code or training datasets is unavailable.

---

## References
1. **Holzinger, A., et al.** (2014). Graph Extraction from Image Data. *Brain Informatics and Health*. DOI: 10.1007/978-3-319-09891-3_50  
2. **Valderhaug, V. D., et al.** (2019). Deep Learning Toolbox for Neuronal Graphs. *arXiv preprint*.  
3. **Hart, P. E., et al.** (1968). A* Search Algorithm. *IEEE Transactions on Systems Science and Cybernetics*.  
4. **Likhachev, M., et al.** (2005). Anytime Dynamic A*. *ICAPS Proceedings*.  
