# Deep Learning Course - 16th & 17th February

## 📚 Course Overview
This repository contains comprehensive learning materials from a Deep Learning course conducted on February 16th-17th, covering fundamental concepts of Artificial Neural Networks (ANN), implementation, and practical applications.

---


### 📁 **GITHUB Folder**
Contains practical implementation files and theoretical resources

#### **Day-/** (Main Practice Directory)

##### **Project Files:**
- **`Churn Modeling.ipynb`** - Complete Jupyter notebook implementing customer churn prediction using TensorFlow/Keras ANN
  - Dataset preprocessing and feature engineering
  - Neural network architecture with multiple hidden layers
  - Model training with 150 epochs
  - Accuracy: ~86.35%
  - Confusion matrix analysis

- **`Churn_Modelling.csv`** - Customer dataset (684 KB)
  - Contains customer information for churn analysis
  - Features: CreditScore, Geography, Gender, Age, Tenure, Balance, etc.

- **`streamlit_churn_modeling.py`** - Interactive web application for churn prediction
  - Built with Streamlit framework
  - Provides user interface for model predictions

##### **16th,17th - ANN THEORY, Installation/**
Comprehensive theoretical materials and setup guides:

**Environment Setup:**
- `steps to create tensorflow environment.txt` - Complete guide for:
  - Anaconda installation and configuration
  - TensorFlow environment creation
  - Library installations (Keras, PyTorch, OpenCV, etc.)
  - VS Code and PyCharm setup

**Theoretical Modules:**

1. **`1.Introduction to DL/`**
   - Fundamental concepts of Deep Learning
   - Contains 3 PNG diagrams illustrating key concepts

2. **`2.Architecture of Neural Network (ANN)/`**
   - Detailed neural network architecture diagrams
   - 3+ architectural illustrations (PNG format)

3. **`1. NN_ BACK PROPAGATION/`**
   - Backpropagation algorithm explained
   - 7 detailed diagrams (7.PNG through 13.PNG)

4. **`2. Multi NN training/`**
   - Multi-layer neural network training concepts
   - 5 explanatory diagrams

5. **`3. Chain rule/`**
   - Mathematical foundation for backpropagation
   - 8 step-by-step diagrams explaining chain rule

6. **`4. Activation Function/`**
   - Different activation functions (Sigmoid, ReLU, Tanh, etc.)
   - 10+ visual representations and comparisons

7. **`4. DROP OUT & REGULARIZATION/`**
   - Techniques to prevent overfitting
   - Dropout and regularization methods

8. **`CHURN MODELING- TF/`**
   - TensorFlow implementation resources for churn prediction

9. **`Practicle - CPU/`**
   - CPU-based implementation examples and exercises

---


## 🛠️ **Technologies & Libraries Used**

### Deep Learning Frameworks:
- **TensorFlow** (2.x)
- **Keras** (3.6.0)
- **PyTorch**

### Data Science Libraries:
- **NumPy** - Numerical computations
- **Pandas** - Data manipulation
- **Scikit-learn** - Preprocessing and metrics
- **Seaborn** - Data visualization
- **Matplotlib** - Plotting
- **SciPy** - Scientific computing

### Computer Vision & NLP:
- **OpenCV** - Image processing
- **Ultralytics** - YOLO implementation
- **MediaPipe** - Computer vision solutions
- **NLTK** - Natural language toolkit
- **spaCy** - Advanced NLP
- **Gensim** - Topic modeling

### Application Framework:
- **Streamlit** - Interactive web applications
- **LangChain** - LLM applications

---

## 📖 **Course Topics Covered**

### 1. **Deep Learning Fundamentals**
- Introduction to neural networks
- Difference between ML and DL
- Applications and use cases

### 2. **Neural Network Architecture**
- Input, hidden, and output layers
- Neurons and weights
- Forward propagation
- Network topology

### 3. **Activation Functions**
- Sigmoid
- Tanh
- ReLU (Rectified Linear Unit)
- Leaky ReLU
- Softmax
- When to use which activation function

### 4. **Training Neural Networks**
- Backpropagation algorithm
- Chain rule for gradients
- Loss functions (Binary Crossentropy, etc.)
- Optimization algorithms (Adam, SGD)

