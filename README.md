## pyscript - some scripts for Home Assistant using Python

In this repository I'm currently testing some of my newest Python scripts that I'm going to use for my homeautomation.
You'll find some basic but also some pretty advanced scipts inside this repo.

---

**What I've finished so far:**
- airconditioner.py - turn my AC on is the current PM2.5 value reaches over the treshold and vica versa
- battery_monitor.py - notify me when some batteried devices get below a certain treshold value
- climates.py - set the current target temperature of my (dumb) bluetooth thermostats in Home Assistant
- music_leds.py - change the current running color palette on a specified timing cycle, turn leds off/on if dependent entity also turn off/on
- nachtmoduy.py - turn on nightmode inside Home Assistant if some criterias are met and turn it off at 7:00 am

---

**Currently working on:**
- vacuum.py - start cleaning cycle if nobody is at home and hasn't cleaned today
