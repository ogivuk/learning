# Logistic Regression

Logistic regression is a classification algorithm, and
it is among the most popular and widely used algorithms today.

## Model

Notation:

* n = number of features
* m = number of training examples
* x<sub>j</sub><sup>(i)</sup> = value of feature j in i<sup>th</sup> training example
* x<sup>(i)</sup> = input (features) of i<sup>th</sup> training example
* Training set: { (x<sup>(1)</sup>,y<sup>(1)</sup>), (x<sup>(2)</sup>,y<sup>(2)</sup>), ... , (x<sup>(m)</sup>,y<sup>(m)</sup>) }

Hypothesis:

* Goal: 0 ≤ h<sub>θ</sub>(x) ≤ 1
* h<sub>θ</sub>(x) = g(θ<sup>T</sup>x)
    * where g(z) = 1 / (1 + e<sup>-z</sup>)
    * g(z) is known as Sigmoid function or also as Logistic function, 
    and it maps any real number to the (0,1) interval.
    * g(z) ≥ 0.5, when z ≥ 0
* h<sub>θ</sub>(x) = 1 / (1 + e<sup>-θ<sup>T</sup>x</sup>)
* Interpretation of hypothesis output:
    * h<sub>θ</sub>(x) = estimated probability that y = 1 on input x parameterized by θ.
    * h<sub>θ</sub>(x) = P( y = 1 | x ; θ)
* Output of h<sub>θ</sub>(x) is translated as:
    * h<sub>θ</sub>(x) ≥ 0.5 -> y = 1
    * h<sub>θ</sub>(x) < 0.5 -> y = 0
* Based on the Sigmoid function property:
    * h<sub>θ</sub>(x) ≥ 0.5, whenever θ<sup>T</sup>x ≥ 0
    * y = 1, whenever θ<sup>T</sup>x ≥ 0
    * y = 0, whenever θ<sup>T</sup>x < 0
* Decision boundry is a property of hypothesis and it is:
    * the line that separates the region where the hypothesis predicts that y = 1 from the region where the hypothesis predicts that y = 0
    * set of points where h<sub>θ</sub>(x) = 0.5

Cost function:

* J(θ) = 1/m ∑<sub>i=1</sub><sup>m</sup> Cost( h<sub>θ</sub>(x<sup>(i)</sup>), y )
* J(θ) from linear regresion would be non-convex for logistic regression
* Cost( h<sub>θ</sub>(x), y ) = 
    * -log(h<sub>θ</sub>(x)), if y = 1
    * -log(1 - h<sub>θ</sub>(x)), if y = 0
    * -y log( h<sub>θ</sub>(x) ) + (1-y) log(1 - h<sub>θ</sub>(x))
* Properties:
    * it is always convex for logistic regression
    * if h<sub>θ</sub>(x) = y, Cost( h<sub>θ</sub>(x), y ) = 0
    * as h<sub>θ</sub>(x) -> 0 for y = 1, Cost -> ∞
    * as h<sub>θ</sub>(x) -> 1 for y = 0, Cost -> ∞