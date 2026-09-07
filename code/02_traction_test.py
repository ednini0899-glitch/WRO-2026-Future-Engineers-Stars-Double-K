from hub import port
import motor
import runloop

# ============================================================
# Stars Double K
# WRO 2026 Future Engineers
# Traction Motor Test
# ============================================================

# Robot configuration
TRACTION_MOTOR = port.A

# Experimental motor speed
TRACTION_SPEED = 200


async def main():

    # --------------------------------------------------------
    # TEST 1 - Traction motor movement
    # --------------------------------------------------------

    # Start the traction motor
    motor.run(TRACTION_MOTOR, TRACTION_SPEED)

    # Keep the motor running for 2 seconds
    await runloop.sleep_ms(2000)

    # Stop the vehicle
    motor.stop(TRACTION_MOTOR)

    await runloop.sleep_ms(1000)

    # --------------------------------------------------------
    # TEST 2 - Reverse motor rotation
    # --------------------------------------------------------

    motor.run(TRACTION_MOTOR, -TRACTION_SPEED)

    await runloop.sleep_ms(1000)

    # Stop traction motor
    motor.stop(TRACTION_MOTOR)


runloop.run(main())
