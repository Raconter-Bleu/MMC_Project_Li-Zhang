# scénario



## Nabla operator

This video introduce the nabla operator....--00

In the Cartesian, the gradient of the function $$f(x,y,z)$$ at point ($$x_0,y_0,z_0$$) can be written as a vector-01
$$
(\frac{\partial f}{\partial x},\frac{\partial f}{\partial x},\frac{\partial f}{\partial x} )|_{x=x_0,y=y_0,z=z_0}
$$
so the gradient function of function $f$ is-02
$$
\nabla f = \begin{pmatrix} \vec{i} & \vec{j} & \vec{k}\end{pmatrix}\begin{pmatrix} \frac{\partial}{\partial x} \\\frac{\partial}{\partial y} \\\frac{\partial }{\partial z} \end{pmatrix}
 = \vec{i}·\frac{\partial f}{\partial x}+\vec{j}·\frac{\partial f}{\partial x}·+\vec{k}·\frac{\partial f}{\partial x}
$$
Where $\begin{pmatrix} \frac{\partial}{\partial x} \\\frac{\partial}{\partial y} \\\frac{\partial}{\partial z} \end{pmatrix}$ is $\nabla$ and it was named as nabla operator. And this gradient function $$\nabla f$$ constitutes the vector field in three-dimensional space --03

### Nabla operator and coordinate transformation  ---04



Consider we have a new three-dimention coordinate system whose basis vector is $\begin{pmatrix} \hat{e_1} & \hat{e_2} & \hat{e_3}\end{pmatrix}^T$, We set a point to be $\begin{pmatrix} e_1 & e_2 & e_3\end{pmatrix}^T$, and another point to be $\begin{pmatrix} e_1+de_1 & e_2+de_2 & e_3+de_3\end{pmatrix}^T$.  ---05

After that we define that 
$$
d\vec{l}=\begin{pmatrix} e_1 & e_2 & e_3\end{pmatrix} \begin{pmatrix} f_1de_1 \\ f_2de_2 \\ f_3de_3\end{pmatrix} = \sum_{i}\hat{e_i}f_ide_i
$$
where $f_i(e_1,e_2,e_3)$ is the metric function we introduced 

In order to introduce the nabla operator, we also need to set a scalar function $T$
$$
dT=\sum_i \frac{\partial T}{\partial e_i}de_i
$$
Then we can import the previous $d\vec{l}$    ---06
$$
dT= \nabla T \cdot d\vec{l} =\sum_i (\nabla T)_if_ide_i
$$
So we can derive  
$$
\nabla T=\sum_i \frac{1}{f_i}\frac{\partial T}{\partial e_i}
$$
In other coordinate system, it can be expressed as
$$
\nabla T=\sum_i \hat{e_i} \frac{1}{f_i}\frac{\partial T}{\partial e_i}
$$
So the next problem to be solved is, how to find a suitable metric function?
Metric tensors are a broader discussion ----07

### Metric tensors in different coordinate systems



A metric tensor is a second-order tensor in Riemannian geometry used to measure matrices, areas, and angles in a metric space.
The introduction of a metric tensor must be considered, no matter how the coordinate system is selected, it cannot affect the measurement result in this case.----08
The metric tensor is represented as
$$
ds^2=\sum_{i j}g_{ij}de_ide_j
$$
Under this definition, the arc length from point a to point b is defined as L -----09
$$
L = \int_a^b\sqrt{\sum_{i j}g_{ij}\frac {dx_i}{dt}\frac {dx_j}{dt}}dt
$$
If there exists a differential homeomorphism $f$ from $R^n$ to $R^n$, then metric tensor G is ---10
$$
G = J^TJ
$$
where $J$ is the Jacobian matrix

Then, in common coordinate systems, they can be represented as follows

