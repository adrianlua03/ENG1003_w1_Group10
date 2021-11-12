<details open="open" align="center">
  <summary><h4 style="display: inline-block"><pre>Table of Contents    <i>--(Toggle)</i></pre></h4></summary>  
    <li><a href="#About Path Planning">About Path Planning</a></li>
    <li><a href="#Theory of Path Planning Algorithm">Theory of Path Planning Algorithm</a></li>
    <li><a href="#Programming Tools">Programming Tools</a></li>
    <li><a href="#Project Goals">Project Goals</a></li>
    <li><a href="#Assignments">Assignments</a></li>
    <li><a href="#Additional Tasks">Additional Tasks</a></li>
    <li><a href="#Reflective Essays">Reflective Essays</a></li>
    <li><a href="#References">References</a></li>
	<br><br>
<a href="https://info.flagcounter.com/MqVq"><img src="https://s01.flagcounter.com/count/MqVq/bg_FFFFFF/txt_000000/border_CCCCCC/columns_1/maxflags_5/viewers_0/labels_0/pageviews_0/flags_0/percent_0/" alt="Flag Counter" border="0"></a>
  </ol>
</details>
<br>
<p align="center">
<img src="Sources\20d9c9ccfee8b5892a145199e458fc79.gif" width="1000" height="500">

<p align="center">
<a href="https://youtu.be/aUYJMlKWbwA">
<img src="Sources\youtube-logo-hd-8.png" width="400" alt="Group Presentation Video">
</a></p>
<p align="center">
Click the Youtube Icon above to access our group's Presentation video
	

<hr><br><br>
<div id="About Path Planning">

<h1>01 | About Path Planning</h1>
<p align="center">
<tr><img src="Sources\March-World-small.gif" width="500" height="300" class="center">


Path planning can be characterized as a process to identify or predict an object's ability to move from the origin to the destination. With recent advancements in technology and digitalization, path planning has become exceptionally important in various industries. Path planning has been commonly used in aviation, robotics, computer gaming, and other transport-based industries. 

In commercial aviation, pilots have to do path planning before every flight in order to make sure that the flight route is possible to run through. Without a proper flight plan, the pilot will not be able to identify where the aircraft must fly in order to fly within optimal conditions. For example, without proper path planning, the pilot will not be able to predict regions with high turbulent flow that the aircraft may want to avoid. At a certain Reynold's Number, drag is larger in a turbulent flow compared to laminar; hence, turbulent regions may decrease flight performance. These problems may also quickly compound and cause even more problems, and may even cause some flight parameters to move outside the flight envelope. 

Aside from pilots, ATCs and flight engineers can utilize path planning as well for more efficient commercial flight operations. As they have to arrange flights around and in the airport, they may also find ways using path planning to keep the route of an aircraft continuous and straight, which can help contribute to greener aviation because of the reduction in fuel emission time. Because of this, path-planning is really important to the aviation industry since it can ensure safety, reduced flight costs, and a more sustainable future.

Moving outside commercial aviation, path planning is also becoming increasingly important in future aeronautical applications such as Unmanned Aerial Vehicles, Drones, and Robotic Aircraft. Proper path planning algorithms must be made to ensure that these non-controlled machines can efficiently do the required work without manual operation. </tr>

<hr><br><br>

<div id="Theory of Path Planning Algorithm">
<h1>02 | Theory of Path Planning Algorithm</h1>
	
<p align="center">
<img src="Sources\Potential_path.gif" width="700" height="300" class="center">
<br>
	
The goal of path planning, simply put, is to select the shortest path from the start node to the goal node. An important theory of path planning is the concept of Global and Local Path Planning. Global Path Planning allows the "object" in the start node to complete its travel based on known parameters and obstacles given. Simply put, the environment and its obstacles are known, and the algorithm can use this predetermined information to generate the needed path. On the other hand, Local Path Planning refers to a path planning wherein the obstacles are unknown and are not predefined. Therefore, the object in the algorithm will need to utilize its sensor to detect the environment and complete its travel.
	
The A Star Path Planning Algorithm, which is used in this project, runs under Global Path Planning because the obstacles and barriers are pre-set. The A Star Path Planning Algorithm uses a heuristic search method to identify the route of travel from the start node to the end node. Heuristic search, by definition, refers to the concept of "testing and trying". The algorithm will test if a certain approach is feasible, taking into account the obstacles, the goal node, and the route. This approach works well with the project because heuristic search methods usually take less time, though less optimal. 
	
	
In order to define the environment that the object will run in, the A Star Path Planning Algorithm will have lines in the code in which users can enter their desired start coordinates and goal coordinates. When using the programming language Python, the graph that contains these coordinates are normally being help displayed by a plotting library called Matplotlib. Matplotlib is not a built in function in Python, but it is a mathematical extension that helps in providing a visually comprehensible map with coordinates. Because Matplotlib is an extension rather than a function, Matplotlib first needs to be installed and then imported into the code for it to be put to use. This is done by entering the line "import matplotlib.pyplot as plt". 
	
