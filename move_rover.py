#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import moteus
import asyncio
import math

class RoverTeleop(Node):
    def __init__(self):
        super().__init__('RoverTeleop')
        self.dist_roti = 1.159
        self.raza_roata = 0.21
        self.sub = self.create_subscription(Twist, '/cmd_vel', self.comanda, 10)
        transport = moteus.get_singleton_transport()
        self.motoare = [moteus.Controller(id=i, transport=transport) for i in [1,2,3,4]]
        
    def comanda(self, msg):
        v = msg.linear.x
        w = msg.angular.z
        misc_st = v - (w * self.dist_roti / 2.0)
        misc_dr = v + (w * self.dist_roti / 2.0)
        rps_st = misc_st / (2 * math.pi * self.raza_roata)
        rps_dr = misc_dr / (2 * math.pi * self.raza_roata)
        
        asyncio.create_task(self.trimit_moteus(rps_st, rps_dr))

    async def trimit_moteus(self, rps_st, rps_dr):
        try:
            await self.motoare[0].set_velocity(velocity=rps_st, maximum_torque=1.5)
            await self.motoare[1].set_velocity(velocity=-rps_dr, maximum_torque=1.5)
            await self.motoare[2].set_velocity(velocity=rps_st, maximum_torque=1.5)
            await self.motoare[3].set_velocity(velocity=-rps_dr, maximum_torque=1.5)
        except Exception as e:
            self.get_logger().error(f"Eroare CAN: {e}")

def main(args=None):
    rclpy.init(args=args)
    node = RoverTeleop()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()