# DAA Lab Assignments (CS5303)

This repository contains Python implementations and performance analyses for Design and Analysis of Algorithms lab experiments.

---

## 1. Interpolation Search
* **File:** `interpolation search.py`
* **Description:** Implements Interpolation Search algorithm to find target values in sorted arrays and measures comparison efficiency over Binary Search for uniformly distributed data.

---

## 2. String Matching Algorithms
* **File:** `rabin karp.py`
* **Description:** Compares Naive String Matching, Knuth-Morris-Pratt (KMP), and Rabin-Karp algorithms based on character comparisons over varying pattern lengths.

---

## 3. Minimum Spanning Tree (MST)
* **File:** `mst_kruskal_prim.py`
* **Description:** Implements Kruskal's (using Union-Find) and Prim's (using Min-Heap) algorithms to compute the Minimum Spanning Tree cost for weighted undirected graphs.

---

## 4. Dijkstra's Algorithm
* **File:** `dijkstra.py`
* **Description:** Computes single-source shortest paths in weighted directed graphs using Dijkstra's algorithm with a priority queue (Min-Heap).

---

## 5. Min-Max using Divide and Conquer
* **File:** `min_max_dc.py`
* **Description:** Finds minimum and maximum elements in an array using Divide & Conquer ($3n/2 - 2$ comparisons) versus Naive sequential search ($2n - 2$ comparisons).

### Sample Output (Experiment 5):
```text
Size     DC Comps    Naive Comps   Formula 3n/2-2
------------------------------------------------------
  10           14             18               13
 100          148            198              148
1000         1498           1998             1498
10000        14998          19998            14998