Aside from the start coordinates and goal coordinates, the relevant borders and obstacles also need to be plotted and seen in Matplotlib. The way that these borders and obstacles are plotted centers around creating a list which will contain the points in the map where the obstacles and borders are to be plotted in. The program uses the .append function to add more elements to the list, which would be the points that will be plotted in the graph. The program also utilizes a "for" loop to continuously add these elements within a certain range, until the desired line (which is made up of the points, defined by the elements in the created list) has been formed. Then, the path planning algorithm will plot these points in the map. 
	
These are the bases of creating the path planning environment. The exact codes of the algorithm varies depending on the type of algorithm used, but they generally have the same goal: to define the shortest route from the start node to the goal node. 
<hr>
<br><br>

<div id="Programming Tools">
  
# 03 | Programming Tools 

	
<p align="center">
<img src="Sources\bfc67a7da17b8a3f224b0ba748c71364.gif" width="700" height="300" class="center">
											       
<pre>
<li>Python</a>   <img src="Sources\220px-Python-logo-notext.svg.png" width="40" height="40"></li>
<li>Github</a>   <img src="Sources\logo_github_icon_143196.png" width="40" height="40"></li>
<li>Microsoft Visual Studio   <img src="Sources\Visual_Studio_Icon_2019.png" width="40" height="40"></li>
<p align="center">
<a href="https://code.visualstudio.com/docs/editor/github"> Click here for brief installation and usage guidance</a>
</pre>
<hr>
<br><br>

<div id="Project Goals">
  
# 04 | Project Goals

<p align="center">
<img src="Sources\68747470733a2f2f626c6f672e636c6f75646c617965722e696f2f636f6e74656e742f696d616765732f323032302f31322f646576656c6f7065725f6d65642d312e676966.gif" width="400" height="300" class="center">

<li><a href="#Task 1">Choose the optimum aircraft models with lowest-cost route</a></li>
<li><a href="#Task 2">Design an aircraft with low operation cost</li>
<li><a href="#Task 3">Design virtual aircraft model with different cost coefficients to fly as safe and cheap as possible</li>
<li><a href="#Task 2">Design virtual aircraft model with different cost coefficients to fly as safe and cheap as possible</li>
<li><a href="#Task 3">Design a minus cost area</li>
<hr>

<br><br>
	
<div id="Assignments">
  
# 05 | Assignments
  
<table><tr><td>
	
### Code Ammendments
<i>	
In this project, the group was given the task to modify an A-Star Algorithm code provided by the lecturers to match the required obstacles of the group.  In this algorithm, however, the group located an error in the calculations for the costs of the fuel-consuming and time-consuming area; specifically in lines 149 and 155 of the original code (a_star_noted.py).  In these calculations, the cost of fuel (C<sub>f</sub>) and time (C<sub>t</sub>) were not multiplied to the additional trip fuel (ΔF<sub>a</sub>) and time (ΔT<sub>a</sub>) required, resulting in a cost a little short of what it is supposed to be.  The group was able to resolve this error, as shown below.
	<br><br>
<img src="Sources\CodeError.jpg">
	<br><br></i>
</td></tr></table>

<br>
	
<tr>The formula used for these tasks is as shown below:</tr>
<tr><img src="Sources\Task 1\CostFormula.png" width="674.34" height="41.87"></tr>

<strong>With</strong>
	<tr><li>D<sub>Total</sub> = Total Distance Travelled</li></tr>
	<tr><li>D<sub>Fa</sub> = Distance Travelled in Fuel Consuming Area</li></tr>
	<tr><li>D<sub>Ta</sub> = Distance Travelled in Time Consuming Area</li></tr>
<hr>
<br>
	
## → Task 1:
<table><tr><td>Find the PolyU Aircraft Model with the minimum cost for the challenge assigned to our group.</td></tr></table>

<strong><h2>a. Methodology</h2></strong>

