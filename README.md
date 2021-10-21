<details open="open" align="center">
  <summary><h4 style="display: inline-block"><pre>Table of Contents    <i>--(Toggle)</i></pre></h4></summary>  
    <li><a href="#About Path Planning">About Path Planning</a></li>
    <li><a href="#Theory of Path Planning Algorithm">Theory of Path Planning Algorithm</a></li>
    <li><a href="#Programming Tools">Engineering Tools</a></li>
    <li><a href="#Project Goals">Project Goals</a></li>
    <li><a href="#Assignments">Assignments</a></li>
    <li><a href="#Additional Tasks">Additional Tasks</a></li>
    <li><a href="#Reflective Essays">Reflective Essays</a></li>
	<br><br>
<a href="https://info.flagcounter.com/MqVq"><img src="https://s01.flagcounter.com/count/MqVq/bg_FFFFFF/txt_000000/border_CCCCCC/columns_1/maxflags_5/viewers_0/labels_0/pageviews_0/flags_0/percent_0/" alt="Flag Counter" border="0"></a>
  </ol>
</details>

<br><br>
<hr>
<div id="About Path Planning">

<h1>01 | About Path Planning</h1>
<p align="center">
<tr><img src="Sources\March-World-small.gif" width="500" height="300" class="center">


Path planning can be characterized as a process to identify or predict an object's ability to move from the origin to the destination. With recent advancements in technology and digitalization, path planning has become exceptionally important in various industries. Path planning has been commonly used in aviation, robotics, computer gaming, and other transport-based industries. 

In commercial aviation, pilots have to do path planning before every flight in order to make sure that the flight route is possible to run through. Without a proper flight plan, the pilot will not be able to identify where the aircraft must fly in order to fly within optimal conditions. For example, without proper path planning, the pilot will not be able to identify regions with high turbulent wind that the aircraft may want to avoid. As a result, during this turbulent phase, the aircraft may experience significant drag increases, especially frictional and pressure drag. These problems may quickly compound and cause more problems, and may even cause some flight parameters to move outside the flight envelope. 

Aside from pilots, ATCs utilize path planning for commercial aviation as well, because they have to arrange flights around and in the airport too. Because of this, path-planning is really important to the aviation industry since it can ensure our safety and reduce flight costs.

Moving outside commercial aviation, path planning is also becoming increasingly important in future aeronautical applications such as Unmanned Aerial Vehicles, Drones, and Robotic Aircraft. Proper path planning algorithms must be made to ensure that these non-controlled machines can efficiently do the required work without manual operation. </tr>

<hr><br><br>

<div id="Theory of Path Planning Algorithm">
<h1>02 | Theory of Path Planning Algorithm</h1>
	
<p align="center">
<img src="Sources\Potential_path.gif" width="500" height="300" class="center">
<br>
	
The goal of path planning, simply put, is to select the shortest path from the start node to the goal node. An important theory of path planning is the concept of Global and Local Path Planning. Global Path Planning allows the "object" in the start node to complete its travel based on known parameters and obstacles given. Simply put, the environment and its obstacles are known, and the algorithm can use this predetermined information to generate the needed path. On the other hand, Local Path Planning refers to a path planning wherein the obstacles are unknown and are not predefined. Therefore, the object in the algorithm will need to utilize its sensor to detect the environment and complete its travel.
	
The A Star Path Planning Algorithm, which is used in this project, runs under Global Path Planning because the obstacles and barriers are pre-set. The A Star Path Planning Algorithm uses a heuristic search method to identify the route of travel from the start node to the end node. Heuristic search, by definition, refers to the concept of "testing and trying". The algorithm will test if a certain approach is feasible, taking into account the obstacles, the goal node, and the route. This approach works well with the project because heuristic search methods usually take less time, though less optimal. 
	
	
In order to define the environment that the object will run in, the A Star Path Planning Algorithm will have lines in the code in which users can enter their desired start coordinates and goal coordinates. When using the programming language Python, the graph that contains these coordinates are normally being help displayed by a plotting library called Matplotlib. Matplotlib is not a built in function in Python, but it is a mathematical extension that helps in providing a visually comprehensible map with coordinates. Because Matplotlib is an extension rather than a function, Matplotlib first needs to be installed and then imported into the code for it to be put to use. This is done by entering the line "import matplotlib.pyplot as plt". 
	
