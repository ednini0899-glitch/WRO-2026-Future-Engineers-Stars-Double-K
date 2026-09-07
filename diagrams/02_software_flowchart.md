# Autonomous Software Flowchart

## Stars Double K – WRO 2026 Future Engineers

This diagram represents the current control logic of the autonomous vehicle.

```text
                    ┌─────────────┐
                    │    START    │
                    └──────┬──────┘
                           │
                           ▼
                ┌─────────────────────┐
                │ Center front wheels │
                │   Steering = 0°     │
                └──────────┬──────────┘
                           │
                           ▼
                  ┌─────────────────┐
                  │  Move Forward   │
                  │ Motor A = 200   │
                  └────────┬────────┘
                           │
                           ▼
                 ┌──────────────────┐
                 │   Read Sensors   │
                 │ Color F / Dist B │
                 └────────┬─────────┘
                          │
                          ▼
                 ┌─────────────────┐
                 │ Color detected? │
                 └───────┬─────────┘
                         │
              ┌──────────┴──────────┐
              │                     │
              ▼                     ▼
        ┌───────────┐         ┌───────────┐
        │    RED    │         │   GREEN   │
        └─────┬─────┘         └─────┬─────┘
              │                     │
              ▼                     ▼
        Display "R"            Display "V"
              │                     │
              ▼                     ▼
        Steer Right             Steer Left
              │                     │
              └──────────┬──────────┘
                         │
                         ▼
                ┌──────────────────┐
                │ Return steering  │
                │ toward center    │
                └────────┬─────────┘
                         │
                         ▼
                ┌──────────────────┐
                │ Continue Driving │
                └────────┬─────────┘
                         │
                         └──────→ READ SENSORS
```

## Current Control Strategy

The autonomous program continuously reads the sensors while the vehicle is moving.

### Red Traffic Pillar

When the color sensor detects red:

```text
RED → Display R → Steer Right → Recover Steering
```

### Green Traffic Pillar

When the color sensor detects green:

```text
GREEN → Display V → Steer Left → Recover Steering
```

## Distance Sensor

The distance sensor connected to Port B is currently integrated into the software for measurement and monitoring.

Its final decision threshold is still pending track calibration.

## Future Development

The current flowchart represents the development version of the software.

The next stage will incorporate:

- Distance thresholds
- Counter-steering
- Trajectory recovery
- Corner navigation
- Complete obstacle avoidance
- Parking strategy

These functions will be calibrated using track tests.
