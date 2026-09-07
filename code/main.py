from hub import port, light_matrix
import motor
import color_sensor
import color
import distance_sensor
import runloop

# ============================================================
# Stars Double K
# WRO 2026 Future Engineers
#
# MAIN PROGRAM - CURRENT DEVELOPMENT VERSION
#
# This program integrates the main systems of the autonomous
# vehicle. Calibration values may be modified after track tests.
# ============================================================


# ---------------- ROBOT CONFIGURATION ----------------

TRACTION_MOTOR = port.A
STEERING_MOTOR = port.E

DISTANCE_SENSOR = port.B
COLOR_SENSOR = port.F


# ---------------- MOVEMENT PARAMETERS ----------------

DRIVING_SPEED = 200
STEERING_SPEED = 100

CENTER = 0

# Experimental steering values
RIGHT_POSITION = -100
LEFT_POSITION = 100


# ---------------- SENSOR PARAMETERS ----------------

# The color sensor currently recognizes the traffic pillars
# at approximately 6 cm under preliminary testing conditions.

COLOR_DETECTION_DISTANCE_CM = 6

# Final distance sensor threshold will be determined
# during additional track testing.
DISTANCE_THRESHOLD = None


# ============================================================
# RED PILLAR MANEUVER
# ============================================================

async def red_pillar():

    print("RED PILLAR DETECTED")

    await light_matrix.write("R")

    # According to the current strategy,
    # the vehicle steers right when red is detected.
    await motor.run_to_relative_position(
        STEERING_MOTOR,
        RIGHT_POSITION,
        STEERING_SPEED
    )

    await runloop.sleep_ms(500)

    # Return steering toward center.
    await motor.run_to_relative_position(
        STEERING_MOTOR,
        CENTER,
        STEERING_SPEED
    )

    light_matrix.clear()


# ============================================================
# GREEN PILLAR MANEUVER
# ============================================================

async def green_pillar():

    print("GREEN PILLAR DETECTED")

    await light_matrix.write("V")

    # According to the current strategy,
    # the vehicle steers left when green is detected.
    await motor.run_to_relative_position(
        STEERING_MOTOR,
        LEFT_POSITION,
        STEERING_SPEED
    )

    await runloop.sleep_ms(500)

    # Return steering toward center.
    await motor.run_to_relative_position(
        STEERING_MOTOR,
        CENTER,
        STEERING_SPEED
    )

    light_matrix.clear()


# ============================================================
# MAIN AUTONOMOUS LOOP
# ============================================================

async def main():

    # IMPORTANT:
    # Front wheels must be positioned straight before
    # starting the program.

    motor.reset_relative_position(
        STEERING_MOTOR,
        CENTER
    )

    await runloop.sleep_ms(1000)

    print("STARS DOUBLE K")
    print("AUTONOMOUS SYSTEM STARTED")

    # Start forward movement.
    motor.run(
        TRACTION_MOTOR,
        DRIVING_SPEED
    )

    while True:

        # Read sensors.
        detected_color = color_sensor.color(
            COLOR_SENSOR
        )

        distance = distance_sensor.distance(
            DISTANCE_SENSOR
        )

        print("Distance:", distance)

        # --------------------------------------------
        # RED TRAFFIC PILLAR
        # --------------------------------------------

        if detected_color == color.RED:

            await red_pillar()

            # Prevent repeated immediate detection.
            await runloop.sleep_ms(500)

        # --------------------------------------------
        # GREEN TRAFFIC PILLAR
        # --------------------------------------------

        elif detected_color == color.GREEN:

            await green_pillar()

            # Prevent repeated immediate detection.
            await runloop.sleep_ms(500)

        # --------------------------------------------
        # NORMAL DRIVING
        # --------------------------------------------

        else:

            motor.run(
                TRACTION_MOTOR,
                DRIVING_SPEED
            )

        await runloop.sleep_ms(20)


runloop.run(main())
