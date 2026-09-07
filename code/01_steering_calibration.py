from hub import port
import motor
import runloop

# ============================================================
# Stars Double K
# WRO 2026 Future Engineers
# Steering Calibration Test
# ============================================================

# Robot configuration
STEERING_MOTOR = port.E

# Current experimental steering parameters
STEERING_SPEED = 100

CENTER = 0
RIGHT_POSITION = -100


async def main():

    # IMPORTANT:
    # Before starting this program, the front wheels
    # must be manually positioned straight.

    # Establish the current wheel position as 0 degrees.
    motor.reset_relative_position(STEERING_MOTOR, CENTER)

    await runloop.sleep_ms(1000)

    # --------------------------------------------------------
    # TEST 1 - Turn steering to the right
    # --------------------------------------------------------

    await motor.run_to_relative_position(
        STEERING_MOTOR,
        RIGHT_POSITION,
        STEERING_SPEED
    )

    # Keep the steering position for two seconds
    # so the mechanical movement can be observed.
    await runloop.sleep_ms(2000)

    # --------------------------------------------------------
    # TEST 2 - Return steering to center
    # --------------------------------------------------------

    await motor.run_to_relative_position(
        STEERING_MOTOR,
        CENTER,
        STEERING_SPEED
    )

    await runloop.sleep_ms(1000)

    # Stop steering motor
    motor.stop(STEERING_MOTOR)


runloop.run(main())