Aside from the start coordinates and goal coordinates, the relevant borders and obstacles also need to be plotted and seen in Matplotlib. The way that these borders and obstacles are plotted centers around creating a list which will contain the points in the map where the obstacles and borders are to be plotted in. The program uses the .append function to add more elements to the list, which would be the points that will be plotted in the graph. The program also utilizes a "for" loop to continuously add these elements within a certain range, until the desired line (which is made up of the points, defined by the elements in the created list) has been formed. Then, the path planning algorithm will plot these points in the map. 
	
These are the bases of creating the path planning environment. The exact codes of the algorithm varies depending on the type of algorithm used, but they generally have the same goal: to define the shortest route from the start node to the goal node. 

<br><br>

<div id="Programming Tools">
  
# 03 | Programming Tools 
	
<pre>
<li>Python</a>   <img src="Sources\220px-Python-logo-notext.svg.png" width="40" height="40"></li>
<li>Github</a>   <img src="Sources\logo_github_icon_143196.png" width="40" height="40"></li>
<li>Microsoft Visual Studio   <img src="Sources\Visual_Studio_Icon_2019.png" width="40" height="40"></li>
<p align="center">
<a href="https://code.visualstudio.com/docs/editor/github"> Click here for brief installation and usage guidance</a>
</pre>
<br><br>

<div id="Project Goals">
  
# 04 | Project Goals

<li><a href="#Task 1">Choose the optimum aircraft models with lowest-cost route</a></li>
<li><a href="#Task 2">Design an aircraft with low operation cost</li>
<li><a href="#Task 3">Design virtual aircraft model with different cost coefficients to fly as safe and cheap as possible</li>
<li><a href="#Task 2">Design virtual aircraft model with different cost coefficients to fly as safe and cheap as possible</li>
<li><a href="#Task 3">Design a minus cost area</li>



<br><br>
<div id="Assignments">
  
# 05 | Assignments
  
<table><tr><td>
	
### Code Ammendments
<i>
  "In this project, the group was given the task to modify an A-Star Algorithm code provided by the lecturers to match the required obstacles of the group.  In this algorithm, however, the group located an error in the calculations for the costs of the fuel-consuming and time-consuming area; specifically in lines 149 and 155 of the original code (a_star_noted.py).  In these calculations, the cost of fuel (C<sub>f</sub>) and time (C<sub>t</sub>) were not multiplied to the additional trip fuel (ΔF<sub>a</sub>) and time (ΔT<sub>a</sub>) required, resulting in a cost a little short of what it is supposed to be.  The group was able to resolve this error, as shown below."
	</i>
	
<img src="Sources\CodeError.jpg">

</td></tr></table>

<table><tr><td>
<h2>→ Task 1: </h2>
<table><tr><td>Find the PolyU Aircraft Model with the minimum cost for the challenge assigned to our group.</td></tr></table>
	<tr><strong>The given features of the 4 PolyU Aircraft Model are as follows:</strong>
<img src="Sources\Task 1\Aircraft Models.png"></tr><br><br>
	<tr><li><strong>By using the following formulae given:</tr></li></strong>
<tr><img src="Sources\Task 1\CostFormula.png" width="674.34" height="41.87"></tr>

<strong>With</strong>
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
<table><tr><td>Design a new aircraft model within the constrains to achieve minimum cost for your group challenge. 
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

According to the formula above, the cost deduction was simply subtracted from the original equation.  It can be seen that to get the maximum possible deduction for this path, the distance would have to be altered as the cost per node is fixed.  This would mean that the minus-cost area would have to be a 16-grid-point-long diagonal line 16√2, since this would cover the most distance along the path.  This distance is the maximum possible distance for any case, which means that the maximum possible cost is also fixed for any situation.  This would mean that to obtain the minimum cost, we would have to subtract the maximum possible deduction from the minimum original cost (as calculated in task 1).  

This analysis also shows that altering the path to get the minimum cost would not be possible because altering the cost would make the path longer, increasing the cost.  This increase would outweigh the deduction from the minus-cost path, making the alteration unviable.  

