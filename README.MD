Windows:python -m pip install moteus-gui  AND pip install moteus
Linux:python -m pip install moteus-gui AND pip install moteus
BEST look at https://mjbots.github.io/moteus/ for best DOC, also in hid Disc sv is very active.
mover_rover=it was one of a projects made it by a university team. Since i made the teleometry of the rover i will share what u neeed, for example for a Rover with a diferential move(like a tank) you have to consider that he will make a curve just when left or right motors are less powerfull than others.
        misc_st = v - (w * self.dist_roti / 2.0)
        misc_dr = v + (w * self.dist_roti / 2.0)
If u want to be more precisely u need to calculate also rps
        rps_st = misc_st / (2 * math.pi * self.raza_roata)
        rps_dr = misc_dr / (2 * math.pi * self.raza_roata)
St-left
dr-right
To add more or less motors just delete the id and the async for them
