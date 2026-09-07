from hub import port, light_matrix
import motor
import color_sensor
import color
import distance_sensor
import runloop

# ============================================================
# Stars Double K
# WRO 2026 Future Engineers
# Combined Sensor and Movement Test
# ============================================================

TRACTION_MOTOR = port.A
STEERING_MOTOR = port.E
DISTANCE_SENSOR = port.B
COLOR_SENSOR = port.F

DRIVING_SPEED = 200
STEERING_SPEED = 100

CENTER = 0
RIGHT_POSITION = -100
LEFT_POSITION = 100


async def main():

    # Front wheels must be manually centered
    # before starting the test.
    motor.reset_relative_position(STEERING_MOTOR, CENTER)

    await runloop.sleep_ms(1000)

    # Start forward movement.
    motor.run(TRACTION_MOTOR, DRIVING_SPEED)

    while True:

        detected_color = color_sensor.color(COLOR_SENSOR)
        distance = distance_sensor.distance(DISTANCE_SENSOR)

        print("Distance:", distance)
        print("Color:", detected_color)

        # ----------------------------------------------------
        # RED detection
        # ----------------------------------------------------
        if detected_color == color.RED:

            print("RED PILLAR DETECTED")
            await light_matrix.write("R")

            await motor.run_to_relative_position(
                STEERING_MOTOR,
                RIGHT_POSITION,
                STEERING_SPEED
            )

            await runloop.sleep_ms(500)

            await motor.run_to_relative_position(
                STEERING_MOTOR,
                CENTER,
                STEERING_SPEED
            )

            light_matrix.clear()

        # ----------------------------------------------------
        # GREEN detection
        # ----------------------------------------------------
        elif detected_color == color.GREEN:

            print("GREEN PILLAR DETECTED")
            await light_matrix.write("V")

            await motor.run_to_relative_position(
                STEERING_MOTOR,
                LEFT_POSITION,
                STEERING_SPEED
            )

            await runloop.sleep_ms(500)

            await motor.run_to_relative_position(
                STEERING_MOTOR,
                CENTER,
                STEERING_SPEED
            )

            light_matrix.clear()

        else:
            # Continue driving while no target color is detected.
            motor.run(TRACTION_MOTOR, DRIVING_SPEED)

        await runloop.sleep_ms(50)


runloop.run(main())
