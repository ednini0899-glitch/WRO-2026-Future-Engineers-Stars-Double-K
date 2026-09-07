# Engineering Journal

## Stars Double K – WRO 2026 Future Engineers

This engineering journal documents the development process of the autonomous vehicle designed by **Stars Double K** for the WRO 2026 Future Engineers category.

The purpose of this journal is to record the engineering process followed by the team, including mechanical development, programming, sensor integration, testing, problems encountered, technical decisions and improvements.

Our development process follows an iterative engineering methodology:

**Problem → Idea → Prototype → Test → Result → Improvement → New Test**

Not every test produced the expected result. Failed tests were useful because they helped the team understand the mechanical and programming limitations of the vehicle and determine the next modifications.

---

# 1. Robot Configuration

The vehicle is based on the **LEGO Education SPIKE Prime** platform.

Current hardware configuration:

| Port | Component | Function |
|---|---|---|
| A | Traction motor | Vehicle forward and reverse movement |
| B | Distance sensor | Distance and environment detection |
| E | Steering motor | Mechanical steering of the front wheels |
| F | Color sensor | Red and green traffic pillar detection |

The SPIKE Prime Hub is located near the central section of the vehicle.

The vehicle uses a four-wheel chassis with a dedicated traction system and a mechanical steering system for the front wheels.

---

# 2. Initial Mechanical Development

The first objective was to construct a chassis capable of supporting the SPIKE Prime Hub, sensors and motors while maintaining enough stability for autonomous navigation.

A major design decision was to separate the two principal movement functions:

- **Port A motor:** traction
- **Port E motor:** steering

This allows the vehicle to control its forward movement independently from the orientation of the front wheels.

The steering motor is mechanically connected to the front wheel system through LEGO gears and structural components.

Because the steering motor does not directly rotate the wheels, the relationship between motor rotation and actual wheel steering angle must be determined experimentally.

---

# 3. Test 1 – Motor Function Identification

## Objective

Identify the function and movement of each motor before developing autonomous navigation.

## Procedure

The motors were activated individually.

The team verified that:

- Port A controls vehicle traction.
- Port E controls the front steering mechanism.

## Result

The two principal movement systems were successfully identified.

## Engineering Decision

Future programs were separated into traction tests and steering tests before combining both systems.

This made troubleshooting easier because each subsystem could be evaluated independently.

---

# 4. Test 2 – Steering Center Calibration

## Objective

Create a reference position representing straight front wheels.

## Procedure

The front wheels were manually positioned in the straight direction.

The relative position of the steering motor was then reset:

```text
CENTER = 0°
```

This position became the reference used by the steering programs.

## Result

The program could command the steering motor to move away from the center reference and later attempt to return to zero.

## Engineering Decision

The vehicle must begin each calibration test with the wheels physically centered.

This reduces errors caused by starting the program with an incorrect steering reference.

---

# 5. Test 3 – Steering Movement

## Objective

Determine whether the steering motor produced enough mechanical movement to change the trajectory of the vehicle.

## Initial Observation

During the first steering tests, the movement of the front wheels was not sufficiently pronounced for the desired turn.

## Modification

The steering motor movement was progressively increased.

The team observed the mechanical response of the steering linkage after each modification.

## Result

Increasing the steering movement produced a more noticeable change in the direction of the front wheels.

However, this also revealed another problem: excessive steering movement could interfere with the ability of the mechanism to return correctly to center.

---

# 6. Test 4 – Excessive Steering Failure

One of the most important failures observed during development occurred when the steering movement was increased too much.

## Problem

The front wheels reached an excessive steering position.

After the turn, the steering mechanism did not correctly recover the straight position.

## Observed Result

When traction continued with the wheels still turned, the vehicle followed an unintended circular trajectory instead of continuing straight.

## Analysis

This demonstrated that a larger motor rotation does not necessarily produce a better maneuver.

The mechanical steering system has a practical operating range.

If the steering motor is commanded beyond the useful mechanical range, the vehicle may:

- Lose steering accuracy.
- Fail to return to center.
- Produce an excessively tight turn.
- Continue driving in a circular trajectory.
- Reduce the repeatability of the autonomous maneuver.

## Engineering Decision

The steering value was reduced and the team decided to calibrate the system progressively instead of using the maximum possible movement.

The current experimental reference is approximately:

```text
CENTER = 0°
RIGHT_POSITION = -100°
LEFT_POSITION = +100°
STEERING_SPEED = 100 deg/s
```

These values are development parameters and may be modified after additional track testing.

---

# 7. Test 5 – Traction System

## Objective

Verify that the vehicle can move using the traction motor independently from the steering system.

The traction motor is connected to:

```text
Port A
```

The current development speed used in the integrated programs is approximately:

