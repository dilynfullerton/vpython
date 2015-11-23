__author__ = 'Alpha'

from visual import *

# Simple program where projectile follows path determined by forces applied to it


# Velocity is vector(number, number, number)

# Force is vector(number, number, number)

# Momentum is vector(number, number, number)

# Mass is number

# Position is vector(number, number, number)

# Acceleration is vector(number, number, number)

# Time is number


T_MAX = 1000
GRAV_ACCEL = vector(0, - 9.81, 0)
STEP = .01


# Mass Acceleration -> Force
def get_force(m, a):
    f = m * a
    return f


class Projectile:
    def __init__(self, m, s, p, t, f):
        self.m = m
        self.s = s
        self.p = p
        self.t = t
        self.f = f
        self.grav_force()

    # Projectile Force -> Projectile
    def update_p(self):
        p_f = self.p + self.f * STEP
        self.p = p_f

    # Projectile -> Projectile
    def update_s(self):
        s_f = self.s + STEP * self.p / self.m
        self.s = s_f

    # Projectile -> Projectile
    def update_t(self):
        t_f = self.t + STEP
        self.t = t_f

    # Projectile -> Force
    def grav_force(self):
        return get_force(self.m, GRAV_ACCEL)

    # Force (listof Force) -> Projectile
    def get_net_force(self, forces_on):
        f_net = self.grav_force() + net_force(forces_on)
        self.f = f_net

m0 = 1
s0 = vector(0, 0, 0)
p0 = vector(10, 20, 10)
t0 = 0
f0 = s0

BALL0 = Projectile(m0, s0, p0, t0, f0)
NO_OTHER_FORCES = [f0]
f_wind = vector(-1, -11, 4)
WIND = [f_wind]
MARKER_SCALE = .05
AXIS_SCALE = 70

SHOW_PATH = True
SHOW_POSITION_ARROW = True
SHOW_FORCE_ARROW = True
SHOW_MOMENTUM_ARROW = True


# (listof Force) -> Force
def net_force(forces):
    f_net = vector(0, 0, 0)
    for f in forces:
        f_net += f
    return f_net

# Projectile ->
def animate(projectile, forces):
    s_i = projectile.s

    projectile.get_net_force(forces)

    xscale = AXIS_SCALE
    yscale = AXIS_SCALE
    zscale = AXIS_SCALE

    width = .01 * AXIS_SCALE

    xaxis = arrow(axis=(xscale, 0, 0),
                  shaftwidth=width)
    yaxis = arrow(axis=(0, yscale, 0),
                  shaftwidth=width)
    zaxis = arrow(axis=(0, 0, zscale),
                  shaftwidth=width)

    unitx = (1, 0, 0)
    unity = (0, 1, 0)
    unitz = (0, 0, 1)

    image = sphere(pos=projectile.s,
                   radius=projectile.m,
                   color=color.red)

    if SHOW_PATH:
        points(pos=[image.pos],
               size=MARKER_SCALE*image.radius,
               color=image.color)


    if SHOW_POSITION_ARROW:
        position_arrow = arrow(pos=vector(0, 0, 0),
                               axis=image.pos,
                               color=color.blue,
                               shaftwidth=width)

    if SHOW_MOMENTUM_ARROW:
        momentum_arrow = arrow(pos=image.pos,
                               axis=projectile.p,
                               color=color.green,
                               shaftwidth=width)
    if SHOW_FORCE_ARROW:
        net_force_arrow = arrow(pos=image.pos,
                                axis=projectile.f,
                                color=color.yellow,
                                shaftwidth=width)

    while True:
        rate(1/STEP)
        if projectile.t > T_MAX:
            break
        elif projectile.s.y < s_i.y:
            break
        else:
            projectile.update_s()
            projectile.update_p()
            projectile.update_t()

            image.pos = projectile.s

            if SHOW_PATH:
                points(pos=[image.pos],
                       size=MARKER_SCALE*image.radius,
                       color=image.color)

            if SHOW_POSITION_ARROW:
                position_arrow.axis = image.pos

            if SHOW_MOMENTUM_ARROW:
                momentum_arrow.pos = image.pos
                momentum_arrow.axis = projectile.p

            if SHOW_FORCE_ARROW:
                net_force_arrow.pos = image.pos
                net_force_arrow.axis = projectile.f




#animate(BALL0, NO_OTHER_FORCES)
animate(BALL0, WIND)