The cost data for air carriers and general aviation aircrafts are defined as variable or fixed. Variable costs change in proportion to aircraft usage and include fuel, maintenance, and crew costs. Since it is quite impossible for a human to keep track of all the aircraft models simultaneously, spreadsheets and database softwares can be used by inputing all the respective formulae and variables into the different terminals or user interfaces to allow the softwares to calculate values either by batch or real-time. After calculations are done, a sort function can also be applied to show total costs in order from the least to the largest.

For this task, the values of the variables of the respective PolyU aircraft were inputted into the A-Star Algorithm code.  Their respective values were then compared, and the aircraft with the least total cost was obtained.  
	
<strong><h2>b. Results</h2></strong>
	
The summary of costs are as presented below:
<img src="Week 6 Compulsory Tasks\Task 1\Task1Highlighted.png" width="756.3035" height="230.625">

<a href="https://github.com/adrianlua03/ENG1003_w1_Group10/blob/main/Week%206%20Compulsory%20Tasks/Task%201/Cost%20for%20each%20Plane.xlsx?raw=true">Click here for  Excel Raw File</a>	<br><br>
	
The path plan for the most efficient aircraft (Polyu-A380) is as shown below:

<img src="Sources\GIFs\AAEFP Task 1 - A380.gif" width="309" height="232.5">
</tr></td></table>

<strong><h2>c. Discussion</h2></strong>

As shown on the results above, the PolyU-A380 has the gives the lowest cost for the entire path plan.  This result may be due to the PolyU-A380 having the lowest variable costs among the four aircrafts. The values of these variables determine the total cost of the flight plan as they are positively correlated to the cost, as shown on the formula above.  

In result, the path is being plotted through both the fuel and time consuming area as it is not viable for the plane to be routed away, avoiding both of the mentioned area as more acute turns may not be comfortable for passengers and by other means, burns more fuel if flying time increased.

<hr>
<br>

## → Task 2
<table><tr><td>Design a new aircraft model within the constrains to achieve minimum cost for your group challenge. 
</td></tr></table>

	

<pre><strong>2.1 | 4 constraints with 2 variables</strong><br></pre>

### a. Methodology

Because there are only 2 variables to be determined in this task, a simple graph-and-test approach can be done to find the minimum total cost for the new aircraft model. In this task, the group performed the following steps: 

1. Let C<sub>f</sub> = x and C<sub>t</sub> = y
2. In the mathematical graphing software, Desmos, place the equations of the 4 constraints assigned.
3. From the graph plotted in Desmos, find the intersection of all 4 equations.
4. Take the vertices and test their values (x,y) in the general equation. 
5. The values (x,y) that yields the minimum are the chosen values for C<sub>f</sub> and C<sub>t</sub> of the new aircraft model

Below is the image of the graph and the calculations: 

<img src="Sources\Task 2\Graph1 copy.png" width="558.12" height="298.2">
<br><br>

Aside from this method, another possible solution is to analyze the given inequalities. Solving the inequalities results in the following constraints for both C<sub>f</sub> and C<sub>t</sub>:

10 ≤ C<sub>f</sub> ≤ 60 <br>
20 ≤ C<sub>t</sub> ≤ 40 

The constraints were then analyzed to study how each variable would affect the cost.  As mentioned earlier, to minimize the cost, the variable costs would have to be minimized as they are positively correlated with each other.  This results in 2 possible solutions: (10,40) and (20,20). These points were then inputted into the cost formula to see which has the lower cost.  

### b. Results

The table of results is shown below: 

<img src ="Sources\Task 2\2.1Results.png" width = "626.25" height = "92.25">


The path plan is as shown below:  
<br />
<img src="Sources\GIFs\AAEFP Task 2 - 2 Var.gif" width="309" height="232.5">

### c. Discussion
  
According to the results of this task, to minimize the cost of the path plan, the values for C<sub>f</sub> and C<sub>t</sub> would have to be 20 each. 

This task shows how two cost variables may each affect each other and the total cost. In real life scenarios, these costs may be interrelated and finding the balance between the economic costs of these variables may be important in minimizing the total cost of the path plan.  In some cases, fully minimizing one of their costs will result in a higher cost for the other.  Some aspects such as these must be sacrificed to obtain the least total cost.

<br><br>
<pre><strong>2.2 | 4 constraints with 6 variables</strong><br></pre>
 
### a. Methodology
	
Unlike in task 2.1, a graph would not be able to provide an answer as there are six missing variables in this task.  Instead, pure analysis was used to solve this.  Just like in tasks 1 and 2.1, it can be seen that the lower the values of the given variables are, the lower the total cost would be.  This makes sense because, as shown on the given formula above, the total cost is positively correlated with the given variables.  This reasoning would also make the analysis of the constraints simpler since they set a minimum value to the inequalities of the variables.