```text
DRIVING_SPEED = 200 deg/s
```

Some steering tests were also performed using a driving value of approximately 220 deg/s.

## Result

The traction system was successfully integrated with the steering tests.

## Engineering Consideration

Driving speed affects the complete autonomous system.

A higher speed reduces the available reaction time for the sensors and steering system.

A lower speed provides additional reaction time but increases the total time required to complete the course.

For this reason, the final competition speed will be selected after additional track testing.

---

# 8. Test 6 – Steering While Driving

## Objective

Observe the steering mechanism while the vehicle was moving.

## Procedure

The vehicle was programmed to:

1. Start with the front wheels centered.
2. Move using the traction motor.
3. Change the steering position.
4. Observe the vehicle trajectory.
5. Return the steering motor toward the center reference.
6. Continue moving.

## Result

This test demonstrated that traction and steering could operate as part of the same program.

It also showed that steering calibration must consider the vehicle while it is moving, because the trajectory depends on both steering position and traction speed.

---

# 9. Color Sensor Integration

The color sensor is connected to:

```text
Port F
```

Its purpose is to distinguish the red and green traffic pillars used during the obstacle challenge.

## Preliminary Observation

During current testing, the color sensor can recognize the target color at an approximate distance of:

```text
6 cm
```

This is an observed preliminary working distance.

The final detection performance may vary depending on:

- Lighting conditions.
- Sensor orientation.
- Vehicle speed.
- Pillar position.
- Distance between the sensor and the pillar.

---

# 10. Test 7 – Red Color Detection

## Objective

Verify that the SPIKE Prime system can identify a red traffic pillar.

## Current Logic

When red is detected:

```text
RED detected
      ↓
Display "R" on Hub
      ↓
Execute right steering response
```

The Hub display was included during development to provide visual confirmation that the program recognized the color.

This makes it easier to distinguish between a sensor detection problem and a steering problem.

---

# 11. Test 8 – Green Color Detection

## Objective

Verify that the SPIKE Prime system can identify a green traffic pillar.

## Current Logic

When green is detected:

```text
GREEN detected
       ↓
Display "V" on Hub
       ↓
Execute left steering response
```

The letter **V** is used as visual feedback for "Verde" during the development process.

The final autonomous behavior does not depend on this visual feedback; it is mainly a debugging tool.

---

# 12. Test 9 – Color Detection While Driving

After testing color recognition, the next step was to combine detection with traction.

The vehicle was programmed to move continuously while reading the color sensor.

Current development logic:

```text
MOVE FORWARD
     ↓
READ COLOR SENSOR
     ↓
 ┌───────────────┐
 │               │
RED             GREEN
 │               │
 ↓               ↓
Display R       Display V
 │               │
 ↓               ↓
Steer right     Steer left
 │               │
 └───────┬───────┘
         ↓
Return steering
         ↓
Continue driving
```

This test represents an important transition from individual subsystem testing toward autonomous behavior.

---

# 13. Distance Sensor Development

The distance sensor is connected to:

```text
Port B
```

The sensor has been integrated into the software so its measurements can be monitored during development.

The final distance threshold has not yet been established.

```text
DISTANCE_THRESHOLD = TBD
```

The threshold will be selected after additional testing on the track.

The team decided not to define a final threshold without observing the real behavior of the robot.

---

# 14. Combined System Development

The current software development combines:

- Traction motor.
- Steering motor.
- Color sensor.
- Distance sensor.
- SPIKE Prime Hub.
- Visual debugging information.

The integrated program continuously reads sensor information while controlling the movement of the vehicle.

The current architecture can be represented as:

```text
             START
               ↓
      Initialize steering
               ↓
          Move forward
               ↓
          Read sensors
               ↓
       Analyze environment
               ↓
       Color detected?
          /          \
        RED          GREEN
         ↓              ↓
   Right response   Left response
          \            /
           ↓          ↓
          Recover steering
               ↓
          Continue driving
               ↓
             LOOP
```

---

# 15. Current Obstacle Avoidance Development

The current program can react to the detected traffic pillar color.

However, a complete obstacle maneuver requires more than a single steering movement.

The next development stage is to create a controlled trajectory composed of:

```text
Detect obstacle
      ↓
Initial steering
      ↓
Pass obstacle
      ↓
Counter-steering
      ↓
Recover trajectory
      ↓
Continue navigation
```

Counter-steering is important because simply returning the steering motor to zero does not automatically return the entire vehicle to its original trajectory.

The vehicle position must also be corrected after passing the obstacle.

---

# 16. Main Problems Identified

During the current development process, the team identified several important engineering challenges:

### Steering range

Too little steering does not produce enough trajectory change.

Too much steering can prevent correct recovery and produce a circular trajectory.

### Mechanical steering recovery

