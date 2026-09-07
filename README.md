# WRO 2026 Future Engineers – Stars Double K

## Autonomous Vehicle Engineering Documentation

Welcome to the official engineering repository of **Stars Double K** for the **WRO 2026 Future Engineers** category.

This repository documents the development of our autonomous vehicle, including its mechanical design, steering system, sensors, programming, testing process, failures, improvements and autonomous navigation strategy.

Our objective is not only to develop a vehicle capable of completing the challenge, but also to document the engineering process used to design, test and improve the robot.

---

# 1. Team and Project

**Team:** Stars Double K  
**Competition:** WRO 2026  
**Category:** Future Engineers  
**Country:** Mexico  
**Platform:** LEGO Education SPIKE Prime  
**Programming:** Python  

The project consists of a four-wheel autonomous vehicle designed for the WRO Future Engineers challenge.

The robot uses a traction motor for movement and a separate motor connected to a mechanical steering mechanism for the front wheels.

This configuration allows the vehicle to move similarly to a conventional car instead of using differential steering.

---

# 2. Robot Overview

Our autonomous vehicle is divided into four main systems:

1. Traction system
2. Steering system
3. Sensor system
4. Autonomous control software

The LEGO SPIKE Prime Hub acts as the main controller.

## Port Configuration

| Port | Component | Function |
|------|-----------|----------|
| A | Motor | Vehicle traction |
| E | Motor | Front wheel steering |
| B | Distance Sensor | Distance and environment detection |
| F | Color Sensor | Red and green obstacle detection |

The internal motion sensor of the SPIKE Prime Hub can also be used during navigation tests to analyze changes in the orientation of the vehicle.

---

# 3. Mechanical Design

## 3.1 Chassis

The robot uses a four-wheel chassis designed to provide stability during straight movement and curves.

The SPIKE Prime Hub is located near the central section of the vehicle.

During the construction process, special attention was given to:

- Chassis rigidity
- Wheel alignment
- Steering movement
- Sensor placement
- Weight distribution
- Accessibility to the Hub and motors

Photographic documentation of the current robot can be found in:

[Robot Photographs](media/photos/)

---

# 4. Traction System

The traction motor is connected to **Port A**.

Its function is to move the vehicle forward and backward.

During development, the traction system was tested independently before integrating steering and sensor detection.

Different speeds are being evaluated because the optimal speed depends on the situation.

The vehicle can use a higher speed during straight sections and a lower speed during turns or obstacle avoidance.

This helps reduce trajectory errors and improves control.

---

# 5. Steering System

The steering motor is connected to **Port E**.

Instead of controlling the left and right wheels independently, this motor operates a mechanical system that changes the direction of the front wheels.

The steering system has been one of the most important parts of our testing process.

Small motor movements initially produced limited movement at the front wheels because the motor movement is transferred through the mechanical steering system.

For this reason, different steering values were tested experimentally.

---

## 5.1 Steering Center

Before running steering tests, the front wheels are manually placed in the straight position.

The relative position of the steering motor can then be established as the reference position.

Conceptually:

```text
0 = wheels centered
negative value = steering to one side
positive value = steering to the opposite side
```

This reference makes it possible to command the steering motor and then return the wheels toward the center.

---

## 5.2 Steering Calibration

Several steering angles were tested.

One of the first problems was that a small steering movement did not produce enough movement in the front wheels.

A larger steering angle was therefore tested.

However, increasing the steering movement too much created another problem: the wheels did not correctly return to the center.

As a result, the vehicle continued moving with the front wheels turned and completed an unintended circular trajectory.

This test demonstrated that the largest possible steering value is not necessarily the best value.

The steering angle must consider:

- Mechanical limits
- Gear movement
- Steering linkage
- Wheel angle
- Vehicle speed
- Ability to return to center

The current strategy is to calibrate the steering progressively instead of making large changes.

---

# 6. Sensor System

The vehicle currently uses two external sensors.

## 6.1 Color Sensor – Port F

The color sensor is used to identify the red and green traffic pillars used during the obstacle challenge.

The current program can distinguish between:

- Red
- Green

During testing, the SPIKE Prime Hub also provides visual feedback when a color is detected.

For example:

```text
R = Red detected
V = Green detected
```

This allows the team to verify that the sensor recognized the correct color before analyzing the steering response.

---

## 6.2 Distance Sensor – Port B

The distance sensor is connected to **Port B**.

Its purpose is to provide information about the environment in front of the vehicle.

During development, distance measurements are used to experiment with the detection of walls, track sections or areas where the robot must prepare to turn.

The final distance thresholds will be determined through testing on the competition field.

---

# 7. Autonomous Driving Strategy

The autonomous program is being developed progressively.