With this, it can be concluded that to provide the minimum total cost, the result of the inequalities would have to be either equal or close to the set minimum.  Substituting the values in the variables , it can be seen that the further the values of the variables (e.g. C<sub>F</sub> & C<sub>T</sub>) are away from each other, the lower the result of the cost.  This is because if the values of the variables are closer to each other (if all of them are 5), the first inequality is maximized, and as stated earlier, it is favorable for the inequalities to be at its minimum.  This means that the possible values of the cost (C<sub>F</sub> & C<sub>T</sub>) and trip variables (ΔF & ΔT) pairs should only be either 1 or 9.  When substituted to the variables, however, the first inequality is not satisfied (it is below the minimum).  To solve this, two of the variables must be replaced with 2 and 8 instead of 1 and 9; in this case, ΔT and ΔF were replaced, respectively. From this, it can be seen that all inequalities are satisfied and are equal or close to its minimum, resulting in a minimum cost.

With this analysis, however, there may be multiple patterns of ones and nines.  The values of each variables were chosen to further minimize the cost of the path.  As only values of 1 and 9 must be chosen to fulfill the goal of this task, the group must consider which variable or area to give the higher value (9).  To do this, the actual course of the aircraft must be considered.  It can be seen in the course that the aircraft has no way around the fuel-consuming area.  This means that the cost through the fuel-consuming area must be minimized.  This is why the costs of the fuel-consuming area are reduced to 1.  This would also mean that the cost of the time-consuming area should be either 8 or 9.  In this case, 9 was chosen for both.  This is because either way (if the variables are either 8 or 9), the aircraft would avoid this area entirely.  This means that the trip time (not additional time) would have to be equal to 8, minimizing the total cost of the trip time and path.  
	
### b. Results
	
The 6 chosen variables (not including C<sub>C</sub>) and the cost it amounted to are as shown below:
	
<img src="Sources\Task 3\Task3Result.png" width="626.25" height="92.25">	
	
The path plan is as shown below:  
<br />
<img src="Sources\GIFs\AAEFP Task 2 - 6 Var.gif" width="309" height="232.5">

### c. Discussion

From the results of this task, it can be seen that similar to the {aircraft of task 2.1}, {task 2.2} also avoids the time-consuming area.  This is because the cost of fuel and the additional trip fuel is too high in this case.  The results also show that the path taken by this aircraft is longer than paths taken by the PolyU aircrafts, similar to {task 2.1}.  

An important implication from this task is that to minimize the cost, minimizing all of the variables may not be practical or efficient.  As implied in the analysis from the methodology, all variables work together to minimize the cost.  Some values must be raised to minimize the others; as in real life situations, there will always be constraints similar to the inequalities provided in the task.  Additionally, just because one variable is high does not mean that the total cost would also be high.  In some cases, similar to that of task 2.1, maximizing costs in one area may lead to a different path, which avoids the area entirely.  In most real life situations, choosing a more efficient path, instead of the shortest path, will lead to shorter costs.  
	
<hr><br>

## → Task 3
<table><tr><td>Design a new cost area that can reduce the cost of the route.
</td></tr></table>

### a. Methodology

Similar to the previous task, the implementation of the minus-cost area was also done with pure analysis.  For this task, the aircraft used was the PolyU-A380, whose original minimum cost path is already known as figured in task 1.  Because of this, the group would be able to know where to implement the minus-cost area since it would be most logical to have it coincide with the path to obtain the maximum deduction.  

This is because the original path of the PolyU A380 already gives the minimum cost.  It would make sense to implement the minus-cost area along this path as this further minimizes the cost of the already minimum path.  Additionally, adding this area along the original path would not alter it, making it a more favorable path.  

For this task, the formula of the cost was manipulated, as shown below:

<table><tr><td>
<img src="Sources\Task 3\Task3Formula.png" width="703.3" height="31.4">

<strong>With</strong>

• D<sub>P</sub> = Distance travelled in minus-cost area
</table></tr></td>

According to the formula above, the cost deduction was simply subtracted from the original equation.  It can be seen that to get the maximum possible deduction for this path, the distance would have to be altered as the cost per node is fixed.  This would mean that the minus-cost area would have to be a 16-grid-point-long diagonal line 16√2, since this would cover the most distance along the path.  This distance is the maximum possible distance for any case, which means that the maximum possible cost is also fixed for any situation.  This would mean that to obtain the minimum cost, we would have to subtract the maximum possible deduction from the minimum original cost (as calculated in task 1).  

