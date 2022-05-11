# This is Data Gathering Tool (DGT)
## Created by Daan Assies & Rogier Harmelink
#### App last updated 03-04-2022

**THIS README IS NOT FINAL**

This Assetto Corsa app stores almost all possible imformation using the ac API.

Data will be stored in the folder DGT/dataGathering/out.  
The folder will be named after the current timestamp+c of starting the game.

The following files and information will be stored, with their corresponding index: \
 ###**session.csv:**

0. **driver name:** str \
driver name
1. **session type:** ACC_SESSION_TYPE \
-1: unknown, 0: practice, 1: qualifying, 2: race, 3: hotlap, 
4: timeattack, 5: drift, 6: drag, 7: hotstint, 8: hotstintsuperpole
2. **car:** str \
car name
3. **ballast:** int \
ballast added to car in kg
4. **caster:** float \
angle of caster in radians
5. **tyre radius:** -
6. **min height:** float \
minimum height of the car (floor of car to surface) in meters
7. **max torque:** -
8. **max power:** -
9. **max rpm:** -
10. **max sus travel:** -
11. **max turbo:** -
12. **ffb:** float \
maximum force feedback levels given through wheel
13. **track:** str \
track name
14. **track config:** str \
track configuration used
15. **track length:** float \
track length in metres
16. **air temp:** -
17. **air density:** -
18. **track temp:** -
19. **surface grip:** -
20. **assists:** -

###**car.csv:**

1. **speed:** float \
current speed in kmph
2. **rpm:** float \
current rpm of engine
3. **gear:** str \
R = reverse, N = neutral, rest is trivial
4. **fuel:** float \
current amount of fuel in the car in kg
5. **drs available:** int (boolean) \
drs can currently be enabled
6. **drs enabled:** int (boolean) \
drs is currently enabled
7. **damage:** (float, float, float, float, float) \
damage of the car at the front, rear, left, right, centre
8. **cg height:** float \
current height of the centre of gravity to the surface in metres
9. **drive train:** float \
current speed delivered to the wheels in kmph, difference with actual speed yet to be understood
10. **velocity:** (float, float, float) \
velocity vector of the car in coordinates (x,y,z)
11. **acceleration:** (float, float, float) \
acceleration vector of the car in coordinates (x,y,z)
12. **tc in use:** int (boolean) \
traction control is currently enabled (happens automatically if the assists is enabled)
13. **abs in use:** int (boolean) \
abs is currently enabled (happens automatically if the assist is enabled)
14. **brake bias:** float \
front brake bias, 0.6 means 60% brake bias on the front
15. **engine brake mapping:** -
16. **world location:** (float, float, float) \
location of the car within the virtual world in (x,y,z)
17. **timestamp:** int \
realtime timestamp the data was gathered at

###**input.csv**

1. **gas:** float [0,1] \
gas input, 0 = nothing, 1 = full
2. **brake:** float [0,1] \
brake input, 0 = nothing, 1 = full
3. **steer:** float \
steer input in degrees. positive = left, negative = right
4. **clutch:** float [0,1] \
clutch input, not used on most cars
5. **force feedback:** float \
last force feedback signal sent to the wheel
6. **timestamp:** int \
realtime timestamp the data was gathered at

###**lap.csv**
1. **lap position:** float [0,1] \
location of the car related to a lap on the circuit. 0 = start, 1 = finish
2. **lap count:** int \
current lap number
3. **current lap:** int \
amount of time spent in current lap in ms
4. **current sector:** int \
current sector the car is located in
5. **last lap:** int \
last lap time in ms
6. **best lap:** int \
best lap time in ms
7. **lap delta:** float \
current lap time compared to best lap time at that part of the circuit in s
8. **split:** float \
last sector time in s
9. **invalid:** boolean \
returns true if there are more than 2 tyres off-track, or the game thinks the lap is invalid
10. **timestamp:** int \
realtime timestamp the data was gathered at

###**tyre.csv**
The columns of this file are repeats of the columns below, for each of the four tyres. 0 = front left, 1 = front right, 2 = rear left, 3 = rear right

1. **tyre wear:** float \
wear of tyre. 100 is full tyre grip, 0 is tyre dead
2. **dirty:** float \
The levels of dirt on the tyre
3. **inner temp:** float \
temperature of the inner part of the tyre surface in celsuis
4. **middle temp:** float \
temperature of the middle part of the tyre surface in celsius
5. **outer temp:** float \
temperature of the outer part of the tyre surface in celsuis
6. **core temp:** float \
core temperature of the tyre in celsuis
7. **tyre pressure:** float \
pressure of the tyre in psi
8. **slip ratio:** float [0,1]
9. **slip angle:** float [0. 360] \
slip angle, angle between the desired direction and the actual direction of the vehicle in degrees
10. **camber:** float \
camber angle of the tyre in degrees
11. **torque:** float \
self-aligning torque of the tyre
12. **load:** float \
wheel load on the tyre in kg
13. **sus travel:** float \
vertical suspension travel in relation to base in metres
14. **contact normal:** (float, float, float) \
normal vector to the tyre's contact point
15. **contact point:** (float, float, float) \
tyre contact point with the surface in virtual world coordinates
16. **contact heading:** (float, float, float) \
tyre heading vector
17. **angular speed:** float \
angular speed of the tyre in rad/s