Instead of attempting to program the entire challenge at once, each subsystem is tested independently.

Our development sequence is:

```text
Traction test
      ↓
Steering test
      ↓
Steering center calibration
      ↓
Forward movement
      ↓
Color detection
      ↓
Distance detection
      ↓
Obstacle response
      ↓
Trajectory recovery
      ↓
Complete autonomous navigation
```

This method makes it easier to identify the source of an error.

---

# 8. Traffic Pillar Detection

The robot uses the color sensor on Port F to identify traffic pillars.

The current logic is based on the detected color.

```text
Vehicle moving
      ↓
Read color sensor
      ↓
Is RED detected?
   ↙         ↘
 YES         NO
  ↓           ↓
Red           Check GREEN
maneuver
              ↓
          GREEN detected
              ↓
          Green maneuver
```

The Hub displays the detected color during testing.

---

# 9. Obstacle Avoidance Development

The first obstacle tests focused on making the vehicle react to red and green while moving.

A basic reaction consists of:

```text
Detect color
      ↓
Change steering angle
      ↓
Continue moving
      ↓
Return steering toward center
```

However, returning the wheels to the center does not automatically return the complete vehicle to its previous trajectory.

For this reason, the next version of the avoidance algorithm is based on a complete maneuver:

```text
Detect obstacle
      ↓
Steer away
      ↓
Pass obstacle
      ↓
Counter-steer
      ↓
Recover trajectory
      ↓
Continue forward
```

This strategy will be calibrated using real track tests.

---

# 10. Software Architecture

The software is written in Python for the LEGO SPIKE Prime platform.

The program is divided into logical sections and functions to make testing and modification easier.

The main software tasks are:

- Initialize motors and sensors
- Establish steering reference
- Control traction
- Read the distance sensor
- Read the color sensor
- Identify red and green
- Control steering
- Execute obstacle maneuvers
- Recover the vehicle trajectory
- Continue autonomous navigation

Source code and individual tests are stored in:

[Source Code](code/)

---

# 11. Engineering Testing Process

Our engineering process is iterative.

We use the following cycle:

```text
PROBLEM
   ↓
IDEA
   ↓
MODIFICATION
   ↓
TEST
   ↓
RESULT
   ↓
ANALYSIS
   ↓
IMPROVEMENT
   ↓
NEW TEST
```

A failed test is not removed from the development history.

Failures provide useful information about mechanical and software limitations and help us make better engineering decisions.

---

# 12. Development Iterations

## Iteration 1 – Motor Function Identification

During the initial development process, the motors were tested independently to determine their real mechanical function.

The current configuration was confirmed as:

```text
Port A → Traction
Port E → Steering
```

This allowed the software structure to be reorganized according to the real mechanical configuration.

---

## Iteration 2 – Steering Movement

Initial steering tests showed that a small motor rotation produced insufficient movement of the front wheels.

The steering movement was increased progressively to obtain a more noticeable wheel angle.

### Result

The vehicle achieved a stronger turn.

### Lesson

Motor rotation and actual wheel angle are not equivalent because the movement is transferred through a mechanical steering system.

---

## Iteration 3 – Excessive Steering

A larger steering movement was tested to obtain a tighter turn.

### Result

The steering mechanism did not return correctly to the center.

The vehicle continued moving with the wheels turned and followed a circular trajectory.

### Engineering Decision

Reduce the steering movement and determine the useful steering range through progressive testing.

### Lesson

Mechanical limits must be considered in software calibration.

---

## Iteration 4 – Steering While Moving

After testing steering independently, traction was added to observe the real trajectory of the vehicle.

This was important because a steering angle that appears correct while the robot is stationary may produce a different result when the vehicle is moving.

### Engineering Decision

Steering calibration must be evaluated dynamically, not only while the robot is stationary.

---

## Iteration 5 – Color Detection

The color sensor connected to Port F was integrated into the program.

The program was developed to recognize red and green.

Visual feedback was added to the SPIKE Prime Hub to make sensor testing easier.

### Current behavior

```text
RED   → Hub displays R
GREEN → Hub displays V
```

---

## Iteration 6 – Color Detection While Driving

The first obstacle reaction tests included interruptions to traction.

The program was later modified so that the vehicle could continue moving while monitoring the color sensor.

This provided a better basis for developing continuous autonomous navigation.

---

# 13. Test Metrics

As development continues, test results will be recorded to compare configurations.

| Test | Parameter | Result |
|------|-----------|--------|
| Traction motor | Port A | Operational |
| Steering motor | Port E | Operational |
| Steering center | Reference position | Under calibration |
| Red detection | Port F | Detected |
| Green detection | Port F | Detected |
| Distance measurement | Port B | Under testing |
| Obstacle avoidance | Steering + color | Under development |
| Lane recovery | Counter-steering | Under development |
| Complete autonomous run | Full system | Under development |