This analysis also shows that altering the path to get the minimum cost would not be possible because altering the cost would make the path longer, increasing the cost.  This increase would outweigh the deduction from the minus-cost path, making the alteration unviable.  

### b. Results

The cost for this task is as shown below:
	
<img src="Sources\Task 3\Task3Table.png" width="785.09" height="92.25">

The path plan is as shown below:  
<br />
<img src="Sources\GIFs\AAEFP Task 3.gif" width="309" height="232.5">

### c. Discussion

From the results shown on the GIF above, it can be seen that the path taken by the A380 in this situation did not alter from the original path taken.  It is also evident that the minus-cost area, shown in blue, coincides with this original path along a diagonal line.  

When compared to real-life situations, the minus-cost area may be analogous to a tailwind in a flight path.  This is because a tailwind may be able to push and speed up the aircraft, requiring less fuel and less time, therefore minimizing the cost.  Unlike in real-life situations, however, the location of a minus-cost area may not always be known and may occur at random times.  Because of this, it may be difficult for flight planners to locate the most efficient route such as what is done in this task.
<hr>
<br><br>


<div id="Additional Tasks">
	
# 06 | Additional Tasks
## → Adding Checkpoints
### a. Methodology

In this task, the A_Star algorithm code first studied for its mechanism and then modified to fit the task.  In the code, two functions called "planning" and "calc_final_path" were used to plan and calculate the total cost required for the entire path.  To add checkpoints, these functions were simply multiplied to three  secions (planning1, 2, 3 and calc_final_path1, 2, 3).  Each of these function pairs calculate the minimum cost to travel from one point to another (start to checkpoint 1, checkpoint 1 to 2, checkpoint 2 to goal).  The variables in each function was simply changed to represent different points.  The additional points, along with the animations of each paths, were then defined in the main function.
	
Since the checkpoints were required to be located inside each cost-consuming area, the group randomly chose points in these areas, making sure that they did not coincide with the original path plan.  
	
### b. Results
	
The original and modified path plans for the A380 are as shown below:
	
<img src="Sources\GIFs\AAEFP Task 1 - A380.gif" width="309" height="232.5">
<img src="Sources\GIFs\AdditionalTask1.gif" width="309" height="232.5">
	
### c. Discussion
	
The GIFs of both the original and modified path plans are presented side-by-side as shown above.  The GIFs show that the path plans for both planes differ significantly, especially because the checkpoints were located far away from the original path plan.  The cost for the path plan with checkpoints also increase significantly as compared to the original path because it is required to travel and stay in the cost-consuming areas along a longer distance.  
	
In most real-life scenarios, such as those in military applications, checkpoints are set for the flight plans.  It is important to take note that the most efficient path from start to end might not always stop on checkpoints.  This is why checkpoints must almost always be included in calculations such as these to find the most efficient path while fulfilling important tasks along the way.  
	
</td></tr></table>

<hr><br>

## → Changing Environment
### a. Methodology

Similar to the previous task, the original A Star Algorithm code was first studied and modified.  For this task, the time-consuming area was first eliminated from the code.  The positions of the fuel consuming area, obstacles, and start and goal points were then modified such that they generate randomly in each run.  To do this, the random module was imported to the code.  

To generate the fuel-consuming area randomly, the group used the random module to generate coordinates for the bottom left corner of the 30x30 square and build up the square from that point.  A range of (-9,30) was used for both coordinates of this point so that when the square generates, it won't overlap with the borders of the map.  

For the obstacles on the other hand, the random module was used to generate obstacles with a probability of 1 in 3.  To do this, a number was randomly generated between 1 and 3 for each point in the map, and if the randomly chosen number is equal to 3, then an obstacle would generate.  This function was also modified such that the obstacles would not generate on the start and goal point. 

As for the start and goal points, the random module was also used to generate their coordinates randomly.  The points are set to generate only within the borders of the map.  For the y-coodinate of the goal point, however, its method of generation had to differ from the rest because the Euclidean distance between the start and goal points must be at least 50.  To do this, a while loop incorporated with the Pythagorean theorem was utilized.  This makes sure that the Euclidean distance between the two points would not go below 50 units.  
	
Aside from modifying the positions of the obstacles, the robot's properties were also modified.  The radius of the robot was modified from 1 to 0 so that it would be able to pass through thinner areas.  The movement of the robot was also modified such that it is unable to move diagonally.  To do this, the get_motion_model function was modified such that all diagonal movements were deleted from the code. 

