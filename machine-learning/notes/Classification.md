# Classification

The classification problem is just like the regression problem,
except that the values we now want to predict take on only discrete values.

There are two types of classification problems.

**Binary classification problem**

* where y ∈ {0,1}. 
* 0 is also known as negative class and 1 as positive class.
* 0 and 1 are also sometimes denoted as - and +, respectivelly.
* can be solved using the [Logistic Regression](Logistic\ Regression.md) algorithm.

**Multiclass Classification Problem**

* where y ∈ {0,1,2,...,n}
* can be solved by **One-versus-all** algorithm:
    * divides the problem into n+1 binary classification problems, each solving with e.g., [Logistic Regression](Logistic\ Regression.md), and then takes the prediction with the maximum probability:
    * h<sub>θ</sub><sup>(0)</sup>(x) = P( y=0 | x; θ)
    * h<sub>θ</sub><sup>(1)</sup>(x) = P( y=1 | x; θ)
    * ...
    * h<sub>θ</sub><sup>(n)</sup>(x) = P( y=0 | x; n)
    * prediction = max<sub>i</sub>( h<sub>θ</sub><sup>(i)</sup>(x) )
