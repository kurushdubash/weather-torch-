<html>
<body bgcolor=(0,0,0)><font color=white>
<center><h1><font color=red =arial> <U>WEATHER TORCH</U></font> </h1>

<h5> INSPIRED BY TWITTER TORCH by SPARK Community User RUEDI</h5>

<h5>CREDIT TO PLAN44 for MESSAGE TORCH Project on GIT: https://github.com/plan44/messagetorch </h5>

<img src="http://affordableamericaninsurance.com/wp-content/uploads/iStock_000017482380Large.jpg" height=250 width=300>
<br>
<br>
<h4> A fun and functional addition to the Message Torch porject that uses local Weather data to control the animation of the Torch </h4>

After seeing the Message Torch project by plann44, I not only wanted to build the torch myself, but I also came up with many different ideas 
on how I could modify the animations to do what I wanted. After having worked with temperature sensors and building temperature readers using 
LCDs, I came up with a mod: Use the local weather data to change the colors of the torch; Dark red corresponding to high Temperatures( 95 degrees F) 
while light blue corresponding to low temperatures (50 degrees F).
<br>
<br>
After further thought, I thought, WHY NOT flip the flame animation if
the forecast is rain or snow. Flipping the animation visually looks like rain is falling instead of flame sparks coming up. Changing the
color to blue with the animation flipped looks exactly like rain! And why not make the Torch brighter during the day, and dimmer during the 
night? So, the Torch will turn dim in the late evening, so it does not distract you from sleeping, and serves as a really cool
nightlight. The torch will automatically turn bright once the sun rises. 
<br>
<br>
After thinking about it, I realized that I should use online Weather services instead of a physical Temperature reader. I looked at various Weather APIs
and finally chose one that was accurate and provided all the information I needed. I take the JSON data and parse the current Temperature, 
current Wind speed, and the Forecast. 
<br>
<br>
The temperature is used to control the color of the flame animation.
<br>
<br>
The wind speed controls how fast the flame goes up (or how fast the rain comes down)
<br>
<br>
The forecast tells the Weather Torch whether it is raining or clear. This controls the animation orientation.
<br>
<br>

<h4> How to run Weather Torch </h4>
First, you must get the Message Torch project from PLAN44's Github. He is the author of the animation that I use for the Weather Torch.
<br>
<br>
Next, my code is written in Python, so make sure you have Python3 installed on your computer. Download Weather Torch code from here, and 
run the Weather_Torch.py using your command prompt. 
<br>
<br>
The program will ask you of your local ZIP Code. Enter it in, and your Weather Torch is ready to go! As long is the python program is running, 
your Weather Torch will be updated every 10 minutes according to your local weather.
<br>

<h4> NOTE: All information on how to make the Torch and how to run the animation code is found at PLAN44's GITHUB, linked above! </h4>
</center> 
</body>
</html>