### b. Results

The path plans of 5 randomly generated obstacles are as shown below:

<img src="Sources\GIFs\AdditionalTask2(1).gif" width="309" height="232.5">

### c. Discussion

The results (GIFs) above shows 5 different scenarios of the running code, all of which have different positions for the start and goal points, obstacles, and fuel-consuming area. 

The results of this task plays an important role in further understanding path planning for aircrafts.  The randomness of these obstacles may represent the random weather patterns that may be experienced during flight.  This is why flight paths are not always exactly the same for each flight from one destination to another.  Although the paths may be similar, random weather patterns may allow them to differ, requiring the aircraft to follow other paths to optimize the costs during a flight.  

Unlike in real-life scenarios, weather patterns in different times may not as significantly differ as compared to comparing two adjacent code runs.  The idea of differing environments, however, is important to take into account when planning a flight.  

<hr><br>

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
	
Whereas for theory, a less systematic approach was taken. The respective algorithms' principles were studied and relevant research papers were read. Then, a table was used to compare specific properties of the algorithms. 
	
		
### b. Results
	
**Obstacles**

D Star Lite
	
For the D Star Lite Algorithm, the obstacle coordinates were successfully changed. The bottom, top, left, and right borders were similar to the assigned A Star Algorithm, and the obstacle sets were similar as well. 
	
<img src="Sources\D_Star_Lite_Plot.png" width="309" height="232.5">	
	
However, because D Star Algorithm is written in a different way and logic as the A Star Algorithm, the path generated differs from that of the A Star Algorithm. In the path generation for D Star, the algorithm simply passes through the obstacle, which the group finds somewhat unintuitive. The code can be modified to generate a more intuitive path. However, such task is beyond the scope of the obstacle comparison. 

<img src ="Sources\IMG_5941.gif" width="309" height="232.5">
		
Flow Field 
	
For Flow Field Path Planning, the obstacles relied on the assigned vector fields, which is currently beyond the capabilities of the group to modify. Therefore, a different obstacle set was used for Flow Field Path Planning (see figure). However, the group was able to draw comparisons based on theory, which will be discussed after this section. 

<img src ="Sources\Flow Field.gif" width="309" height="232.5">
	
Potential Field 
	
Similar to the Flow Field Path Planning, the obstacles were a challenge to modify, which the group believes cannot be solved within the given time frame. A different obstacle set was used, but the group was able to compare the theoretical aspect of the algorithm. 

<img src ="Sources\PotentialField.gif" width="309" height="232.5">
	
**Theory**
	
Below is the completed table that highlights the differences and similarities of each algorithm.
	
<img src ="Sources\Table_AddTask3_Result.png" width="500" height="500">
		
### c. Discussion
	
**D Star Lite**
	
Among the three algorithms, D Star Lite contains the most similarities when compared with the A Star algorithm. Obstacle coordinates are collected in a similar way, by using the .append and "for" function of Python, and then compiling these coordinates into a list that will be plotted in MatPLotLib. 
	
The main difference, however, would be the automatic random generation of a new obstacle. This is a particularly practical feature of D Star Lite, because it takes into account unexpected obstacles which is very likely in the real world. 
	
**Flow Field**
	
The flow field algorithm, on the other hand, differs significantly from the A Star Path Planning. The flow field algorithm adds a new element to the pathfinding process: vector fields. These vector fields influence the route of the pathfinding process, as the object will move in the direction of the vector fields. 
	
Introducing the concept of flow fields in this pathfinding process is an effective method to further simulate real world processes. In aviation, when an aircraft flies through the atmosphere, the aircraft encounters flow fields, with streamlines passing through the airfoil. Aircraft also generate vortex fields which circulate around the aircraft wingtips, and can affect the motion of the aircraft. For these reasons, the flow field algorithm is useful for advanced aerodynamic purposes. 
	
**Potential Field**
	
Similar to the flow field algorithm, the potential field algorithm incorportates potential fields in the pathfinding process. This can be practical in research situations wherein the velocity potential of a flow is taken into account. Compared with Flow Field Pathfinding, Potential Field Pathplanning is less practical as Flow Fields are better suited for dynamic situations. 
<hr>
<br><br><br>


<div id="Reflective Essays">
	
# 07 | Reflective Essays
	
