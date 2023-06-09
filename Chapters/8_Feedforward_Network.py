#Feedforward Network: 

#The FeedForward class in the code represents a simple feedforward neural network. 
#It takes the number of embedding dimensions (n_embd) as an argument and defines a sequential neural network with two linear layers, 
#a ReLU activation function, and a dropout layer.

#The first linear layer projects the input to a higher dimensional space, and the ReLU activation function applies a non-linearity to the output. 
#The dropout layer randomly drops some of the activations to prevent overfitting. 
#Finally, the second linear layer projects the output back to the original dimensionality.

#Overall, the FeedForward class is used as part of the Transformer block to transform the output of the self-attention layer before passing it to the next layer in the network.

def __init__(self, n_embd):
    super().__init__()
    self.net = nn.Sequential(
        nn.Linear(n_embd, 4 * n_embd),
        nn.ReLU(),
        nn.Linear(4 * n_embd, n_embd),
        nn.Dropout(dropout),
    )

def forward(self, x):
    return self.net(x)

