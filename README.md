<details open="open" align="center">
  <summary><h4 style="display: inline-block"><pre>Table of Contents    <i>--(Toggle)</i></pre></h4></summary>  
    <li><a href="#About Path Planning">About Path Planning</a></li>
    <li><a href="#Programming Tools">Engineering Tools</a></li>
    <li><a href="#Project Goals">Project Goals</a></li>
    <li><a href="#Assignments">Assignments</a></li>
    <li><a href="#Additional Tasks">Additional Tasks</a></li>
    <li><a href="#Reflective Essays">Reflective Essays</a></li>

  </ol>
</details>
<br><br>
<hr>
<div id="About Path Planning">

<h1>About Path Planning</h1>
<p align="center">
<tr><img src="Sources\March-World-small.gif" width="500" height="300" class="center">


Path planning can be characterized as a process to identify or predict an object's ability to move from the origin to the destination. With recent advancements in technology and digitalization, path planning has become exceptionally important in various industries. Path planning has been commonly used in aviation, robotics, computer gaming, and other transport-based industries. 

In commercial aviation, pilots have to do path planning before every flight in order to make sure that the flight route is possible to run through. Without a proper flight plan, the pilot will not be able to identify where the aircraft must fly in order to fly within optimal conditions. For example, without proper path planning, the pilot will not be able to identify regions with high turbulent wind that the aircraft may want to avoid. As a result, during this turbulent phase, the aircraft may experience significant drag increases, especially frictional and pressure drag. These problems may quickly compound and cause more problems, and may even cause some flight parameters to move outside the flight envelope. 

Aside from pilots, ATCs utilize path planning for commercial aviation as well, because they have to arrange flights around and in the airport too. Because of this, path-planning is really important to the aviation industry since it can ensure our safety and reduce flight costs.

Moving outside commercial aviation, path planning is also becoming increasingly important in future aeronautical applications such as Unmanned Aerial Vehicles, Drones, and Robotic Aircraft. Proper path planning algorithms must be made to ensure that these non-controlled machines can efficiently do the required work without manual operation. </tr>

<hr><br><br>





<div id="Programming Tools">
  
# Programming Tools 
<pre>
<li>Python</a>   <img src="Sources\220px-Python-logo-notext.svg.png" width="40" height="40"></li>

<li>Github</a>   <img src="Sources\logo_github_icon_143196.png" width="40" height="40"></li>

<li>Microsoft Visual Studio   <img src="Sources\Visual_Studio_Icon_2019.png" width="40" height="40"></li>
</pre>
<br><br>
<div id="Project Goals">
  
# Project Goals

<li><a href="#Task 1">Choose the optimum aircraft models with lowest-cost route</a></li>
<li><a href="#Task 2">Design an aircraft with low operation cost</li>
<li><a href="#Task 3">Design virtual aircraft model with different cost coefficients to fly as safe and cheap as possible</li>
<li><a href="#Task 2">Design virtual aircraft model with different cost coefficients to fly as safe and cheap as possible</li>
<li><a href="#Task 3">Design a minus cost area</li>



<br><br>
<div id="Assignments">
  
# Assignments
  
<table><tr><td>
	
### Code Ammendments
	
  "In this project, the group was given the task to modify an A-Star Algorithm code provided by the lecturers to match the required obstacles of the group.  In this algorithm, however, the group located an error in the calculations for the costs of the fuel-consuming and time-consuming area; specifically in lines 149 and 155 of the original code (a_star_noted.py).  In these calculations, the cost of fuel (C<sub>f</sub>) and time (C<sub>t</sub>) were not multiplied to the additional trip fuel (ΔF<sub>a</sub>) and time (ΔT<sub>a</sub>) required, resulting in a cost a little short of what it is supposed to be.  The group was able to resolve this error, as shown below."
	
<img src="Sources\CodeError.jpg">

</td></tr></table>

<table><tr><td>
<h2>→ Task 1: </h2>
<table><tr><td>Find the PolyU Aircraft Model with the minimum cost for the challenge assigned to our group.</td></tr></table>
<tr>The given features of the 4 PolyU Aircraft Model are as follows:
<img src="Sources\Task 1\Aircraft Models.png"></tr><br><br>
<tr><li>By using the following formulae given:</tr></li>
<tr><img src="Sources\Task 1\CostFormula.png" width="674.34" height="41.87"></tr>

With
	<tr><li>D<sub>Total</sub> = Total Distance Travelled</li></tr>
	<tr><li>D<sub>Fa</sub> = Distance Travelled in Fuel Consuming Area</li></tr>
	<tr><li>D<sub>Ta</sub> = Distance Travelled in Time Consuming Area</li></tr>

</td></tr></table>

<hr>
<table><td><tr>
<tr><h4><i>Solution:</i></tr></h4>
<li>Excel is being utilized to help generate the following table:</li>
<img src="Week 6 Compulsory Tasks\Task 1\Cost for each plane.png"><br>
<a href="https://github.com/adrianlua03/ENG1003_w1_Group10/blob/main/Week%206%20Compulsory%20Tasks/Task%201/Cost%20for%20each%20Plane.xlsx?raw=true">Click here for  Excel Raw File</a>	<br><br>
∴ As can be seen, highlighted in green, the PolyU-A380 scores the lowest Goal Cost under the consideration with the given constraints. It is being animated below:
<br>
	<p align="center">
