# Cats vs Dogs Classification with CNNs and Transfer Learning

## Project Overview
This project explores image classification using Convolutional Neural Networks (CNNs) on the Cats vs Dogs dataset.

The goal is to:
- build a CNN from scratch
- improve it with data augmentation and regularization
- compare it with a pretrained model (transfer learning)

---

## Dataset
- Binary classification: Cat vs Dog
- Images resized to 128×128 (CNN) and 224×224 (ResNet)
- Train / validation / test split

---

## Models

### 1. Baseline CNN
- Simple convolutional architecture
- Trained from scratch
- Result: ~80% accuracy

---

### 2. Improved CNN
- Data augmentation:
  - random horizontal flip
  - random resized crop
- Regularization:
  - dropout
  - weight decay

Result: ~81–85% accuracy

---

### 3. Transfer Learning (ResNet18)
- Pretrained on ImageNet
- Backbone frozen
- New classifier head trained

Result: ~97% accuracy

---

## Results

| Model | Accuracy |
|------|--------|
| MLP | ~70% |
| CNN | ~81% |
| CNN + Augmentation | ~85% |
| ResNet18 (Transfer Learning) | ~97% |

---

## Key Observations

- CNN significantly outperforms MLP on image data
- Data augmentation improves generalization
- Regularization had limited impact in this setup
- Transfer learning provides a major performance boost

---

## Example Outputs

### Confusion Matrix
Confusion Matrix

### Predictions
Predictions

---

## Key Takeaways

- Training CNNs from scratch requires large datasets
- Transfer learning is extremely effective for small datasets
- Pretrained models already capture rich visual features
- Validation curves are critical to detect overfitting

---

## Tech Stack
- Python
- PyTorch
- NumPy
- Matplotlib

---

## Possible Improvements
- Fine-tuning deeper layers of ResNet
- Grad-CAM for model interpretability
- Hyperparameter tuning (learning rate, architecture)