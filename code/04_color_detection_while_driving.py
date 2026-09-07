from hub import port, light_matrix
import motor
import color_sensor
import color
import runloop

# ============================================================
# Stars Double K
# WRO 2026 Future Engineers
# Color Detection While Driving
# ============================================================

TRACTION_MOTOR = port.A
STEERING_MOTOR = port.E
COLOR_SENSOR = port.F

DRIVING_SPEED = 200
STEERING_SPEED = 100

CENTER = 0
RIGHT_POSITION = -100
LEFT_POSITION = 100


async def red_detected():
    # Red pillar detected
    print("RED")
    await light_matrix.write("R")

    # Steer to the right
    await motor.run_to_relative_position(
        STEERING_MOTOR,
        RIGHT_POSITION,
        STEERING_SPEED
    )

    await runloop.sleep_ms(500)

    # Return steering to center
    await motor.run_to_relative_position(
        STEERING_MOTOR,
        CENTER,
        STEERING_SPEED
    )

    light_matrix.clear()


async def green_detected():
    # Green pillar detected
    print("GREEN")
    await light_matrix.write("V")

    # Steer to the left
    await motor.run_to_relative_position(
        STEERING_MOTOR,
        LEFT_POSITION,
        STEERING_SPEED
    )

    await runloop.sleep_ms(500)

    # Return steering to center
    await motor.run_to_relative_position(
        STEERING_MOTOR,
        CENTER,
        STEERING_SPEED
    )

    light_matrix.clear()


async def main():

    # Front wheels must be straight before starting.
    motor.reset_relative_position(STEERING_MOTOR, CENTER)

    await runloop.sleep_ms(1000)

    # Start autonomous forward movement.
    motor.run(TRACTION_MOTOR, DRIVING_SPEED)

    while True:

        detected_color = color_sensor.color(COLOR_SENSOR)

        if detected_color == color.RED:
            await red_detected()
            await runloop.sleep_ms(500)

        elif detected_color == color.GREEN:
            await green_detected()
            await runloop.sleep_ms(500)

        else:
            # Continue moving while no traffic
            # pillar color is detected.
            motor.run(TRACTION_MOTOR, DRIVING_SPEED)

        await runloop.sleep_ms(20)


runloop.run(main())
