# EasyTeX Problem Set


### Header Fields
<table class="tg">
  <tr>
    <th class="tg-e3zv">Field Name</th>
    <th class="tg-e3zv">Required/Optional</th>
  </tr>
  <tr>
    <td class="tg-031e">author</td>
    <td class="tg-031e">Required</td>
  </tr>
  <tr>
    <td class="tg-031e">collaborators</td>
    <td class="tg-031e">Optional</td>
  </tr>
  <tr>
    <td class="tg-031e">due_date</td>
    <td class="tg-031e">Optional</td>
  </tr>
  <tr>
    <td class="tg-031e">title</td>
    <td class="tg-031e">Optional</td>
  </tr>
  <tr>
    <td class="tg-031e">course</td>
    <td class="tg-031e">Optional</td>
  </tr>
  <tr>
    <td class="tg-031e">school</td>
    <td class="tg-031e">Optional</td>
  </tr>
</table>

### Problems
<table class="tg">
  <tr>
    <th class="tg-e3zv">Field Name</th>
    <th class="tg-e3zv">Required/Optional</th>
  </tr>
  <tr>
    <td class="tg-031e">label</td>
    <td class="tg-031e">Optional</td>
  </tr>
  <tr>
    <td class="tg-031e">statement</td>
    <td class="tg-031e">Required</td>
  </tr>
  <tr>
    <td class="tg-031e">solution</td>
    <td class="tg-031e">Required</td>
  </tr>
</table>

## General Layout
Note: all fields are left empty to illuminate EasyTeX's tabbed-delineation!

	problem_set:
		author:
		collaborators:
		due_date:
		title:
		course:
		school:
		
		problem:
			label:
			statement:
			
			solution:
			
		problem:
			label:
			statement:
				
			solution:
			

## Samples

### Problem Set with One Problem (all optional fields filled)

	problem_set:
	    author: Paul Dapolito
	    collaborators: Robert, Angela, Daniel
	    due_date: September 21, 2015
	    title: Basic Problem Set
	    course: Programming Languages
	    school: Harvey Mudd College

	    problem:
	        label: 1

	        statement:
	            What is the rate of change $f'$ of a function $f$ at the point $a$?

	        solution:
	            Suppose we have the model $M$ consisting of the set $A = \{\textrm{domestic cat, feline, mammal}\}$. Then, the
	            interpretation of ${\sim}$ is to be "is a". From this, we see that the first axiom $A0$ is satisfied, for
	            every domestic cat is a domestic cat, every feline is a feline, and every mammal is a mammal. Furthermore, we
	            see that the third axiom $A 2$ is satisfied, for if every domestic cat is a feline, and if every feline is a
	            mammal, then every domestic cat is a mammal. However, the axiom $A1$ does not hold, for it is not true that if
	            every domestic cat is a feline, then every feline is a domestic cat. Thus, we have found a model that
	            satisfies axioms $A0$ and $A2$, but not axiom $A1$. 


				
### Problem Set with Multiple Problems (some optional fields missing)

	problem_set:
	    author: Michael Libucha
	    collaborators: Paul, Rojesh

	    problem:
	        statement:
	            Sect 2.3 - \textbf{38.} Find an equation for the plane tangent to the graph of $z = 4 \cos xy$ at the point
	            $(\pi/3, 1, 2)$. 

	        solution: 
	            The given function $f(x,y)$ has the following second-order partial derivatives:
	            $$f_{x x}, f_{x y}, f_{y x}, f_{y y}$$

	            First, let us find the two first-order partial derivatives of the given function:
	            $$\frac{\partial f}{\partial x} = 2xe^{x^2+y^2}$$
	            $$\frac{\partial f}{\partial y} = 2ye^{x^2+y^2}$$

	            Now, let us now determine all of the second-order partial derivatives:
	            $$\boxed{f_{xx} = (4x^2\cdot e^{y^2} + 2e^{y^2})e^{x^2}}$$
	            $$\boxed{f_{xy} = 4xye^{y^2 + x^2}}$$
	            $$\boxed{f_{yx} = 4xye^{y^2 + x^2}}$$
	            $$\boxed{f_{yy} = (4y^2e^{x^2} + 2e^{x^2})e^{y^2}}$$

	    problem:
	        statement:
	            Section 2.5 - \textbf{22.}
	            Calculate $D(\textbf{f}\circ\textbf{g})$ in two ways:
	                \begin{enumerate}
	                    \item by first evaluating $\textbf{f}\circ\textbf{g}$ and
	                    \item by using the chain rule and the derivative matrices $D\textbf{f}$ and $D\textbf{g}$.
	                    \[
	                        f(x,y)=x^2-3y^2, \qquad \textbf{g}(s,t)=(st,s+t^2)
	                    \]
	                \end{enumerate}

	        solution:
	            Let us first define a function $F(x)$ as: 
	                $$F(x) = f(a + vx)$$
	            
	            By the definition of the directional derivative of $F$ at $a$,
	                $$D_v f(a) = \lim_{x \rightarrow 0} \frac{f(a + vx) - f(a)}{x} = \lim_{x \rightarrow 0} \frac{F(x) - F(0)}{x-0} = F'(0)$$
	            
	            Thus,
	                $$D_v f(a) = \frac{d}{dt} f(a + vx) |_{x = 0}$$

	            If we let $y(t) = a + vx$ and use the chain rule on the right side of our equation above $(\frac{d}{dt} f(a + vx))$,
	                $$\frac{d}{dx} f(a + vx) = Df(y) Dy(x) = Df(y) \cdot v$$
	            
	            We will now evaluate $Df(y) \cdot v$ at $x = 0$ to obtain
	                $$Df(a) \cdot v = \nabla f(a) \cdot v$$

	            Which directly implies that the directional derivative of $f(a)$ in the direction of $v$ $(D_{v} f(a) )$ is
	                $$D_{v} f(a) = \nabla f(a) \cdot v$$
	            QED.


