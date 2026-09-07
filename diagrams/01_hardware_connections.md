# Hardware Connection Diagram

## Stars Double K – WRO 2026 Future Engineers

The autonomous vehicle is controlled using a LEGO Education SPIKE Prime Hub.

The current hardware connections are:

```text
                    LEGO SPIKE PRIME HUB
                 ┌─────────────────────────┐
                 │                         │
 Traction Motor ─┤ PORT A                  │
                 │                         │
Distance Sensor ─┤ PORT B                  │
                 │                         │
 Steering Motor ─┤ PORT E                  │
                 │                         │
   Color Sensor ─┤ PORT F                  │
                 │                         │
                 └─────────────────────────┘
```

## Port Configuration

| Port | Component | Function |
|------|-----------|----------|
| A | Traction Motor | Forward and reverse movement |
| B | Distance Sensor | Measures distance from surrounding objects |
| E | Steering Motor | Controls the mechanical front steering system |
| F | Color Sensor | Detects red and green traffic pillars |

## System Interaction

```text
Distance Sensor (B) ───┐
                       │
Color Sensor (F) ──────┼──→ SPIKE Prime Hub
                       │          │
                       │          ├──→ Traction Motor (A)
                       │          │
                       │          └──→ Steering Motor (E)
                       │
                       └── Environmental information
```

The sensors provide information about the environment to the SPIKE Prime Hub.

The program processes this information and controls the traction and steering motors to produce autonomous vehicle movement.

The color sensor is currently positioned to detect the red and green traffic pillars. During preliminary testing, color detection was observed at approximately 6 cm.

The distance sensor is integrated into the system, while its final operating threshold is still pending track calibration.
