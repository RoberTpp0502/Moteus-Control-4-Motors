import argparse
import asyncio
import math
import moteus

async def main():
    parser = argparse.ArgumentParser()
    moteus.make_transport_args(parser)
    args = parser.parse_args()

    transport = moteus.get_singleton_transport(args)

    c1 = moteus.Controller(id=1, transport=transport)
    c2 = moteus.Controller(id=2, transport=transport)
    c3 = moteus.Controller(id=3, transport=transport)
    c4 = moteus.Controller(id=4, transport=transport)

    while True:
        results = await asyncio.gather(
            c1.set_position(position=math.nan, velocity=1.0, accel_limit=0.5, query=True),
            c2.set_position(position=math.nan, velocity=0.5, accel_limit=0.25, query=True),
            c3.set_position(position=math.nan, velocity=1.0, accel_limit=0.5, query=True),
            c4.set_position(position=math.nan, velocity=0.5, accel_limit=0.25, query=True),
        )

        # Print ID and position for each motor
        print(", ".join(
            f"ID {r.source}: {r.values[moteus.Register.POSITION]}"
            for r in results
        ))

        await asyncio.sleep(0.01)


if __name__ == "__main__":
    asyncio.run(main())