Mechanical components can introduce small differences between the commanded motor position and the actual wheel orientation.

### Vehicle speed

Speed affects sensor reaction time and steering behavior.

### Sensor distance

The color sensor currently detects the target color at approximately 6 cm, requiring careful sensor placement.

### Obstacle recovery

Avoiding the pillar is only the first part of the maneuver. The vehicle must also recover its trajectory.

---

# 17. Engineering Improvements

Based on the tests performed, the development strategy was modified.

Instead of attempting to program the complete challenge immediately, the system was divided into smaller subsystems.

Development sequence:

```text
Steering
   ↓
Traction
   ↓
Steering + Traction
   ↓
Color Detection
   ↓
Color + Movement
   ↓
Distance Measurement
   ↓
Combined Sensors
   ↓
Autonomous Navigation
```

This modular development strategy allows failures to be identified more easily.

---

# 18. Software Development History

The repository contains separate programs representing different development stages.

| File | Purpose |
|---|---|
| `01_steering_calibration.py` | Steering calibration |
| `02_traction_test.py` | Traction motor testing |
| `03_steering_while_driving.py` | Steering while vehicle is moving |
| `04_color_detection_while_driving.py` | Color detection during movement |
| `05_distance_sensor_test.py` | Distance sensor readings |
| `06_combined_sensor_test.py` | Sensor and movement integration |
| `main.py` | Current integrated development program |

Keeping these programs separately allows the team to preserve the development history instead of only presenting the latest program.

---

# 19. Current Parameters

Current development parameters:

| Parameter | Value | Status |
|---|---:|---|
| Traction motor | Port A | Confirmed |
| Steering motor | Port E | Confirmed |
| Distance sensor | Port B | Confirmed |
| Color sensor | Port F | Confirmed |
| Steering center | 0° | Current reference |
| Right steering | -100° | Experimental |
| Left steering | +100° | Experimental |
| Steering speed | 100 deg/s | Experimental |
| Driving speed | 200 deg/s | Development value |
| Color detection distance | Approx. 6 cm | Observed |
| Distance threshold | TBD | Pending validation |

---

# 20. Final Testing Plan

Additional track testing will be used to determine the final parameters.

The following tests are planned:

1. Right steering calibration.
2. Left steering calibration.
3. Steering center recovery.
4. Straight-line stability.
5. Distance sensor threshold.
6. Red pillar detection during movement.
7. Green pillar detection during movement.
8. Right obstacle avoidance.
9. Left obstacle avoidance.
10. Counter-steering.
11. Trajectory recovery.
12. Corner navigation.
13. Complete autonomous run.

Each important test will be repeated to evaluate consistency.

---

# 21. Test Record Template

The following table will be updated with measured results:

| Test | Attempt 1 | Attempt 2 | Attempt 3 | Attempt 4 | Attempt 5 | Result |
|---|---|---|---|---|---|---|
| Steering center recovery | TBD | TBD | TBD | TBD | TBD | TBD |
| Red detection | TBD | TBD | TBD | TBD | TBD | TBD |
| Green detection | TBD | TBD | TBD | TBD | TBD | TBD |
| Right obstacle avoidance | TBD | TBD | TBD | TBD | TBD | TBD |
| Left obstacle avoidance | TBD | TBD | TBD | TBD | TBD | TBD |
| Trajectory recovery | TBD | TBD | TBD | TBD | TBD | TBD |
| Corner navigation | TBD | TBD | TBD | TBD | TBD | TBD |

---

# 22. Current Project Status

## Completed or currently operational

- Four-wheel vehicle structure.
- Traction motor installation.
- Mechanical front steering.
- Steering motor control.
- Steering center reference.
- Traction control.
- Red color recognition.
- Green color recognition.
- Color detection while moving.
- Distance sensor reading.
- Integration of motors and sensors into the current software.

## Under Development / Calibration

- Final steering limits.
- Distance threshold.
- Obstacle passing trajectory.
- Counter-steering.
- Trajectory recovery.
- Corner navigation.
- Final driving speed.
- Complete autonomous challenge.
- Parking strategy.

---

# 23. Engineering Conclusion

The development of the Stars Double K autonomous vehicle is based on continuous testing and improvement.

One of the most useful lessons from the current development stage was the steering calibration failure. Increasing the steering movement initially appeared to be a solution to insufficient turning, but excessive movement caused the vehicle to lose its centered steering position and follow a circular trajectory.

This result changed the team's approach from simply increasing steering movement to progressively calibrating the complete mechanical system.

The integration of traction, steering, color detection and distance measurement represents the foundation of the current autonomous system.

Further track testing will be used to replace preliminary parameters with measured values and improve the reliability of the complete autonomous navigation strategy.

---

**Stars Double K**  
**WRO 2026 Future Engineers**