### b. Results

The path plan is as shown below:  
<br />
<img src="Sources\GIFs\AAEFP Task 3.gif" width="309" height="232.5">


The cost for this task is as shown below:
	
<img src="Sources\Task 3\Task3Table.png" width="785.09" height="92.25">

### c. Discussion

From the results shown on the GIF above, it can be seen that the path taken by the A380 in this situation did not alter from the original path taken.  It is also evident that the minus-cost area, shown in blue, coincides with this original path along a diagonal line.  

When compared to real-life situations, the minus-cost area may be analogous to a tailwind in a flight path.  This is because a tailwind may be able to push and speed up the aircraft, requiring less fuel and less time, therefore minimizing the cost.  Unlike in real-life situations, however, the location of a minus-cost area may not always be known and may occur at random times.  Because of this, it may be difficult for flight planners to locate the most efficient route such as what is done in this task.

<br><br>


<div id="Additional Tasks">
	
# 06 | Additional Tasks
## → Adding Checkpoints
### a. Methodology

In this task, the A_Star algorithm code first studied for its mechanism and then manipulated to fit the task.  In the code, two functions called "planning" and "calc_final_path" were used to plan and calculate the total cost required for the entire path.  To add checkpoints, these functions were simply multiplied to three  secions (planning1, 2, 3 and calc_final_path1, 2, 3).  Each of these function pairs calculate the minimum cost to travel from one point to another (start to checkpoint 1, checkpoint 1 to 2, checkpoint 2 to goal).  The variables in each function was simply changed to represent different points.  The additional points, along with the animations of each paths, were then defined in the main function.
	
Since the checkpoints were required to be located inside each cost-consuming area, the group randomly chose points in these areas, making sure that they did not coincide with the original path plan.  
	
### b. Results
	
The original and modified path plans for the A380 are as shown below:
	
<img src="Sources\GIFs\AAEFP Task 1 - A380.gif" width="309" height="232.5">
<img src="Sources\GIFs\AdditionalTask1.gif" width="309" height="232.5">
	
### c. Discussion
	
The GIFs of both the original and modified path plans are presented side-by-side as shown above.  The GIFs show that the path plans for both planes differ significantly, especially because the checkpoints were located far away from the original path plan.  The cost for the path plan with checkpoints also increase significantly as compared to the original path because it is required to travel and stay in the cost-consuming areas along a longer distance.  
	
In most real-life scenarios, such as those in military applications, checkpoints are set for the flight plans.  It is important to take note that the most efficient path from start to end might not always stop on checkpoints.  This is why checkpoints must almost always be included in calculations such as these to find the most efficient path while fulfilling important tasks along the way.  
	
</td></tr></table>
	
## → Changing Environment
	
## → Comparing Algorithms
### a. Methodology
	
In this additional task, three other algorithms were taken from the Path Planning Repository owned by Atsushi Sakai, namely: D Star Lite, Flow Field, and Potential Field. These algorithms were then modified to try to provide a similar obstacle set as the obstacle set assigned to the group for the A Star algorithm. In addition, the algorithms' theories and operating principles were studied thoroughly. 
	
The group selected two parameters suitable for comparison: Obstacles and Theory
	
**Obstacles**
	
The following steps were taken to modify/compare obstacles:
1. Locate lines of code that set the obstacle positions
2. Identify the coordinates of the obstacles in the assigned A Star Algorithm 
3. Replace the original obstacle coordinates with the coordinates assigned in the A Star Algorithm
4. Capture a photo of the plot 
	
**Theory**
	
Whereas for theory, a less systematic approach was taken. The respective algorithms' principles were studied and relevant research papers were read. Then, a table (see figure below) was used to compare specific properties of the algorithms. 
	
(Insert table)
		
### b. Results
	
**Obstacles**

D Star Lite
	
