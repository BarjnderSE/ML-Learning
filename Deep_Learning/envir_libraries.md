# Setting Up a Machine Learning Environment

```bash
# Create the ML environment
conda create -n ml_env python=3.8

# Activate the environment
conda activate ml_env

# Install essential libraries for machine learning
conda install numpy pandas matplotlib seaborn scikit-learn
conda install -c conda-forge jupyter  # Optional, for Jupyter Notebook


# Setting Up TensorFlow and PyTorch Environments

```bash
# TensorFlow Environment
conda create -n tf_env python=3.8
conda activate tf_env
conda install tensorflow
conda install numpy pandas matplotlib seaborn scikit-learn
conda install -c conda-forge opencv  # Optional, for computer vision tasks
conda install -c conda-forge jupyter  # Optional, for Jupyter Notebook
python -c "import tensorflow as tf; print(tf.__version__)"

# PyTorch Environment
conda create -n torch_gpu python=3.8
conda activate torch_gpu
conda install pytorch torchvision torchaudio -c pytorch
conda install numpy pandas matplotlib seaborn scikit-learn
conda install -c conda-forge opencv  # Optional, for computer vision tasks
conda install -c conda-forge jupyter  # Optional, for Jupyter Notebook
python -c "import torch; print(torch.__version__)"