<p align="center">
<img src="Sources\ecf76f_c399f08accac43ceba9b7f8d92dfcfd3_mv2.gif" width="300">
	
  
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
When I was first assigned to this course, I thought I would have a difficult time.  I was initially overwhelmed with the words “Path Planning Algorithms” because prior to this course, I had little knowledge of the Python language.  I’ve only learned the basics in the summer prior to my first year in university, so I thought that I wouldn’t be able to keep up.  As time progressed, however, I realized that I was wrong, and I learned so much more from this course than what I thought I would have. <br><br>
	  
The first thing I’ve learned was, of course, about Python.  Although our instructors did not go in depth in discussing how the code works and how path planning works, I was still able to learn a lot through hands-on experience.  One of the most useful things in this course is that we were able to learn something by doing the work, instead of studying books like what is normally done in other subjects.  From this subject, I was able to code and modify some algorithms to fit our goal.  Doing this took a lot of time because I had to study how the code worked before I was able to manipulate it.  From this, however, I am confident enough to say that my skills in python have improved significantly.  

Aside from my programming skills, my analytical skills have also improved along with it.  From coding, I had to learn how everything worked.  Not only this, but I also had to learn which functions to use and how to use them.  Though these tasks were challenging and took a lot of time, I was still able to perform these tasks and get the right results.  Aside from programming, however, I also got to build my analytical skills from analyzing the tasks.  In tasks 2 and 3, for example, I mainly used analytical skills to try and solve these problems because solving these problems manually or with codes may be too difficult.  I found that solving these analytically took less time and gave satisfactory results.

I have also learned a lot about path planning.  I learned that numerous variables have to be taken into account in path planning, and that they are all inter-related.  For example in task 2.2, where we have to find 6 unknown variables; although one variable is a lot more than the other, it still produces the lowest cost.  I also learned that sometimes, the shortest path might not be the most efficient/ cost effective.  In path planning, there are a lot of variables and scenarios that we have to consider.  We also have to consider that these variables and scenarios may change over time.  Although the tasks done in this course were relatively simple as compared to what is experienced in the real world, these concepts may still be combined and applied.  

This project has also taught me a lot about working with a group.  Initially, I thought working with a group online would be too difficult.  With the lack of face-to-face interaction with my groupmates and instructors, I feared that I wouldn’t be able to do much for the group.  I was able to contribute a lot, however, and help my groupmates in these tasks.  I hope to be better at collaborating with other people after this experience and learn to work with others more efficiently.  
  </td></tr></table>  
  
  ####   TSUI Zheng Yang （21065427D）
    
  <table><tr><td>
With this group project slowly coming to an end, there's definitely a few things that I could takeaway. Although I am no longer that familiar in progrramming with  Python like 4 years ago where I used to be joining a Summer Institute organized by HKUST, it was solely about doing data analysis from a set of database while making predictions using Python, which I can't find myself useful in this project. So with the help from Adrian, our group leader, and Jershon, we are able to modify the pre-existing as what we called the A star Path Planning, we are only able to finish this project flawlessly. So what I immediate got in charge was the Readme, it is definitely one of the most vital part in summarizing the overall timeline and rundown of the project, so Curtis and I spent a great amount of time debating and designing an intuitive Readme page using the HTML webpage programming language, so  that we could present and explain every tasks and procedures in absolute details. To acknowledge how the Python and Path Planning works, alongside with tasks example to better understand the flexibility of the code.<br><br>
In the early stages, path planning can only be done by hand manually to help ensure the safe operation of an aircraft during a route flight. Performing calculations by hand, especially when solving through multiple sets of constraints and lines continuous equations could be troublesome, and humans wouldn’t otherwise be able to catch up with the rapidly changing environmental conditions, making the process highly complicated and time consuming. In modern days as technology advanced exponentially, the need of manual path planning is greatly reduced where computer flight planning Is being adopted into our daily lives whereas the usage does not only get restricted to flight planning, but robotics or even computer games! <br><br>
With computer aided path planning, accurate weather forecasts can be obtained directly from the internet while the fuel consumption calculations and flight conditions are being optimized to be efficient hence as inexpensive as possible. In this subject, we are being given the above task where our group gets to experience 2-Dimensional path planning by using Python, a high-level programming language, where it calculates a set of solutions that best fits the aircraft’s operational efficiency in real time alongside with the two safety-critical aspects: fuel approximation and the compliance with the air traffic control requirements. To conclude with, doing path planning with program languages such as Python can be highly versatile and instantaneous, great for tasks like flight planning where data are analysed continuously. <br>
  </td></tr></table>  
  
  ####   WONG Dik Hin (21071947D)
    
  <table><tr><td>
    As the first group project, I didn’t thought that it will be hard. I thought it would be just a small project to help us to know how we should work in the university and included some ice-breaking job. But it turns out differently. From the beginning to the end, problems have nearly appeared consistently. There were lots new things kept popping up in the lectures. And over these few weeks, I have really learnt a lot.