For the D Star Lite Algorithm, the obstacle coordinates were successfully changed. The bottom, top, left, and right borders were similar to the assigned A Star Algorithm, and the obstacle sets were similar as well. 
	
	
![DimpledWealthyCardinal-size_restricted](https://user-images.githubusercontent.com/76478835/138321445-4c12d221-f6ef-4734-a4cf-0a9b763daf74.gif)

	
However, because D Star Algorithm is written in a different way and logic as the A Star Algorithm, the path generated differs from that of the A Star Algorithm. In the path generation for D Star, the algorithm simply passes through the obstacle, which the group finds somewhat unintuitive. The code can be modified to generate a more intuitive path. However, such task is beyond the scope of the obstacle comparison. 
		
FLow Field 
	
For Flow Field Path Planning, (to be continued)
	
Potential Field 
	
(To be continued)
	
**Theory**
	
Below is the completed table that highlights the differences and similarities of each algorithm.
	
(Insert Table)
		
### c. Discussion
	
**D Star Lite**
	
Among the three algorithms, D Star Lite contains the most similarities when compared with the A Star algorithm. Obstacle coordinates are collected in a similar way, by using the .append and "for" function of Python, and then compiling these coordinates into a list that will be plotted in MatPLotLib. 
	
The main difference, however, would be the automatic random generation of a new obstacle. This is a particularly practical feature of D Star Lite, because it takes into account unexpected obstacles which is very likely in the real world. 
	
**Flow Field**
	
The flow field algorithm, on the other hand, differs significantly from the A Star Path Planning. The flow field algorithm adds a new element to the pathfinding process: vector fields. These vector fields influence the route of the pathfinding process, as the object will move in the direction of the vector fields. 
	
Introducing the concept of flow fields in this pathfinding process is an effective method to further simulate real world processes. In aviation, when an aircraft flies through the atmosphere, the aircraft encounters flow fields, with streamlines passing through the airfoil. Aircraft also generate vortex fields which circulate around the aircraft wingtips, and can affect the motion of the aircraft. For these reasons, the flow field algorithm is useful for advanced aerodynamic purposes. 
	
**Potential Field**
	
Similar to the flow field algorithm, the potential field algorithm incorportates potential fields in the pathfinding process. This can be practical in research situations wherein the velocity potential of a flow is taken into account. Compared with Flow Field Pathfinding, Potential Field Pathplanning is less practical as Flow Fields are better suited for dynamic situations. 

  
<br><br>
<div id="Reflective Essays">
	
# 07 | Reflective Essays
  
  ####   LUA, Adrian Shalom (21093985D)
  
  <table><tr><td>
Upon hearing the words “path planning”, what initially came to mind were complex codes and algorithms that consisted of over a thousand lines of code. “Path planning” sounded like a job for the “experts”: well-tenured engineers with over ten years of experience, computer scientists with PhDs, and so on. However, what I failed to realize before completing this project was the fact that simple path planning algorithms such as A Star can actually be learned by freshmen students such as myself, with the right mindset.
<br><br>

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
In the early stages, path planning can only be done by hand manually to help ensure the safe operation of an aircraft during a route flight. Performing calculations by hand, especially when solving through multiple sets of constraints and lines continuous equations could be troublesome, and humans wouldn’t otherwise be able to catch up with the rapidly changing environmental conditions, making the process highly complicated and time consuming. In modern days as technology advanced exponentially, the need of manual path planning is greatly reduced where computer flight planning Is being adopted into our daily lives whereas the usage does not only get restricted to flight planning, but robotics or even computer games! <br><br>
With computer aided path planning, accurate weather forecasts can be obtained directly from the internet while the fuel consumption calculations and flight conditions are being optimized to be efficient hence as inexpensive as possible. In this subject, we are being given the above task where our group gets to experience 2-Dimensional path planning by using Python, a high-level programming language, where it calculates a set of solutions that best fits the aircraft’s operational efficiency in real time alongside with the two safety-critical aspects: fuel approximation and the compliance with the air traffic control requirements. To conclude with, doing path planning with program languages such as Python can be highly versatile and instantaneous, great for tasks like flight planning.
(TBC, -ve 70 words)
  </td></tr></table>  
  
  ####   WONG Dik Hin (21071947D)
    
  <table><tr><td>
    typehere4
  </td></tr></table>  
  
  ####   Chang Jung Wook (21108704D)
    
  <table><tr><td>
    typehere5
  </td></tr></table>  
