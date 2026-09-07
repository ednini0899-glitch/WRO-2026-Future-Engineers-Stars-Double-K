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

# 13. Test Metrics and Current Configuration

The following information summarizes the current configuration and preliminary testing of the **Stars Double K** autonomous vehicle.

The robot is still undergoing calibration. Values identified as experimental correspond to configurations currently used during development and may be adjusted after additional track testing.

## 13.1 Current Robot Configuration

| Parameter | Current Value | Status |
|---|---:|---|
| Traction motor | Port A | Confirmed |
| Steering motor | Port E | Confirmed |
| Distance sensor | Port B | Confirmed |
| Color sensor | Port F | Confirmed |
| Color detection distance | Approx. 6 cm | Observed |
| Steering center reference | 0° | Current configuration |
| Normal driving speed | 200 deg/s | Current software setting |
| Steering motor speed | 100 deg/s | Current software setting |
| Right steering reference | -100° | Experimental |
| Left steering reference | +100° | Experimental |
| Distance threshold | TBD | Pending track validation |
| Complete obstacle avoidance | Under development | Pending validation |
| Complete autonomous navigation | Under development | Pending validation |

---

## 13.2 Color Sensor Test

The color sensor is connected to **Port F**.

During preliminary testing, the sensor was able to recognize the red and green traffic pillar colors at an approximate distance of **6 cm**.

This distance is currently used as a practical reference during development.

The actual detection behavior can be affected by:

- Lighting conditions
- Vehicle speed
- Sensor orientation
- Distance between the sensor and the traffic pillar
- Position of the traffic pillar relative to the vehicle

The current software recognizes:

```text
RED detected
      ↓
Hub displays "R"
      ↓
Execute red maneuver

GREEN detected
      ↓
Hub displays "V"
      ↓
Execute green maneuver
```

The final reliability percentage will be calculated after repeated tests under track conditions.

---

## 13.3 Steering Calibration

The steering motor is connected to **Port E**.

Before starting a test, the front wheels are positioned in the straight direction and this position is established as the steering reference.

Current reference:

```text
CENTER = 0°
```

The current experimental steering values are:

```text
Right steering reference: -100°
Left steering reference:  +100°
Steering speed:             100 deg/s
```

These values represent the current software configuration and are still being calibrated.

During development, different steering values were tested.

Initially, the front wheels did not turn enough to produce the desired trajectory. The steering movement was therefore increased.

When the steering movement was increased too much, the front wheels did not correctly return to the center position.

As a result, the vehicle continued moving with the wheels turned and followed an unintended circular trajectory.

This test showed that the steering range must be selected according to the mechanical limits of the steering system and not only according to the motor encoder value.

### Engineering Decision

The steering values will be increased or reduced progressively during testing until the vehicle can:

1. Produce the required turn.
2. Avoid reaching the mechanical steering limit.
3. Return the front wheels toward the center.
4. Continue with a stable trajectory after the maneuver.

---

## 13.4 Traction Test

The traction motor is connected to **Port A**.

The motor has been tested while the steering system is operating.

The current development speed is:

```text
Normal driving speed: 200 deg/s
```

This is a development configuration and not necessarily the final competition speed.

The final speed will be selected according to the balance between:

- Vehicle stability
- Sensor response time
- Steering accuracy
- Obstacle avoidance
- Corner performance

Higher speed can reduce the time available for sensor detection and steering correction, while lower speed provides more control but increases the total driving time.

---

## 13.5 Distance Sensor

The distance sensor is connected to **Port B**.

Its purpose is to provide information about the environment around the vehicle and support autonomous navigation.

The final distance threshold has not yet been established.

```text
Distance threshold: TBD
```

The threshold will be determined through track testing instead of selecting a final value without experimental evidence.

Tests will compare different detection distances and analyze their effect on the vehicle trajectory.

---

## 13.6 Current Obstacle Strategy

The current obstacle strategy combines:

- Continuous forward movement
- Color detection
- Steering control
- Steering center recovery

The current control concept is:

```text
START
  ↓
Move forward
  ↓
Read sensors
  ↓
Traffic color detected?
  ↓
 ┌───────────────┐
 │               │
RED             GREEN
 │               │
 ↓               ↓
Display R       Display V
 │               │
 ↓               ↓
Red maneuver    Green maneuver
 │               │
 └───────┬───────┘
         ↓
Recover trajectory
         ↓
Continue forward
```

The complete trajectory recovery maneuver is still under development.

The final strategy will use steering and counter-steering so that the vehicle does not only avoid the obstacle but also returns toward its intended driving trajectory.

---

## 13.7 Preliminary Engineering Targets

The following values represent engineering objectives for the final testing stage.

They are **targets and not measured success rates**.

| Engineering Objective | Target |
|---|---|
| Red pillar detection | Detect during autonomous movement |
| Green pillar detection | Detect during autonomous movement |
| Color working distance | Approx. 6 cm |
| Steering recovery | Return wheels close to straight |
| Straight movement | Maintain stable trajectory |
| Obstacle avoidance | Pass pillar without contact |
| Trajectory recovery | Return toward intended path |
| Corner navigation | Complete curve without leaving track |
| Autonomous operation | Operate without external control |

---

## 13.8 Final Validation Plan

The following parameters will be measured during the final testing stage:

| Test | Attempt 1 | Attempt 2 | Attempt 3 | Attempt 4 | Attempt 5 | Success Rate |
|---|---|---|---|---|---|---|
| Red detection | TBD | TBD | TBD | TBD | TBD | TBD |
| Green detection | TBD | TBD | TBD | TBD | TBD | TBD |
| Steering returns to center | TBD | TBD | TBD | TBD | TBD | TBD |
| Right obstacle maneuver | TBD | TBD | TBD | TBD | TBD | TBD |
| Left obstacle maneuver | TBD | TBD | TBD | TBD | TBD | TBD |
| Corner navigation | TBD | TBD | TBD | TBD | TBD | TBD |
| Trajectory recovery | TBD | TBD | TBD | TBD | TBD | TBD |

The success rate will be calculated using:

```text
Success Rate = Successful Attempts / Total Attempts × 100
```

For example, if four of five future attempts are successful:

```text
4 / 5 × 100 = 80%
```

This is only an example of the calculation method and is not a current measured result.

---

## 13.9 Parameters Pending Final Calibration

The following values will be updated after additional testing:

```text
Final right steering value:      TBD
Final left steering value:       TBD
Final steering center:           TBD
Final traction speed:            TBD
Final curve speed:               TBD
Final distance threshold:        TBD
Red maneuver timing:             TBD
Green maneuver timing:           TBD
Counter-steering timing:         TBD
```

Keeping these parameters marked as TBD allows the repository to distinguish between the current development configuration and experimentally validated competition values.

---

## 13.10 Current Development Status

### Confirmed / Tested

- Traction motor connected to Port A
- Steering motor connected to Port E
- Distance sensor connected to Port B
- Color sensor connected to Port F
- Vehicle forward movement
- Mechanical front steering
- Steering center reference
- Red color recognition
- Green color recognition
- Approximate 6 cm color detection distance
- Hub visual feedback for detected colors
- Color detection while the vehicle is moving

### Currently Under Calibration

- Final right steering angle
- Final left steering angle
- Steering center recovery
- Distance sensor threshold
- Obstacle avoidance trajectory
- Counter-steering
- Trajectory recovery
- Corner navigation
- Final driving speed
- Complete autonomous navigation

The repository will be updated as additional measurements and track tests are completed.
