# Deep Learning & Regression Projects

This repository contains three independent machine learning projects:

1. [World Cup Jersey Recognition — Neural Network From Scratch](#1-world-cup-jersey-recognition--neural-network-from-scratch)
2. [Player Rating Prediction — Linear & Polynomial Regression](#2-player-rating-prediction--linear--polynomial-regression)
3. [PCA From Scratch — Dimensionality Reduction](#3-pca-from-scratch--dimensionality-reduction)

---

## Repository Structure

```
.
├── README.md
├── neural-network/
│   └── Task4.ipynb                    # Autograd engine, MLP from scratch, PyTorch MNIST
├── player-rating-regression/
│   └── Competition.ipynb            # Linear & polynomial regression on player stats
└── pca/
    └── Task2.2&2.3_PCA.ipynb          # PCA from scratch + applied to a real dataset
```

---

## 1. World Cup Jersey Recognition — Neural Network From Scratch

### Overview
A neural network built from first principles, framed around a World Cup match-analysis
scenario: reading jersey numbers reliably enough to support real-time tactical decisions.
The project has four phases:

1. **Autograd engine** — a `Value` class implementing reverse-mode automatic
   differentiation (a minimal PyTorch-style computational graph with `backward()`).
2. **Neural network from scratch** — `Neuron`, `Layer`, and `MLP` classes built on top
   of the `Value` engine, with no ML libraries involved.
3. **Training on scikit-learn digits** — an 8x8 handwritten-digit dataset (a mini
   version of MNIST), trained end-to-end with the from-scratch engine, with a training
   loss curve and confusion matrix.
4. **PyTorch re-implementation on full MNIST** — the same architecture, rebuilt in
   PyTorch and trained on the real 70,000-image MNIST dataset, for a direct comparison
   against the from-scratch model.

### What's implemented
- Manual backpropagation via topological sort + reverse-order gradient accumulation
- Core ops: `+`, `*`, `**`, `tanh`, and their gradients
- `Neuron` / `Layer` / `MLP` composed the same way you'd stack layers in PyTorch
- Training loop, loss curve, and confusion matrix on the digits dataset
- A PyTorch `nn.Module` MLP trained on full MNIST, for a from-scratch-vs-framework comparison

**Bonus additions:**
- Softmax + cross-entropy loss (in place of MSE)
- Momentum-based parameter updates
- Dropout (inverted dropout, active only during training)

### Expected results
- From-scratch model (baseline MSE + tanh): ~50–90% test accuracy depending on
  dataset size and epochs (the digits dataset is small, so results vary run to run)
- PyTorch model on full MNIST: typically 95%+ test accuracy after a handful of epochs

### How to run
```bash
cd neural-network
pip install numpy scikit-learn matplotlib torch torchvision
jupyter notebook Task4.ipynb
```
Run all cells top to bottom. The from-scratch training loop is pure Python, so
expect roughly 1–3 minutes per epoch — that's expected, not a bug.

---

## 2. Player Rating Prediction — Linear & Polynomial Regression

### Overview
A regression project (Kaggle-style player-stats dataset) predicting a player's
overall rating from their individual attribute scores — pace, shooting, passing,
dribbling, defending, physicality, and similar per-player statistics. The goal is to
compare a simple linear model against polynomial regression to see whether the
relationship between attributes and rating is better captured by a non-linear fit,
and where that added flexibility helps or starts to overfit.

### Approach
1. **Exploratory Data Analysis (EDA)** — inspect feature distributions, check for
   missing values, and look at correlations between individual attributes and the
   target rating.
2. **Feature engineering** — select/scale the relevant numeric attributes; encode
   any categorical fields (e.g. position) if used.
3. **Linear Regression baseline** — fit a straightforward linear model and evaluate it.
4. **Polynomial Regression** — expand features to degree 2/3 polynomial terms and
   refit, comparing against the linear baseline.
5. **Model evaluation** — compare models using RMSE, MAE, and R² on a held-out test
   set, and check for overfitting as polynomial degree increases (train vs. test
   error gap).
6. **Visualization** — actual-vs-predicted plots, residual plots, and an
   error-vs-polynomial-degree curve to justify the final model choice.

### Results
*(Fill in with your actual numbers once the notebook is finalized — e.g. final
model, RMSE/R² on the test set, and the polynomial degree that generalized best.)*

### How to run
```bash
cd player-rating-regression
pip install numpy pandas scikit-learn matplotlib seaborn
jupyter notebook player_rating.ipynb
```

---

## 3. PCA From Scratch — Dimensionality Reduction

### Overview
An implementation of Principal Component Analysis (PCA) built directly on top of
NumPy, split into two parts:

- **Task 2.2 — Implement PCA.** Mean-center the data, compute the covariance
  matrix, eigendecompose it (`np.linalg.eigh`), sort by eigenvalue, and project
  the data onto the top-k eigenvectors. Verified against scikit-learn's `PCA` —
  explained variance and the transformed coordinates match exactly (up to the
  sign ambiguity inherent to eigenvectors).
- **Task 2.3 — Apply PCA.** Run the from-scratch implementation on the
  scikit-learn `digits` dataset (1,797 samples, 64 features):
  - A scree plot and cumulative explained-variance curve, showing how many
    components are needed to capture 90%/95% of the total variance.
  - A 2D projection of the full dataset, colored by digit label.
  - Reconstruction error (MSE) as a function of how many components are kept,
    plus a visual original-vs-reconstructed comparison for a handful of digits.

### Results
On the digits dataset: the first 2 components explain roughly 28% of total
variance combined; ~21 components are needed to reach 90% of the variance and
~29 for 95% (out of 64 original features) — a solid ~2-3x compression before
losing meaningful information. Reconstruction error drops sharply between
`k=1` and `k=20`, then flattens out.

### How to run
```bash
cd pca
pip install numpy scikit-learn matplotlib
jupyter notebook "Task2.2&2.3_PCA.ipynb"
```

---

## Requirements

Both projects use standard Python data-science tooling:

```
numpy
pandas
scikit-learn
matplotlib
seaborn
torch
torchvision
jupyter
```

Install everything at once with:
```bash
pip install -r requirements.txt
```

## License
MIT — feel free to use or adapt for coursework/learning purposes.