First of all, lots of knowledge can be seen in the lessons. I have never heard things like Python and GitHub before. Although I didn’t understand how both of them works, I still able get to know into details that how they operates and what functions they can do. For coding, I know that once we have sufficient time to explore more, there is nothing that is impossible. It can nearly create everything. And the GitHub, it is a useful tool, especially in group projects. Apart from recording our working progress, we can see lots of other programs and articles that people have uploaded to the GitHub.

Other than the above, I have also able to get deeply into path planning. I have heard of it before but just very briefly. I always thought only pilots or airline staffs will need to know about it. I have never thought of freshmen like us would learn it that soon. Initially, I thought we have to do calculations for path planning manually. But after this project, I have figured there are different path planning algorithms and Python can always help us to do the calculations once we have finished coding.

At last, the most important thing that I have learnt is how we should work in modern days. No matter what task you have to deal with, you may face different difficulties. Due to advanced technology, we can easily surf in the internet to find solutions if we don’t want to disturb anyone. Although the internet is full of information, sometimes it may not able to help to solve issues, we can still ask for help from others. Most of the people are quite friendly unless you keep bothering them. They can often inspire us.
  </td></tr></table>  
  
  ####   CHANG Jung Wook (21108704D)
    
  <table><tr><td>
    I choose this course because I was interested in coding and the topic “Path Finding Algorithms” attracted me. I don’t have any knowledge about path finding and coding, but I felt that this is the one that I really want to try. When I first attend to this class, as I expected it was big challenge for me because I have no idea what I should have to do in this course. Thankfully, my groupmates helped me to adapt in the course. Also, professor and assistants helped me to work in python and GitHub.

This was my first group project in university. I was quite nervous that I thought group project in university is totally different to project in high school. However, it was not much different from high school, and groupmates all took care of each other and led each other. With groupmates, we were able to separate works efficiently and collaborate to make best result. 

Talk about this topic more deeply, I found out that a lot of underwriting is needed for one coding. At first, I did not think path finding is that complicated. However, the deeper I dig in, the newer things and complicated processes were contained. But these things rather stimulated me and made me more interested. It was also fun to help each other and solve it even if it was difficult because I worked with the team members. When I have to do it alone, through web searching, I tried to find a solution myself and repeat until it works well.

I was assigned to do task 2.1 which is 4 constraints with 2 variables to find a minimum cost for path planning. By working this task, I have to use graphing calculator find inequalities to find out the minimum cost. It was quite challenging but the results it came out was simple which I put in table and calculate the minimum cost. This task shows how two cost variables may each affect each other and the total cost. Additional task which is comparing algorithms was my favorite part. 

At last, I have learned the path finding working process and what kind of effects cause problems. We experienced 2D path planning, graphing, python, programming language, find out the maximum profit (minimum cost). It was my first group project, but I was so satisfied that it ended successfully, and I was thankful and happy for the team members.
  </td></tr></table>  
	
	
<div id="References">
		
# References
	
(1) Montazeri, A., Can, A., Imran, I. (2021). Advances in Nonlinear Dynamics and Chaos (ANDC), Unmanned Aerial Systems. ch.3, pp.47-80. Academic Press, 2021
	
(2) Federal Aviation Administration (2016). Pilot's Handbook of Aeronautical Knowledge, Navigation. Ch. 16. Simon and Schuster, 2016
	
(3) Federal Aviation Administration (2021). Airplane Flying Handbook, Aerodynamics of Flight. Ch. 5. Simon and Schuster, 2021
	
(4) Siddiqui, R. (2018). Path Planning Using Potential Field Algorithm. Retrieved from https://medium.com/@rymshasiddiqui/path-planning-using-potential-field-algorithm-a30ad12bdb08
	
(5) National Aeronautics and Space Administration (n.d.). Definition of Streamlines. Retrieved from https://www.grc.nasa.gov/www/k-12/airplane/stream.html
	
(6) Marshall, D. (n.d.). Heuristic Search. Retrieved from https://users.cs.cf.ac.uk/Dave.Marshall/AI2/node23.html
	
(7) Princeton University (n.d.), Transition and Turbulence. Retrieved from https://www.princeton.edu/~asmits/Bicycle_web/transition.html
	
	


<br><br>
<p align="center">
<img src="Sources\have-a-anice-flight-1.gif" width="1000">
