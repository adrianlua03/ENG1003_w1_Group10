<details open="open">
  <summary><h4 style="display: inline-block"><pre>Table of Contents    <i>--(Toggle)</i></pre></h4></summary>  
    <li><a href="#About Path Planning">About Path Planning</a></li>
    <li><a href="#Programming Tools">Engineering Tools</a></li>
    <li><a href="#Project Goals">Project Goals</a></li>
    <li><a href="#Assignments">Assignments</a></li>
    <li><a href="#Reflective Essays">Reflective Essays</a></li>

  </ol>
</details>

<hr>
<div id="About Path Planning">

<h1>About Path Planning</h1>
<tr><img src="Sources\March-World-small.gif" width="500" height="300" class="center">


Path planning can be characterized as a process to identify or predict an object's ability to move from the origin to the destination. With recent advancements in technology and digitalization, path planning has become exceptionally important in various industries. Path planning has been commonly used in aviation, robotics, computer gaming, and other transport-based industries. 

In commercial aviation, pilots have to do path planning before every flight in order to make sure that the flight route is possible to run through. Without a proper flight plan, the pilot will not be able to identify where the aircraft must fly in order to fly within optimal conditions. For example, without proper path planning, the pilot will not be able to identify regions with high turbulent wind that the aircraft may want to avoid. As a result, during this turbulent phase, the aircraft may experience significant drag increases, especially frictional and pressure drag. These problems may quickly compound and cause more problems, and may even cause some flight parameters to move outside the flight envelope. 

Aside from pilots, ATCs utilize path planning for commercial aviation as well, because they have to arrange flights around and in the airport too. Because of this, path-planning is really important to the aviation industry since it can ensure our safety and reduce flight costs.

Moving outside commercial aviation, path planning is also becoming increasingly important in future aeronautical applications such as Unmanned Aerial Vehicles, Drones, and Robotic Aircraft. Proper path planning algorithms must be made to ensure that these non-controlled machines can efficiently do the required work without manual operation. </tr>

<hr>





<div id="Programming Tools">
  
# Programming Tools 
<pre>
<li>Python</a>   <img src="Sources\220px-Python-logo-notext.svg.png" width="40" height="40"></li>

<li>Github</a>   <img src="Sources\logo_github_icon_143196.png" width="40" height="40"></li>

<li>Microsoft Visual Studio   <img src="Sources\Visual_Studio_Icon_2019.png" width="40" height="40"></li>
</pre>

<div id="Project Goals">
  
# Project Goals

<li><a href="#Task 1">Choose the optimum aircraft models with lowest-cost route</a></li>

<li><a href="#Task 2">Design an aircraft with low operation cost</li>
<li><a href="#Task 3">Design virtual aircraft model with different cost coefficients to fly as safe and cheap as possible</li>

<li><a href="#Task 2">Design virtual aircraft model with different cost coefficients to fly as safe and cheap as possible</li>
<li><a href="#Task 3">Design a minus cost area</li>




<div id="Assignments">
  
# Assignments
  
<table><tr><td>
	
### Code Ammendments
	
  "In this project, the group was given the task to modify an A-Star Algorithm code provided by the lecturers to match the required obstacles of the group.  In this algorithm, however, the group located an error in the calculations for the costs of the fuel-consuming and time-consuming area; specifically in lines 149 and 155 of the original code (a_star_noted.py).  In these calculations, the cost of fuel (C<sub>f</sub>) and time (C<sub>t</sub>) were not multiplied to the additional trip fuel (ΔF<sub>a</sub>) and time (ΔT<sub>a</sub>) required, resulting in a cost a little short of what it is supposed to be.  The group was able to resolve this error, as shown below."

  <img src="Sources\CodeError.jpg">
</td></tr></table>

<h2>Task 1</h2>
<h4> Find the PolyU Aircraft Model with the minimum cost for the challenge assigned to our group.</h4>

<tr>The given features of the 4 PolyU Aircraft Model are as follows:
	<img src="Sources\Task 1\Aircraft Models.png"></tr>

<tr><li>By using the following formulae given:</tr></li>
<tr><img src="Sources\Task 1\Formulae Cost.png" width="250" height="25"></tr>
<br>
<table><td><tr>
<tr><i>Solution:</i></tr>
<li>Excel is utilized to generate the following table:</li>
<img src="Week 6 Compulsory Tasks\Task 1\Cost for each plane.png"><br>
<a href="https://github.com/adrianlua03/ENG1003_w1_Group10/blob/main/Week%206%20Compulsory%20Tasks/Task%201/Cost%20for%20each%20Plane.xlsx?raw=true">Click here for  Excel Raw File</a>	<br>
<img src="Sources\GIFs\AAEFP Task 1 - A380.gif" width="412" height="310">
</tr></td></table>

	
  ## Task 2.1
  
  #### Find the PolyU Aircraft Model that achieve minimum cost for the challenge assigned to our group.
  <img src="Sources\GIFs\AAEFP Task 2 - 2 Var.gif" width="412" height="310"></li>
  
  ## Task 2.2
 
	
  ## Task 3
 
  #### Design a minus cost area for the challenge assigned to our group.

  
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

