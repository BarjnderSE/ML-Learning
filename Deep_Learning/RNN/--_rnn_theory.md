https://stanford.edu/~shervine/teaching/cs-230/cheatsheet-recurrent-neural-networks

# Recurrent Neural Networks (RNNs) and Key Terminology

## What is an RNN?
A **Recurrent Neural Network (RNN)** is a type of neural network designed for processing sequential data. Unlike regular neural networks, RNNs have loops that allow information to be passed from one step to the next, making them great for tasks like language processing, time series prediction, and speech recognition.

## Key Terminology in RNNs

1. **Hidden State (h)**:
   - This is the memory of the RNN that stores information from previous time steps. It helps the network remember past inputs.

2. **Input (x)**:
   - The data fed into the RNN at each time step (e.g., a word, a stock price).

3. **Output (y)**:
   - The result or prediction of the RNN at each time step.

4. **Weights (W, U)**:
   - These are learnable parameters in the RNN that help transform the input and hidden state to generate the next hidden state and output.

5. **Activation Function (f)**:
   - A function (like **tanh** or **ReLU**) applied to the input and hidden state to introduce non-linearity.

6. **Time Steps**:
   - The RNN processes data step by step. Each step is a **time step**, where the model updates its hidden state and makes a prediction.

7. **Backpropagation Through Time (BPTT)**:
   - A method used to train RNNs, where the gradients of the error are propagated back through time to update the weights.

8. **Vanishing Gradient Problem**:
   - A problem where gradients become very small as they are backpropagated through many time steps, making it difficult for the network to learn long-term dependencies.

9. **Long Short-Term Memory (LSTM)**:
   - A type of RNN that uses special gates to better remember long-term information and solve the vanishing gradient problem.

10. **Gated Recurrent Unit (GRU)**:
    - A simpler version of LSTM that also handles long-term dependencies but with fewer parameters.

## Libraries to Use for RNNs

- **TensorFlow**:
   - Library: `tensorflow`
   - Use: Popular for building RNNs, LSTMs, and GRUs. Provides high-level APIs like `Keras` for easy model building.
   - Example:
     ```python
     from tensorflow.keras.models import Sequential
     from tensorflow.keras.layers import SimpleRNN, LSTM, GRU
     ```

- **PyTorch**:
   - Library: `torch`
   - Use: Another popular deep learning library for building and training RNNs, LSTMs, and GRUs. It provides a lot of flexibility for custom model designs.
   - Example:
     ```python
     import torch
     import torch.nn as nn
     
     class RNNModel(nn.Module):
         def __init__(self):
             super(RNNModel, self).__init__()
             self.rnn = nn.RNN(input_size=10, hidden_size=20, num_layers=2)
     ```

- **Keras**:
   - Library: `tensorflow.keras`
   - Use: Keras provides simple and user-friendly APIs to build RNN models with LSTM, GRU layers.
   - Example:
     ```python
     from tensorflow.keras.models import Sequential
     from tensorflow.keras.layers import LSTM
     ```

## Summary
RNNs are great for sequential tasks where past information matters. They use **hidden states** to remember previous inputs, and are trained using **BPTT**. **LSTM** and **GRU** are advanced versions of RNNs that solve issues like the **vanishing gradient problem**.

Let me know if you need more details on any specific topic!