<img src="Sources\GIFs\AAEFP Task 1 - A380.gif" width="412" height="310">
</tr></td></table>
<hr>

<table><tr><td>
<h2>→ Task 2</h2>
<table><tr><td>Find the PolyU Aircraft Model that achieve minimum cost for the challenge assigned to our group.
</td></tr></table></td></tr></table>

	

<pre><strong>2.1 | 4 constraints with 2 variables</strong><br></pre>
<p align="center">
<img src="Sources\GIFs\AAEFP Task 2 - 2 Var.gif" width="412" height="310"></li>
  
<pre><strong>2.2 | 4 constraints with 6 variables</strong><br></pre>
 
### a. Methodology
	
Unlike in task 2.1, a graph would not be able to provide an answer as there are six missing variables in this task.  Instead, pure analysis was used to solve this.  Just like in tasks 1 and 2.1, it can be seen that the lower the values of the given variables are, the lower the total cost would be.  This makes sense because, as shown on the given formula above, the total cost is an additive of and directly proportional to the given variables.  Because of this, the higher the variables are, the higher the cost, and vice versa.
	
The given constraints also made the analysis simpler because they set a minimum value to the inequalities of the variables.  The same reasoning, as stated earlier, can be applied to this situation, where the higher the values of the variables are, the higher its result of the inequality as it is an additive of the products of specific variables.  
	
With this in mind, it can be concluded that to provide the minimum total cost, the result of the inequalities would have to be either equal or close to the set minimum.  Substituting the values in the variables , it can be seen that the further the values of the variables (e.g. C<sub>F</sub> & C<sub>T</sub>) are away from each other, the lower the result of the cost.  This is because the closer the values of the variables are to each other (if all of them are 5), the first inequality is maximized, and as stated earlier, it is favorable for the inequalities to be at its minimum.  This means that the possible values of the cost (C<sub>F</sub> & C<sub>T</sub>) and trip variables (ΔF & ΔT) pairs should only be either 1 or 9.  When substituted to the variables, however, the first inequality is not satisfied (it is below the minimum).  To solve this, two of the variables must be replaced with 2 and 8 instead of 1 and 9; in this case, ΔT and ΔF were replaced, respectively. From this, it can be seen that all inequalities are satisfied and are equal or close to its minimum, resulting in a minimum cost.

With this analysis, however, there may be multiple patterns of ones and nines.  The values of each variables were chosen to further minimize the cost of the path.  As only values of 1 and 9 must be chosen to fulfill the goal of this task, the group must consider which variable or area to give the higher value (9).  To do this, the actual course of the aircraft must be considered.  It can be seen in the course that the aircraft has no way around the fuel-consuming area.  This means that the cost through the fuel-consuming area must be minimized.  This is why the costs of the fuel-consuming area are reduced to 1.  This would also mean that the cost of the time-consuming area should be either 8 or 9.  In this case, 9 was chosen for both.  This is because either way (if the variables are either 8 or 9), the aircraft would avoid this area entirely.  This means that the trip time (not additional time) would have to be equal to 8, minimizing the total cost of the trip time and path.  
	
### b. Results
	
The path plan is as shown below:  
<br />
<img src="Sources\GIFs\AAEFP Task 2 - 6 Var.gif" width="309" height="232.5">
	

The 6 chosen variables (not including C<sub>C</sub>) and the cost it amounted to are as shown below:
	
<img src="Sources\Task 3\Task3Result.png" width="626.25" height="92.25">	
	

### c. Discussion

From the results of this task, it can be seen that similar to the {aircraft of task 2.1}, {task 2.2} also avoids the time-consuming area.  This is because the cost of fuel and the additional trip fuel is too high in this case.  The results also show that the path taken by this aircraft is longer than paths taken by the PolyU aircrafts, similar to {task 2.1}.  

An important implication from this task is that to minimize the cost, minimizing all of the variables may not be practical or efficient.  As implied in the analysis from the methodology, all variables work together to minimize the cost.  Some values must be raised to minimize the others; as in real life situations, there will always be constraints similar to the inequalities provided in the task.  Additionally, just because one variable is high does not mean that the total cost would also be high.  In some cases, similar to that of task 2.1, maximizing costs in one area may lead to a different path, which avoids the area entirely.  In most real life situations, choosing a more efficient path, instead of the shortest path, will lead to shorter costs.  
	
<hr>

<table><tr><td>
<h2>→ Task 3</h2>
<table><tr><td>Design a new cost area that can reduce the cost of the route.
</td></tr></table></td></tr></table>

### a. Methodology

