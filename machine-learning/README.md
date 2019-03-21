# Machine Learning

## What is Machine Learning

There is no well accepted definition of what is and what is not machine learning. Here are some examples of the ways that people have tried to define it:

* Arthur Samuel (1959), Machine Learning: "Field of study that gives computers the ability to learn without being explicitly programmed."
* Tom Mitchell (1998), Well-posed Learning Problem: "A computer program is said to learn from experience E with respect to some task T and some performance measure P, if its performance on T, as measured by P, improves with experience E."

## Supervised Learning

In supervised learning, there is a given data set with already known correct output for input values.

Supervised learning problems are categorized into regression and classification problems:

* Regression problem: predict continuous valued output.
* Classification problem: predict discrete valued output.

## Unsupervised Learning

Unsupervised learning is used when there is a need to derive structure from data with little or no idea what the results should look like.

Examples of unsupervised learning:

* Clustering: cluster given data points into groups that are somehow similar or related by different variables.
* Non-clustering (Cocktail Party Algorithm): find structure in a chaotic environment.

## Model

Notation:

* x_i - input variable/feature.
* X - space of input values.
* y_i - output variable.
* Y - space of output values.
* (x_i,y_i); i=1,...,m - training set with *m* examples.

**Hypothesis function h(x)** is a predictor for the corresponding value of y for a given x:

* h : X → Y

**Cost function J(θ)** measures the accuracy of our hypothesis function:

* Mean squared error.
* $J(θ) = 1/(2m) ∑ (h_θ(x_i) - y_i)^2$ - sum over all *m* examples.
* The mean is halved (1/2) as a convenience for the computation of the gradient descent.
* The goal is to minimize the cost function by choosing the best values of θ.

**Gradient Descent** is used to estimate the parameters in the hypothesis function:

* Using derivative (the tangential line to a function) of the cost function.
* The derivative (slope of the tangent) gives the direction with the steepest descent towards minimizing the cost functions.
* The algorithm makes steps down the cost function in the direction with the steepest descent, and the size of each step is determined by the parameter α (the learning rate).
* Depending on where one starts, one could end up at different points in the end.
* The gradient descent algorithm is to repeat the following until convergence:
* θ_j := θ_j - α ∂/∂θ_j J(θ), where *j=1..n* represents the feature index number.
  * At each iteration, one should simultaneously update all parameters θ_j. The derivative for all is done at the same point.
  * If α is too small, gradient descrent can be slow.
  * If α is too large, gradient descrent may overshoot the minimum. It can fail to converge, or it can even diverge.

## Literature

* [Machine Learning by Stanford University on Coursera](https://www.coursera.org/learn/machine-learning)