### 5. **Regularization Techniques**
- Dropout layers
- L1/L2 regularization
- Preventing overfitting
- Batch normalization

### 6. **Practical Implementation**
- Customer Churn Prediction Project
- Data preprocessing and encoding
- One-hot encoding for categorical variables
- Feature scaling with StandardScaler
- Model evaluation metrics
- Confusion matrix interpretation

---

## 💻 **Environment Setup**

### **Anaconda Installation:**
```bash
# Create TensorFlow environment
conda create -n tensorflow_env tensorflow

# Activate environment
conda activate tensorflow_env
```

### **Required Libraries:**
```bash
pip install keras==3.6.0
pip install --upgrade tensorflow
pip install torch
pip install opencv-python
pip install ultralytics
pip install mediapipe
pip install langchain
pip install scikit-learn
pip install nltk
pip install spacy
pip install numpy pandas seaborn scipy gensim
pip install streamlit
```

### **VS Code Virtual Environment:**
```bash
# Navigate to project directory
cd path/to/your/project

# Create virtual environment
python -m venv myenv

# Activate virtual environment
.\myenv\Scripts\activate

# Install required packages
pip install -r requirements.txt
```

---

## 🚀 **Getting Started**

### **Running the Churn Modeling Project:**

1. **Jupyter Notebook:**
   ```bash
   cd "GITHUB/Day-"
   jupyter notebook "Churn Modeling.ipynb"
   ```

2. **Streamlit Application:**
   ```bash
   cd "GITHUB/Day-"
   streamlit run streamlit_churn_modeling.py
   ```

---

## 📊 **Project Highlights: Churn Modeling**

### **Dataset Features:**
- Customer demographics (Age, Gender, Geography)
- Financial information (Credit Score, Balance, Estimated Salary)
- Banking behavior (Tenure, Number of Products, Credit Card, Active Member)
- **Target Variable:** Exited (0 = Stayed, 1 = Left)

### **Model Architecture:**
```
Input Layer (12 features after one-hot encoding)
    ↓
Hidden Layer 1 (6 neurons, ReLU)
    ↓
Hidden Layer 2 (6 neurons, ReLU)
    ↓
Hidden Layer 3 (5 neurons, ReLU)
    ↓
Hidden Layer 4 (4 neurons, ReLU)
    ↓
Output Layer (1 neuron, Sigmoid)
```

### **Training Configuration:**
- **Optimizer:** Adam
- **Loss Function:** Binary Crossentropy
- **Batch Size:** 32
- **Epochs:** 150
- **Train/Test Split:** 80/20

### **Model Performance:**
- **Accuracy:** ~86.35%
- **Confusion Matrix:**
  - True Negatives: 1541
  - False Positives: 54
  - False Negatives: 219
  - True Positives: 186

---

## 📝 **Learning Resources**

### **Theoretical Materials:**
All theoretical concepts are explained through:
- Visual PNG diagrams in respective topic folders
- Step-by-step illustrations
- Mathematical foundations
- Implementation examples

### **Video Lectures:**
- Complete lecture recordings in both full quality (.mkv) and compressed (.mp4) formats
- Separate sessions for theory and coding practice
- Duration: Multiple hours of comprehensive content

---

## 🎯 **Key Learning Outcomes**

After completing this course, you will understand:

✅ Fundamental concepts of Deep Learning and Neural Networks  
✅ How to design and implement ANN architectures  
✅ Various activation functions and their applications  
✅ Backpropagation and gradient descent algorithms  
✅ Regularization techniques to prevent overfitting  
✅ Data preprocessing for neural networks  
✅ Model evaluation and performance metrics  
✅ End-to-end implementation of real-world ML projects  
✅ Deployment using Streamlit web framework  
✅ Environment setup for Deep Learning projects  

---

## 🔧 **Tools & IDEs Used**

- **Anaconda Navigator** - Environment management
- **Jupyter Notebook** - Interactive development
- **VS Code** - Code editing and debugging
- **PyCharm** - Python IDE (optional)
- **Spyder** - Scientific Python IDE



**Happy Learning! 🚀📊🤖**
