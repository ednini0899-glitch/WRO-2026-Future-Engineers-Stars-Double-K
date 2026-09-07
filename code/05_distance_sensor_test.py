from hub import port
import distance_sensor
import runloop

# ============================================================
# Stars Double K
# WRO 2026 Future Engineers
# Distance Sensor Test
# ============================================================

DISTANCE_SENSOR = port.B


async def main():

    while True:

        distance = distance_sensor.distance(DISTANCE_SENSOR)

        print("Distance:", distance)

        # Short pause to avoid printing too fast
        await runloop.sleep_ms(100)


runloop.run(main())