Similar to the previous task, the implementation of the minus-cost area was also done with pure analysis.  For this task, the aircraft used was the PolyU-A380, whose original minimum cost path is already known as figured in task 1.  Because of this, the group would be able to know where to implement the minus-cost area since it would be most logical to have it coincide with the path to obtain the maximum deduction.  

This is because the original path of the PolyU A380 already gives the minimum cost.  It would make sense to implement the minus-cost area along this path as this further minimizes the cost of the already minimum path.  Additionally, adding this area along the original path would not alter it, making it a more favorable path.  

For this task, the formula of the cost was manipulated, as shown below:

<img src="Sources\Task 3\Task3Formula.png" width="703.3" height="31.4">

With

• D<sub>P</sub> = Distance travelled in minus-cost area

According to the formula above, the cost deduction was simply subtracted from the original equation.  It can be seen that to get the maximum possible deduction for this path, the distance would have to be altered as the cost per node is fixed.  This would mean that the minus-cost area would have to be a 16-grid-point-long diagonal line 16√2, since this would cover the most distance along the path.  This distance is the maximum possible distance for any case, which means that the maximum possible cost is also fixed for any situation.  This would mean that to obtain the minimum cost, we would have to subtract the maximum possible deduction from the minimum original cost.  

This analysis also shows that altering the path to get the minimum cost would not be possible because altering the cost would make the path longer, increasing the cost.  This increase would outweigh the deduction from the minus-cost path, making the alteration unviable.  

### b. Results

The path plan is as shown below:  
<br />
<img src="Sources\GIFs\AAEFP Task 3.gif" width="309" height="232.5">


The cost for this task is as shown below:
	
<img src="Sources\Task 3\Task3Table.png" width="785.09" height="92.25">

### c. Discussion

From the results shown on the GIF above, it can be seen that the path taken by the A380 in this situation did not alter from the original path taken.  It is also evident that the minus-cost area, shown in blue, coincides with this original path along a diagonal line.  

When compared to real-life situations, the minus-cost area may be analogous to a tailwind in a flight path.  This is because a tailwind may be able to push and speed up the aircraft, requiring less fuel and less time, therefore minimizing the cost.  Unlike in real-life situations, however, the location of a minus-cost area may not always be known and may occur at random times.  Because of this, it may be hard for flight planners to locate the most efficient route such as what is done in this task.

<br><br>


<div id="Additional Tasks">
	
# Additional Tasks
## → Adding Checkpoints
	
	
</td></tr></table>

<br><br>
<div id="Reflective Essays">
  
# Reflective Essays
  
  ####   LUA, Adrian Shalom (21093985D)
  
  <table><tr><td>
Upon hearing the words “path planning”, what initially came to mind were complex codes and algorithms that consisted of over a thousand lines of code. “Path planning” sounded like a job for the “experts”: well-tenured engineers with over ten years of experience, computer scientists with PhDs, and so on. However, what I failed to realize before completing this project was the fact that simple path planning algorithms such as A Star can actually be learned by freshmen students such as myself, with the right mindset.
	 
One of the main things that I have learned in this project was that there are several variables that can affect the cost consumption of an aircraft, and slight changes to one variable can significantly impact the cost of a flight. For example, when we compare the variables of the PolyU-A380 Aircraft with the PolyU-A381, the differences of their variables didn’t seem significant: Delta_F deviated by 0.5, Ct deviated by 1, DeltaFa deviated by 0.1, and deltaTa deviated by 0.2. These slight deviations may seem negligible, but those deviations were responsible for a cost difference of about 3,000. In this project, I have gained a better understanding of how small, seemingly insignificant changes to aircraft properties can actually cause a big difference in terms of cost. 

Another thing I have learned was that programming and analytical skills are built through active engagement. Before partaking in this project, my mindset towards programming was such: “If I have a very skilled instructor who will teach me how to improve my programming skills, then I will be a great programmer myself”. However, after taking on this hands-on project with minimal experience, I have realized that engaging in codes that I have never seen before, altering them, learning how they work, and learning how to manipulate variables was a very effective way to enhance my programming skills. My programming capabilities were not dependent on external factors, rather it was dependent on my willingness to learn and actively challenge myself, to expose myself to codes that are difficult. The path planning project was a difficult task to accomplish, but with a willingness to learn, I, along with my groupmates, were able to face the challenges and accomplish the compulsory tasks.

Lastly, I have recognized the importance of routing and directions when it comes to aviation. It is easy to think that flying is the only important part of aviation. Everything else, including path planning, were just secondary. However, the project has helped me appreciate the out-of-flight procedures, because these are equally as important, especially when trying to allow efficient flight. 

  </td></tr></table>  
  
  ####   ANG Jershon Ainsleigh Entote （21094022D）  
  
  <table><tr><td>
    typehere2
  </td></tr></table>  
  
  ####   TSUI Zheng Yang （21065427D）
    
  <table><tr><td>
    typehere3
  </td></tr></table>  
  
  ####   WONG Dik Hin (21071947D)
    
  <table><tr><td>
    typehere4
  </td></tr></table>  
  
  ####   Jay    ()
    
  <table><tr><td>
    typehere5
  </td></tr></table>  