Future tests will include repeated attempts so that reliability can be measured instead of relying on a single successful run.

---

# 14. Risks and Failure Modes

## Steering Mechanical Limit

**Risk:**  
The steering motor may move beyond the useful range of the mechanical linkage.

**Mitigation:**  
Increase steering values gradually and verify that the wheels can return to center.

---

## Steering Backlash

**Risk:**  
Mechanical play in the steering mechanism may cause the real wheel position to differ slightly from the commanded position.

**Mitigation:**  
Perform repeated center tests and calibrate the useful steering positions.

---

## Color Detection

**Risk:**  
Lighting, distance and sensor position can influence color readings.

**Mitigation:**  
Test the color sensor under different conditions and maintain consistent sensor placement.

---

## Vehicle Speed

**Risk:**  
Excessive speed may cause overshooting during curves and obstacle avoidance.

**Mitigation:**  
Use different speeds for straight movement and steering maneuvers.

---

# 15. Engineering Documentation

Detailed engineering notes are stored in:

[Engineering Journal](documentation/engineering_journal.md)

The journal documents the development process, including modifications, tests and engineering decisions.

---

# 16. Engineering Diagrams

Mechanical, sensor and software diagrams are organized in:

[Engineering Diagrams](diagrams/)

This section will include:

- Mechanical steering diagram
- Robot component layout
- Sensor and motor connection diagram
- Software flowchart

---

# 17. Robot Photographs

Photographic evidence is available in:

[Robot Photographs](media/photos/)

Current documented views include:

- Front view
- Right side view
- Top view

Additional views will be added to complete the photographic documentation.

---

# 18. Autonomous Driving Videos

Video evidence will be organized in:

[Autonomous Driving Videos](media/videos/)

The final documentation will include autonomous driving evidence for the developed challenge strategies.

---

# 19. Repository Structure

```text
WRO-2026-Future-Engineers-Stars-Double-K/
│
├── README.md
│
├── code/
│   └── README.md
│
├── documentation/
│   └── engineering_journal.md
│
├── diagrams/
│   └── README.md
│
└── media/
    ├── photos/
    │   ├── README.md
    │   ├── FRONTAL.jpg
    │   ├── DERECHA.jpg
    │   └── ARRIBA.jpg
    │
    └── videos/
        └── README.md
```

This structure separates source code, engineering documentation, diagrams and multimedia evidence.

---

# 20. How to Run the Robot

Before running the program:

1. Turn on the LEGO SPIKE Prime Hub.
2. Verify all motor and sensor connections.
3. Confirm the port configuration:

```text
A → Traction motor
E → Steering motor
B → Distance sensor
F → Color sensor
```

4. Place the front wheels in the straight position.
5. Load the appropriate Python program.
6. Place the robot in the test or starting area.
7. Start the autonomous program.
8. Observe the steering and sensor behavior.

Steering calibration must be checked before autonomous navigation tests.

---

# 21. Current Project Status

## Completed or Tested

- Four-wheel vehicle chassis
- Traction motor control
- Mechanical front steering
- Forward movement
- Steering movement
- Steering center testing
- Red color detection
- Green color detection
- Hub visual feedback
- Color detection while the vehicle is moving

## Currently Under Development

- Final steering calibration
- Distance-based navigation
- Complete red obstacle maneuver
- Complete green obstacle maneuver
- Counter-steering
- Trajectory recovery
- Corner navigation
- Full autonomous challenge strategy
- Final reliability testing

The status of these functions will be updated as testing continues.

---

# 22. Reproducibility

This repository is intended to provide enough information to understand how the robot was developed.

The documentation includes:

- Hardware configuration
- Motor and sensor ports
- Mechanical design explanation
- Steering calibration process
- Source code
- Sensor strategy
- Test results
- Failure analysis
- Engineering decisions
- Photographs
- Diagrams
- Video evidence

Our goal is to document not only the final vehicle but the complete engineering process behind it.

---

# 23. Conclusion

Stars Double K is developing an autonomous vehicle for the WRO 2026 Future Engineers challenge using LEGO Education SPIKE Prime.

The project combines mechanical design, sensors, programming and repeated experimental testing.

One of the most important lessons during development has been the relationship between software commands and real mechanical behavior. A motor value that appears correct in software does not necessarily produce the expected wheel angle or vehicle trajectory.

For this reason, our development process is based on testing, observation, measurement and progressive improvement.

Every test contributes information to the next version of the robot.

The repository will continue to be updated as the autonomous navigation system is improved and the final competition strategy is completed.

---

## Stars Double K

**WRO 2026 – Future Engineers**  
**Mexico**
