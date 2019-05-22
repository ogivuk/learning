# Linear Regression

Linear regression is a great algorithm for regression problems, which aim to predict continuous valued output.
However, applying linear regression to classification problems is often not a good idea.

## Model

Notation:

* n = number of features.
* m = number of training examples.
* x<sub>j</sub><sup>(i)</sup> = value of feature j in the i<sup>th</sup> training example.
* x<sup>(i)</sup> = input (features) of the i<sup>th</sup> training example.
* X = the design matrix of size of m x (n+1) with all feature values for all training data. Row i of X contains values of all features for the i<sup>th</sup> training example, including x<sub>0</sub><sup>(i)</sup>=1 so that X(:,1)=1.
* y<sup>(i)</sup> = resulting (output) value for the i<sup>th</sup> training example.
* y = vector of size m containing resulting (output) values for all training data.

Multivariate linear regression:

* Hypothesis:
  * h<sub>θ</sub>(x) = θ<sub>0</sub>·x<sub>0</sub> + θ<sub>1</sub>·x<sub>1</sub> + θ<sub>2</sub>·x<sub>2</sub> + ... + θ<sub>n</sub>·x<sub>n</sub>
    * x<sub>0</sub> = 1, for convenience
  * h<sub>θ</sub>(x) = θ<sup>T</sup>·x
    * θ is n+1 dimensional vector of parameters
    * x is n+1 dimensional vector of features
* Cost function:
  * J(θ) = 1/(2m)·∑<sub>i=1</sub><sup>m</sup> (h<sub>θ</sub>(x<sup>(i)</sup>) - y<sup>(i)</sup>)<sup>2</sup>

Polynomial Regression:
  * Making hypothesis function to be quadratic, cubic, square root, etc.
  * Creating additional features based on existing features
  * Examples of making h_θ(x) to be
    * quadratic: h_θ(x) = θ_0 + θ_1·x_1 + θ_2·x_2, where x_2 = x_1^2
    * cubic: h_θ(x) = θ_0 + θ_1·x_1 + θ_2·x_2 + θ_3·x_3, where x_3 = x_1^3
    * square root: h_θ(x) = θ_0 + θ_1·x_1 + θ_2·x_2, where x_2 = √x_1
  * Multiple features can be combined into one, e.g., x_3 = x_1·x_2 
  * Feature scaling is increasingly important for gradient descent.

## Finding Parameters

### Gradient Descent

* Algorithm: repeat the following until convergence
  * θ_j := θ_j - α·1/m·∑_{i=1}^{m} (h_θ(x^(i)) - y^(i))·x<sub>j</sub><sup>(i)</sup>; for j:=0...n
  * simultaneously update all θ_j
  * it is common to declare convergence if J(θ) decreases by less than 0.001 in 1 iteration
* the chosen cost function is always convex -> only one (global) minimum is always reached.
* "batch" gradient descent: each step of gradient descent uses all training examples.
* Practical tips:
  1. Have all input values in roughly the same range for faster convergance. θ descends quickly on small ranges and slowly on large ranges.
    * Can be achieved through feature scaling and mean normalization
    * Feature Scaling - dividing the input values by the range (i.e. the maximum value minus the minimum value) of the input variable, resulting in a new range of just 1.
    * Mean normalization - subtracting the average value for an input variable from the values for that input variable resulting in a new average value for the input variable of just zero.
    * x_i := (x_i - μ_i)/s_i
      * μ_i is the average of all the values for feature (i), and
      * s_i can be the range of values (max - min) or the standard deviation.
  2. Use smaller α if J(θ) is increasing - it is possible that the gradient descent is overshooting the minimum.
    * too small α -> slow convergence
    * too large α -> J(θ) may not decrease with every iteration, and it may even diverge
    * To choose α, try different numbers such as 0.001, 0.003, 0.01, 0.03, 0.1, 0.3, 1

### Other Optimization Algorithms

Given θ and ways to compute J(θ) and partial derivaties of J(θ), the following algorithms can be also used instead of Gradient descent:

* Conjugate gradient
* BFGS
* L-BFGS

Their advantages are:

* No need to manually pick the learning rate α
* Often faster than Gradient descent

Their disadvantages:

* More complex than Gradient descent to implement, but they can be just used out-of-the-box

In Octave, they can be utilized by using the function *fminunc(...)* and providing a function that calculates J(θ) and partial derivaties of J(θ).

### Normal Equation

* Analytical way of calculating the parameters, no iterations.
* Minimize the cost function J(θ) by setting to zero all its partial derivatives with respect to every θ_j.
* θ = (X^T·X)^(-1)·X^T·y
* There is no need to do feature scaling with the normal equation.
* Normal Equation is prefered when n is not very large, e.g., n<10000, since the matrix inverse is an expensive operation with the complexity of O(n^3), where n is the size of the matrix.
* If X^T·X is noninvertible:
  * It is probably due to redundant features, where two or more features are very close (linearly dependent), or due to too many features (e.g. m ≤ n).
  * Solutions include deleting a feature that is linearly dependent with another or deleting one or more features when there are too many features.
  * Use 'pinv' rather than 'inv' in Octave, as 'pinv' gives θ even if X^T·X is not invertible.