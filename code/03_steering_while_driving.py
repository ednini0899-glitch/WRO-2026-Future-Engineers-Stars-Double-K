from hub import port
import motor
import runloop

# ============================================================
# Stars Double K
# WRO 2026 Future Engineers
# Steering While Driving Test
# ============================================================

TRACTION_MOTOR = port.A
STEERING_MOTOR = port.E

DRIVING_SPEED = 220
STEERING_SPEED = 100

CENTER = 0
RIGHT_POSITION = -100


async def main():

    # Before starting the test, the front wheels
    # must be manually positioned straight.

    # Establish straight position as steering reference.
    motor.reset_relative_position(STEERING_MOTOR, CENTER)

    await runloop.sleep_ms(1000)

    # --------------------------------------------------------
    # TEST 1 - Move forward
    # --------------------------------------------------------

    motor.run(TRACTION_MOTOR, DRIVING_SPEED)

    await runloop.sleep_ms(1500)

    # --------------------------------------------------------
    # TEST 2 - Steer while the vehicle is moving
    # --------------------------------------------------------

    await motor.run_to_relative_position(
        STEERING_MOTOR,
        RIGHT_POSITION,
        STEERING_SPEED
    )

    await runloop.sleep_ms(700)

    # Stop traction temporarily.
    motor.stop(TRACTION_MOTOR)

    await runloop.sleep_ms(500)

    # --------------------------------------------------------
    # TEST 3 - Return front wheels to center
    # --------------------------------------------------------

    await motor.run_to_relative_position(
        STEERING_MOTOR,
        CENTER,
        STEERING_SPEED
    )

    await runloop.sleep_ms(500)

    # --------------------------------------------------------
    # TEST 4 - Continue driving with centered steering
    # --------------------------------------------------------

    motor.run(TRACTION_MOTOR, DRIVING_SPEED)

    await runloop.sleep_ms(1500)

    # End test
    motor.stop(TRACTION_MOTOR)
    motor.stop(STEERING_MOTOR)


runloop.run(main())
