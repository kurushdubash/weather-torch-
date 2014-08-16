<html>
<body>
<h1> WEATHER TORCH LAMP </h1>

<h2>INSPIRED BY TWITTER TORCH by SPARK Community User RUEDI</h2>

<h3>CREDIT TO PLAN44 for MESSAGE TORCH Project on GIT: https://github.com/plan44/messagetorch</h3>






~~~~EXAMPLE SPARK API CALLS~~~~~

Three modes: 1: Message, 2: , 3: Cheerlights

curl https://api.spark.io/v1/devices/53ff6f065075535140441187/params \-d access_token=e0dd630ae5f950ff67dad0c1cb20ae56e89dcd0b \-d “args=mode=3,brightness=140”

curl https://api.spark.io/v1/devices/53ff6f065075535140441187/message \-d access_token=e0dd630ae5f950ff67dad0c1cb20ae56e89dcd0b \-d “args=I AM COOL”


curl https://api.spark.io/v1/devices/53ff6f065075535140441187/params \-d access_token=e0dd630ae5f950ff67dad0c1cb20ae56e89dcd0b \-d “args=red_text=140”


curl https://api.spark.io/v1/devices/53ff6f065075535140441187/params \-d access_token=e0dd630ae5f950ff67dad0c1cb20ae56e89dcd0b \-d “args=lamp_red=255”

curl https://api.spark.io/v1/devices/53ff6f065075535140441187/params \-d access_token=e0dd630ae5f950ff67dad0c1cb20ae56e89dcd0b \-d “args=upside_down=1”

</body>
</html>