import time
from plyer import notification
while True:
 notification.notify(
title="**Please drink Water!!",
message="Getting enough water every day is important for your health.Water helps your body: Keep a normal temperature.",
app_icon=(r"C:\Users\KIIT\Desktop\python lab tt\water.ICO.ico"),
timeout=10
)
 time.sleep(60*60)