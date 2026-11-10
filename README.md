# Tommy Lab

A Python toolkit for practising Data Analytics laboratory experiments.

This package is a renamed/repackaged continuation of the Gomma Lab project. Original project attribution is retained.

## Experiments

1. Gradient Descent
2. Linear and Binary Search
3. K-Means Clustering
4. SVM Classification
5. Image Classification using ResNet50
6. LSTM Time Series Prediction

## Installation

```bash
pip install tommy-lab
```

## Usage

Display all six complete experiment programs:

```bash
tommy-lab
```

The command prints each experiment's source code, including its execution block. Copy the relevant experiment into a Google Colab code cell and run it.

## Requirements

Python 3.9 or later. Dependencies are listed in `pyproject.toml`.

CNN and LSTM experiments require PyTorch. The CNN experiment downloads pretrained ResNet50 weights on first use and its upload example is designed for Google Colab.

## Individual experiment usage

### Gradient Descent

```python
from gomma_lab.gradient import gradient_descent, plot_gradient

history = gradient_descent()
plot_gradient(history)
```

### Searching Techniques

```python
from gomma_lab.searching import linear_search, binary_search

arr = [10, 20, 30, 40, 50]
print(linear_search(arr, 30))
print(binary_search(arr, 30))
```

### K-Means Clustering

```python
from gomma_lab.clustering import kmeans_clustering

kmeans_clustering()
```

### SVM Classification

```python
from gomma_lab.classification import svm_classification

svm_classification()
```

### Image Classification

```python
from gomma_lab.cnn import classify_image

classify_image("image.jpg")
```

### LSTM Time Series Prediction

```python
from gomma_lab.lstm import lstm_prediction

lstm_prediction()
```

## License

This project is distributed under the MIT License. See `LICENSE`.