1.polar coordinate system, independent variables $\rho$ and $\phi$
$$
\left\{  
             \begin{array}{lr}  
             x=  \rho cos\phi
             \\   
             y=     \rho sin\phi
             \end{array}  
\right.
$$
Jacobian matrix ----11
$$
J = \frac{\partial (x,y)}{\partial (\rho,\phi)} = \begin{pmatrix} cos\theta & -\rho sin\theta \\ sin\theta&\rho cos\theta \end{pmatrix}
$$
then metric tensor 
$$
G = J^TJ = \begin{pmatrix} cos\theta &  sin\theta \\ -\rho sin\theta&\rho cos\theta \end{pmatrix} \begin{pmatrix} cos\theta & -\rho sin\theta \\ sin\theta&\rho cos\theta \end{pmatrix} =  \begin{pmatrix} 1 & 0 \\ 0&\rho^2 \end{pmatrix}
$$
then -----12
$$
f_1=1,f_2=\rho
$$
2.For the spatial cylindrical coordinate system$\rho,\phi,z$, therefore
$$
f_1=1,f_2=\rho,f_3=1
$$
3.For the space spherical coordinate system$\rho,\theta,\phi$, therefore
$$
f_1=1,f_2=r,f_3=r sin\theta
$$

#### Physical meaning

I will try to explain one of the physical meanings of the nabla operator in mechanics. 

The example I use is the continuity equation in fluid mechanics.

From a macro perspective, we can write the integral form of the continuity equation. ---13
$$
-\iiint_\limits {CV} \frac{\partial\rho}{\partial t}dB= \oiint \rho(\vec{V}\cdot\vec{n})dA
$$
The left side of the equation is the mass that is reduced in the control body, and the right side of the equation is the mass that flows out of the control body. 

Differentiating this equation in integral form, we can get the continuity equation in differential form with the Nabla operator.--14
$$
\frac{\partial \rho}{\partial t}+\nabla\cdot(\rho\vec{V})=0
$$
Through the perspective of differentiation, we can describe the changes in mass in this tiny space in detail.

![image-20220426155838440](C:\Users\Surface-LEO\AppData\Roaming\Typora\typora-user-images\image-20220426155838440.png)

In this tiny space, the reduction in mass is equal to
$$
-\frac{\partial m }{\partial t}=-\frac{\partial\rho}{\partial t}dxdydz
$$
Net outflow in the x-axis
$$
\frac{\partial (\rho u)}{\partial x}dxdydz
$$
Net outflow in the y-axis
$$
\frac{\partial (\rho v)}{\partial y}dxdydz
$$
Net outflow in the z-axis
$$
\frac{\partial (\rho w)}{\partial z}dxdydz
$$
The total net outflow from the control body is
$$
[\frac{\partial (\rho u)}{\partial x}+\frac{\partial (\rho v)}{\partial y}+\frac{\partial (\rho w)}{\partial z}]dxdydz
$$
Therefore, the meaning of the nabla operator is the events that occur in the x, y and z directions respectively. In this physical scenario, it represents the outflow of mass in the x, y and z directions respectively---15



## Lapacian

And next part we will introduce the laplacian and its mathmatical and physical meaning. --00

### Divergene



Before explaining Laplace, it is necessary to introduce divergence and flux. Divergence needs to be explained in terms of flux. Among this equation, $ \Sigma$ indicates a curved surface in a space,  $\vec{n}$ is the normal vector $dS$, and $\vec{A}$ is the physic vector acting on the area element.--01
$$
\Phi_A(\Sigma) = \oint_\Sigma \vec{A}· \vec{n}dS
$$
When our surface is spatially closed, such as a sphere, then the normal vector has a problem of whether pointing inside or outside the sphere. When we define divergence, we just agree that the normal vector uniformly points to the outside of the sphere, repeat, the normal vector points outside.--02

The flux of this sphere can still be expressed by the former equation. It is worth noting that if the vector field within this sphere is uniformly outward from the center, then the total flux for this sphere is zero, because the oppositely directed fluxes on the sphere cancel out. --03

。。。。

Based on the above description of flux, we can describe divergence in terms of flux. Suppose we have such a vector field--04

![image-20220403184834235](C:\Users\lzz20\AppData\Roaming\Typora\typora-user-images\image-20220403184834235.png)

In this vector field, the total flux on the red surface is negative and the total flux on the green surface is positive. We keep shrinking the two surfaces until they are infinitely close to a point {$x$}, then we divide their total flux by the volume $\delta V$ enclosed by the surfaces--05

$$
\nabla A = \lim\limits_{\delta V \to x}\frac{\Phi_A(\Sigma)}{\delta V}
$$
We then get the divergence at point {$x$}

We can also easily find that the divergence at the center of the red circle is negative, and the divergence at the center of the green circle is positive. In fact, divergence measures how much a vector field at a point is emitted or absorbed. --06

For a point with positive divergence, if its divergence is larger, it means that the vector field diverges strongly here. If the point divergence is negative, the corresponding vector field is considered to converge here.--07



### Laplacian

The Laplacian of a function $f$ can be written as

 $$\nabla ^2f$$ or  $$\nabla · \nabla f$$,

---08



It is defined as the divergence of the gradient of the function , F. The value of the Laplacian of a certain vector field just like a mountain, according to the definition of gradient, around the peak, all gradient vectors converge towards the peak, so the Laplacian at each peak is negative. --09

![image-20220403195227611](C:\Users\lzz20\AppData\Roaming\Typora\typora-user-images\image-20220403195227611.png)

And around the valleys, all gradients diverge from here, so the Laplacian at each valley is positive. So, for a function, the Laplacian measures whether the gradient of the function tends to increase or decrease at each point in space.--10

### Math meaning

The former figure shows only the most obvious meaning. The Laplacian operator has more meaning than that, that is, it describes the difference between the average value of the scalar field near a point and the function value of the point.To figure this out, let's start with the one-dimensional case. .  --11

$$
\nabla^2u = \frac{d^2u}{dx^2}
$$
The Laplacian in one dimension is the second derivative. The derivative can be approximated by the difference, this can be proved by mathematical induction and Lagrange's mean value theorem:--12
$$
\Delta ^n u = f^{(n)}(\xi_n)\Delta x^n
$$
therefore:

$$
\frac{d^2u}{dx^2} = \frac{d^2u}{dx^2}
$$
In this way, we may not feel the geometric meaning of the second derivative. I want to use the difference mentioned above to approximate the second derivative, maybe this can make its geometric meaning more intuitive.----13
$$
\frac{d^2u}{dx^2} = \frac{\Delta^2u}{\Delta x^2} = \frac{[u(x+\Delta x)-u(x)]-[u(x)-u(x-\Delta x)]}{\Delta x^2}\\ =  \frac{2}{\Delta x^2} [\frac{u(x+\Delta x)+u(x-\Delta x)}{ 2}-u(x)]
$$


In this way, we can clearly see that the square brackets are the difference between the average value of u in the neighborhood of x and u(x). We can clearly see the geometric meaning of laplacian here, which is important, especially when understanding its meaning. ----14



For multidimensional cases, it can also be generalized.
$$
\delta = \frac{1}{r^2}[\frac{\oint_{S_{r}(x)}u(x+\vec{r})dS}{S}-u(x)]
$$
At this ime, the meaning of the expression is the difference between the average value of the function u in the field of x (which is a sphere, denoted as $S_{r}(x)$) and u(x), and the $ \frac{1}{r^2} $ factor introduced is for the category $\frac{1}{\Delta x^2}$

At this ime, the meaning of the expression is the difference between the average value of the function ,U, in the field of  sphere---15



let's continue to derive the expression of delta and get its integral form,
$$
\begin{aligned}
&\delta=\frac{1}{r^2}[\frac{\oint_{S_{r}(x)}u(x+\vec{r})dS}{S}-u(x)]\\ &=\frac{1}{Sr^2} \oint_{S_{r}(x)}[u(x+\vec{r})-u(x)]dS\\ &\approx \frac{1}{Sr^2} \oint_{S_{r}(x)}\nabla u(x+\vec{r})\cdot \vec{r}dS\\ &= \frac{1}{Sr^2} \oint_{S_{r}(x)}\nabla u\cdot r\vec{n}dS
\end{aligned}
$$
...

And after that, in order to continue, next we're going to use a theorem, in one dimension it's called the Newton-Leibniz theorem
$$
\int^b_au'(x)dx = u(b)-u(a)
$$

And in multiple dimensions it's called the Fundamental Theorem of Calculus---16
$$
\int_V u_{x_i}dV = \int_{\partial V}un^idS
$$

$$u = f(x_1,x_2,...,x_n)$$ is a six-dimensional function, $u_{x_i}$ is the partial derivative with respect to $x_i$, and $dV$ is the boundary of the n-dimensional space $V$. This boundary is not necessarily closed, so the integral symbol does not necessarily have to draw a circle. $n^i$ is the i$^{th}$ unit normal vector pointing out of $dV$

...

Let's go back to the previous derivation, By using the Fundamental Theorem of Calculus, we can get
$$
\delta = \frac{1}{Sr^2} \oint_{S_{r}(x)}\nabla u\cdot r\vec{n}dS \approx \frac{1}{Sr} \oint_{B_{r}(x)}\nabla ^2 udV
$$
Here $B_r(x)$ means an N-dimension ball. ---17

For the integral part, if we taking the limit of $r\to0$, it can be done like this--18
$$
\int_V\nabla ^2 udV \to \nabla^2u(x)\times V
$$
And for an n-dimensional ball, V, equals , S,  plus, R, over ,N . And therefore we can get the fina expression which only differs from the Laplace operator by only a constant factor ,N . ---19
$$
V = \frac{Sr}{n}
$$
$$
\delta=\frac{1}{n}\nabla^2u
$$
### 



When the Laplace operator of our one physical quantity equals to zero, then this degenerates into the Laplace equation.The Lapace equation is the equation that needs to be satisfied by the real and imaginary parts of the analytic function in the complex variable function. --20

#### **Laplace equation**


$$
\nabla^2\phi = 0
$$
 Now we know that the Laplace equation describes one thing: the function phi is uniform at every point in space, that is, the value of each point is equal to the average value in its neighborhood. This is also why the solutions of the Laplace equations are called harmonic functions--21

Just like this equantion
$$
\phi(x) = \frac{1}{|S_r(x)|}\oint_{S_r(x)}udS =  \frac{1}{|B_r(x)|}\int_{B_r(x)}udV
$$
Mathematicians can, by some tricks, convert the local properties of functions to the extended properties of functions, in other words, from differential expression to integral expression. The local averageness of a harmonic function can be converted to averageness over a range.--22

Simply speaking, we can enlarge the previous infinitely small neighborhood into a finitely large sphere, and the harmonic function is equal to the function value at the center of the sphere whether it is averaged on the sphere or on the entire sphere.--23

There are many well-known inferences about the average properties of harmonic functions, which will not be introduced here.--24



After that, we will use the law of heat conduction to explain the physical meaning of the Laplace operator.--25





#### Heat conduction equation

$$
\frac{\partial T}{\partial t} = \alpha\nabla^2T(\alpha>0)
$$

where $T = T(x,y,z,t)$ is the temperature function of a region, describing the temperature of each point in the region at every moment. 

the Heat conduction process can be defined by using Laplace operator. In the equation, T is the temperature function of a region, describing the temperature of each point in the region at every moment.  --26

In the previous derivation, we know that the Laplacian has an average propertie that indicates The difference between the mean value of a point in its neighborhood and the value of this point.--27

So we can easily comprehend that the heat conduction equation is nothing more than saying that if the temperature at a point in space is lower  than the average temperature around it, then the temperature at that point will rise at a rate proportional to that difference.--28

Also, just from a mathematical point of view. The diffusion of matter, also known as Fick's law, is also described by the same point of view.--29

And that is end of the video, thanks for watching. --30

#### 

$$

$$



