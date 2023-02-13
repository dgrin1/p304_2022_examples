###################################################

#
#This plots 3 functions of motions
#
#One plot of the omega_x spin with a wind in the same direction of the spin,
#one in the opposite direction of the spin,
#and one with no spin and a cross wind
#
# The spin in this case is a x spin, with a football this is a spiral




#important values
#Drag coefficient, taken as 0.45 (dimensionless)
# cd = 0.45

#mass of football
#m = 0.411

#radius

#length
#l = 0.282 m

#radius of football (m)
#R = 0.086

# A is the cross-sectional area of the football
#A = 0.114938 m^2

# moments of inertia
#I_1 = 0.002829
#I_3 = 0.001982


#initial velocities and angle
# 20 ms
# 60 degrees

###################################################




from scipy.integrate import odeint
from numpy import sin,cos,exp,linspace,pi,sqrt,arange,array
from pylab import show, plot,ylim,xlim,figure,legend,xlabel,ylabel


sfont = {'fontname':'Serif'}


#constants
#Acceleration due to gravity (m/s^2)
g = 9.81
#Air density (kg/m^3)
rho = 1.22
#Drag coefficient, taken as 0.45 (dimensionless)
cd = 0.49
#Multiplying constant for lift force
clcoef1 = 3.187*10**-1
#Multiplying factor for angular velocity
clcoef2 = 2.483*10**-3


#mass of football
m = 0.411



####################################################
#spin and wind
####################################################

def projectile_motion_function(r,t):

    #adjust these to adjust the wind
    #x, y and z components of the wind velocity, assumed to be independent of x, y, z and t

    W_x = 0.0
    W_y = -10.0
    W_z = 0.0


    # A is the cross-sectional area of the projectile.

    A = 0.114938
    kd = -0.5*rho*A*cd





    #postion components
    x = r[0]
    y = r[1]
    z = r[2]

    #velocity components
    v_x = r[3] #v_x
    v_y = r[4] #v_y
    v_z = r[5] #v_z

    theta = r[6]
    om_x = r[7]
    phi = r[8]
    om_y = r[9]
    psi = r[10]
    om_z = r[11]

    # vmw is the magnitude of [vector v - vector W]
    # equation (17).

    vmw = sqrt((v_x-W_x)**2 + (v_y-W_y)**2 + (v_z-W_z)**2)

############################################################################
############################################################################
#######  Spinning function
############################################################################


    #constants
    #Acceleration due to gravity (m/s^2).
    g = 9.81
    #mass of football (kg)
    M = 0.411
    #radius of football (m)
    R = 0.086

    #length of the football
    l = 0.282

    #football kgm^2
    I_1 = 0.002829
    I_3 = 0.001982



    #equations of motion
    dtheta_dt = om_y
    d_om_y= (om_z**2*sin(theta)*cos(theta)*(I_1-I_3)-I_3*om_z*om_x*sin(theta)+M*g*l*sin(theta))/I_1


    dphi_dt = om_z
    if theta == 0:
        d_om_z = 0

    else:
        d_om_z = (2*(I_3-I_1)*om_z*om_y*sin(theta)*cos(theta)-I_3*om_z*om_y*sin(theta)*cos(theta)+I_3*om_x*om_y*sin(theta))/(I_1*(sin(theta))**2)


    dpsi_dt = om_x
    d_om_x = om_z*om_y*sin(theta)-d_om_z*cos(theta)


############################################################################
############################################################################


    # omega = angular vel. magnitude.
    omega = sqrt(om_x**2 + om_y**2 + om_z**2)

    # Lift Coeff. (dimensionless).
    cl = clcoef1*(1 - exp(-clcoef2*omega))

    kl = 0.5*rho*A*cl

#when omega = 0, then there is a values divided by 0, which causes an error
#need to add an if statemnt for when omega = 0
    if omega == 0:
        #define new equations

        #################################################################################

        #second order differntial equation, broke into two first order equations
        #x components

        #velocity and acceleration in the x direction

            dx_dt = v_x #velocity in the x direction


            # eqs (14) & (30)
            #dy[2] = (vmw/m)*(kd*(v_x-W_x)+ kl*(om_y*(v_z-W_z) - om_z*(v_y-W_y))/omega)

            #rewrite (my version)
            dvx_dt = (vmw/m)*(kd*(v_x-W_x))

        #################################################################################
        #y components

            # y direction; cf equation (29)
            dy_dt = v_y
            # equation (15); cf (30)

            #rewrite (my version)
            dvy_dt = (vmw/m)*(kd*(v_y-W_y))

        #################################################################################
        #z components

            # z direction; cf equation (29)
            dz_dt = v_z
            #eq. (16); cf (30)

            #rewrite (my version)
            dvz_dt = (vmw/m)*(kd*(v_z-W_z)) - g

        #################################################################################


            return array([dx_dt, dy_dt, dz_dt, dvx_dt, dvy_dt, dvz_dt, dtheta_dt, d_om_x, dphi_dt, d_om_y, dpsi_dt, d_om_z], float)

        #################################################################################

    else:
        #################################################################################

        #second order differntial equation, broke into two first order equations
        #x components

        #velocity and acceleration in the x direction

            dx_dt = v_x #velocity in the x direction

            # eqs (14) & (30)

            #rewrite (my version)
            dvx_dt = (vmw/m)*(kd*(v_x-W_x)+kl*((om_y*(v_z-W_z)-om_z*(v_y-W_y))/omega))

        #################################################################################
        #y components

            # y direction; cf equation (29)
            dy_dt = v_y
            # equation (15); cf (30)

            #rewrite (my version)
            dvy_dt = (vmw/m)*(kd*(v_y-W_y)+kl*((om_z*(v_x-W_x)-om_x*(v_z-W_z))/omega))

        #################################################################################
        #z components

            # z direction; cf equation (29)
            dz_dt = v_z
            #eq. (16); cf (30)

            #rewrite (my version)
            dvz_dt = (vmw/m)*(kd*(v_z-W_z)+kl*((om_x*(v_y-W_y)-om_y*(v_x-W_x))/omega))- g

        #################################################################################


            return array([dx_dt, dy_dt, dz_dt, dvx_dt, dvy_dt, dvz_dt, dtheta_dt, d_om_x, dphi_dt, d_om_y, dpsi_dt, d_om_z], float)

        #################################################################################



#initial conditions
x0 = 0
y0 = 0
z0 = 0


#initial velocity
v_x0 = 25*cos(50*(pi/180))
v_y0 = 0
v_z0 = 25*cos(50*(pi/180))

#initial values
theta_0 = 0
om_x0 = 60
phi_0 = 0
om_y_0 = 0
psi_0 = 0
om_z_0 = 0


#################################################################################
#################################################################################
#4th order Runge-Kutta

a = 0
b = 5
N = 10000
h = (b-a)/N

#values of t we want to go over
tpoints = arange(a,b,h)


xpoints = []
ypoints = []
zpoints = []

v_xpoints = []
v_ypoints = []
v_zpoints = []

theta_points = []
om_xpoints = []
phi_points = []
om_y_points =[]
psi_points = []
om_z_points = []

r = array([x0, y0, z0, v_x0, v_y0, v_z0, theta_0, om_x0, phi_0, om_y_0, psi_0, om_z_0],float)

for t in tpoints:

#postion components
    xpoints.append(r[0])
    ypoints.append(r[1])
    zpoints.append(r[2])

#velocity components
    v_xpoints.append(r[3])
    v_ypoints.append(r[4])
    v_zpoints.append(r[5])

#spin components
    theta_points.append(r[6])
    om_xpoints.append(r[7])
    phi_points.append(r[8])
    om_y_points.append(r[9])
    psi_points.append(r[10])
    om_z_points.append(r[11])


    k1 = h*projectile_motion_function(r,t)
    k2 = h*projectile_motion_function(r+0.5*k1, t+0.5*h)
    k3 = h*projectile_motion_function(r+0.5*k2, t+0.5*h)
    k4 = h*projectile_motion_function(r+k3, t+h)
    r += (k1+2*k2+2*k3+k4)/6


#################################################################################

#plotting projectile motion
figure(1)
ylim(top=6)
ylim(bottom=0)
plot(xpoints, zpoints,'--g',label='Spin w Wind')









####################################################
#no spin and wind
####################################################



def projectile_motion_function1(r,t):


    #adjust these to adjust the wind
    #x, y and z components of the wind velocity, assumed to be independent of x, y, z and t

    W_x = 0.0
    W_y = -10.0
    W_z = 0.0


    # A is the cross-sectional area of the projectile.
    #A = pi*(D/2)**2
    A = 0.114938
    kd = -0.5*rho*A*cd





    #postion components
    x = r[0]
    y = r[1]
    z = r[2]

    #velocity components
    v_x = r[3] #v_x
    v_y = r[4] #v_y
    v_z = r[5] #v_z

    theta = r[6]
    om_x = r[7]
    phi = r[8]
    om_y = r[9]
    psi = r[10]
    om_z = r[11]

    # vmw is the magnitude of [vector v - vector W]

    vmw = sqrt((v_x-W_x)**2 + (v_y-W_y)**2 + (v_z-W_z)**2)

############################################################################
############################################################################
#######  Spinning function
############################################################################


    #constants
    #Acceleration due to gravity (m/s^2).
    g = 9.81
    #mass of top (kg)
    M = 0.411
    #radius of top (m)
    R = 0.086

    #length of the top
    l = 0.282

    #football kgm^2
    I_1 = 0.002829
    I_3 = 0.001982



    #equations of motion
    dtheta_dt = om_y
    d_om_y= (om_z**2*sin(theta)*cos(theta)*(I_1-I_3)-I_3*om_z*om_x*sin(theta)+M*g*l*sin(theta))/I_1


    dphi_dt = om_z
    if theta == 0:
        d_om_z = 0

    else:
        d_om_z = (2*(I_3-I_1)*om_z*om_y*sin(theta)*cos(theta)-I_3*om_z*om_y*sin(theta)*cos(theta)+I_3*om_x*om_y*sin(theta))/(I_1*(sin(theta))**2)


    dpsi_dt = om_x
    d_om_x = om_z*om_y*sin(theta)-d_om_z*cos(theta)


############################################################################
############################################################################


    # omega = angular vel. magnitude.
    omega = sqrt(om_x**2 + om_y**2 + om_z**2)

    # Lift Coeff. (dimensionless).
    cl = clcoef1*(1 - exp(-clcoef2*omega))

    kl = 0.5*rho*A*cl

#when omega = 0, then there is a values divided by 0, which causes an error
#need to add an if statemnt for when omega = 0
    if omega == 0:
        #define new equations

        #################################################################################

        #second order differntial equation, broke into two first order equations
        #x components

        #velocity and acceleration in the x direction

            dx_dt = v_x #velocity in the x direction


            # eqs (14) & (30)
            #dy[2] = (vmw/m)*(kd*(v_x-W_x)+ kl*(om_y*(v_z-W_z) - om_z*(v_y-W_y))/omega)

            #rewrite (my version)
            dvx_dt = (vmw/m)*(kd*(v_x-W_x))

        #################################################################################
        #y components

            # y direction; cf equation (29)
            dy_dt = v_y
            # equation (15); cf (30)

            #rewrite (my version)
            dvy_dt = (vmw/m)*(kd*(v_y-W_y))

        #################################################################################
        #z components

            # z direction; cf equation (29)
            dz_dt = v_z
            #eq. (16); cf (30)

            #rewrite (my version)
            dvz_dt = (vmw/m)*(kd*(v_z-W_z)) - g

        #################################################################################


            return array([dx_dt, dy_dt, dz_dt, dvx_dt, dvy_dt, dvz_dt, dtheta_dt, d_om_x, dphi_dt, d_om_y, dpsi_dt, d_om_z], float)

        #################################################################################

    else:
        #################################################################################

        #second order differntial equation, broke into two first order equations
        #x components

        #velocity and acceleration in the x direction

            dx_dt = v_x #velocity in the x direction

            # eqs (14) & (30)

            #rewrite (my version)
            dvx_dt = (vmw/m)*(kd*(v_x-W_x)+kl*((om_y*(v_z-W_z)-om_z*(v_y-W_y))/omega))

        #################################################################################
        #y components

            # y direction; cf equation (29)
            dy_dt = v_y
            # equation (15); cf (30)

            #rewrite (my version)
            dvy_dt = (vmw/m)*(kd*(v_y-W_y)+kl*((om_z*(v_x-W_x)-om_x*(v_z-W_z))/omega))

        #################################################################################
        #z components

            # z direction; cf equation (29)
            dz_dt = v_z
            #eq. (16); cf (30)

            #rewrite (my version)
            dvz_dt = (vmw/m)*(kd*(v_z-W_z)+kl*((om_x*(v_y-W_y)-om_y*(v_x-W_x))/omega))- g

        #################################################################################


            return array([dx_dt, dy_dt, dz_dt, dvx_dt, dvy_dt, dvz_dt, dtheta_dt, d_om_x, dphi_dt, d_om_y, dpsi_dt, d_om_z], float)

        #################################################################################



#initial conditions
x0 = 0
y0 = 0
z0 = 0


#initial velocity
v_x0 = 25*cos(50*(pi/180))
v_y0 = 0
v_z0 = 25*cos(50*(pi/180))

#initial values
theta_0 = 0
om_x0 = 0
phi_0 = 0
om_y_0 = 0
psi_0 = 0
om_z_0 = 0


#################################################################################
#################################################################################
#4th order Runge-Kutta

a = 0
b = 5
N = 10000
h = (b-a)/N

#values of t we want to go over
tpoints = arange(a,b,h)


xpoints = []
ypoints = []
zpoints = []

v_xpoints = []
v_ypoints = []
v_zpoints = []

theta_points = []
om_xpoints = []
phi_points = []
om_y_points =[]
psi_points = []
om_z_points = []

r = array([x0, y0, z0, v_x0, v_y0, v_z0, theta_0, om_x0, phi_0, om_y_0, psi_0, om_z_0],float)

for t in tpoints:

#postion components
    xpoints.append(r[0])
    ypoints.append(r[1])
    zpoints.append(r[2])

#velocity components
    v_xpoints.append(r[3])
    v_ypoints.append(r[4])
    v_zpoints.append(r[5])

#spin components
    theta_points.append(r[6])
    om_xpoints.append(r[7])
    phi_points.append(r[8])
    om_y_points.append(r[9])
    psi_points.append(r[10])
    om_z_points.append(r[11])


    k1 = h*projectile_motion_function1(r,t)
    k2 = h*projectile_motion_function1(r+0.5*k1, t+0.5*h)
    k3 = h*projectile_motion_function1(r+0.5*k2, t+0.5*h)
    k4 = h*projectile_motion_function1(r+k3, t+h)
    r += (k1+2*k2+2*k3+k4)/6


#################################################################################

#plotting projectile motion


plot(xpoints, zpoints,'k',label='No-Spin w +Wind')














####################################################
#spin and no wind
####################################################



def projectile_motion_function2(r,t):


    #adjust these to adjust the wind
    #x, y and z components of the wind velocity, assumed to be independent of x, y, z and t

    W_x = 0.0
    W_y = 10.0
    W_z = 0.0


    # A is the cross-sectional area of the projectile.
    #A = pi*(D/2)**2
    A = 0.114938
    kd = -0.5*rho*A*cd



    #postion components
    x = r[0]
    y = r[1]
    z = r[2]

    #velocity components
    v_x = r[3] #v_x
    v_y = r[4] #v_y
    v_z = r[5] #v_z

    theta = r[6]
    om_x = r[7]
    phi = r[8]
    om_y = r[9]
    psi = r[10]
    om_z = r[11]

    # vmw is the magnitude of [vector v - vector W]
    # equation (17).

    vmw = sqrt((v_x-W_x)**2 + (v_y-W_y)**2 + (v_z-W_z)**2)

############################################################################
############################################################################
#######  Spinning function
############################################################################


    #constants
    #Acceleration due to gravity (m/s^2).
    g = 9.81
    #mass of top (kg)
    M = 0.411
    #radius of top (m)
    R = 0.086

    #length of the top
    l = 0.282

    #football kgm^2
    I_1 = 0.002829
    I_3 = 0.001982



    #equations of motion
    dtheta_dt = om_y
    d_om_y= (om_z**2*sin(theta)*cos(theta)*(I_1-I_3)-I_3*om_z*om_x*sin(theta)+M*g*l*sin(theta))/I_1


    dphi_dt = om_z
    if theta == 0:
        d_om_z = 0

    else:
        d_om_z = (2*(I_3-I_1)*om_z*om_y*sin(theta)*cos(theta)-I_3*om_z*om_y*sin(theta)*cos(theta)+I_3*om_x*om_y*sin(theta))/(I_1*(sin(theta))**2)


    dpsi_dt = om_x
    d_om_x = om_z*om_y*sin(theta)-d_om_z*cos(theta)


############################################################################
############################################################################


    # omega = angular vel. magnitude.
    omega = sqrt(om_x**2 + om_y**2 + om_z**2)

    # Lift Coeff. (dimensionless).
    cl = clcoef1*(1 - exp(-clcoef2*omega))

    kl = 0.5*rho*A*cl

#when omega = 0, then there is a values divided by 0, which causes an error
#need to add an if statemnt for when omega = 0
    if omega == 0:
        #define new equations

        #################################################################################

        #second order differntial equation, broke into two first order equations
        #x components

        #velocity and acceleration in the x direction

            dx_dt = v_x #velocity in the x direction


            # eqs (14) & (30)
            #dy[2] = (vmw/m)*(kd*(v_x-W_x)+ kl*(om_y*(v_z-W_z) - om_z*(v_y-W_y))/omega)

            #rewrite (my version)
            dvx_dt = (vmw/m)*(kd*(v_x-W_x))

        #################################################################################
        #y components

            # y direction; cf equation (29)
            dy_dt = v_y
            # equation (15); cf (30)

            #rewrite (my version)
            dvy_dt = (vmw/m)*(kd*(v_y-W_y))

        #################################################################################
        #z components

            # z direction; cf equation (29)
            dz_dt = v_z
            #eq. (16); cf (30)

            #rewrite (my version)
            dvz_dt = (vmw/m)*(kd*(v_z-W_z)) - g

        #################################################################################


            return array([dx_dt, dy_dt, dz_dt, dvx_dt, dvy_dt, dvz_dt, dtheta_dt, d_om_x, dphi_dt, d_om_y, dpsi_dt, d_om_z], float)

        #################################################################################

    else:
        #################################################################################

        #second order differntial equation, broke into two first order equations
        #x components

        #velocity and acceleration in the x direction

            dx_dt = v_x #velocity in the x direction

            # eqs (14) & (30)

            #rewrite (my version)
            dvx_dt = (vmw/m)*(kd*(v_x-W_x)+kl*((om_y*(v_z-W_z)-om_z*(v_y-W_y))/omega))

        #################################################################################
        #y components

            # y direction; cf equation (29)
            dy_dt = v_y
            # equation (15); cf (30)

            #rewrite (my version)
            dvy_dt = (vmw/m)*(kd*(v_y-W_y)+kl*((om_z*(v_x-W_x)-om_x*(v_z-W_z))/omega))

        #################################################################################
        #z components

            # z direction; cf equation (29)
            dz_dt = v_z
            #eq. (16); cf (30)

            #rewrite (my version)
            dvz_dt = (vmw/m)*(kd*(v_z-W_z)+kl*((om_x*(v_y-W_y)-om_y*(v_x-W_x))/omega))- g

        #################################################################################


            return array([dx_dt, dy_dt, dz_dt, dvx_dt, dvy_dt, dvz_dt, dtheta_dt, d_om_x, dphi_dt, d_om_y, dpsi_dt, d_om_z], float)

        #################################################################################



#initial conditions
x0 = 0
y0 = 0
z0 = 0


#initial velocity
v_x0 = 25*cos(50*(pi/180))
v_y0 = 0
v_z0 = 25*cos(50*(pi/180))

#initial values
theta_0 = 0
om_x0 = 60
phi_0 = 0
om_y_0 = 0
psi_0 = 0
om_z_0 = 0


#################################################################################
#################################################################################
#4th order Runge-Kutta

a = 0
b = 5
N = 10000
h = (b-a)/N

#values of t we want to go over
tpoints = arange(a,b,h)


xpoints = []
ypoints = []
zpoints = []

v_xpoints = []
v_ypoints = []
v_zpoints = []

theta_points = []
om_xpoints = []
phi_points = []
om_y_points =[]
psi_points = []
om_z_points = []

r = array([x0, y0, z0, v_x0, v_y0, v_z0, theta_0, om_x0, phi_0, om_y_0, psi_0, om_z_0],float)

for t in tpoints:

    #postion components
    xpoints.append(r[0])
    ypoints.append(r[1])
    zpoints.append(r[2])

    #velocity components
    v_xpoints.append(r[3])
    v_ypoints.append(r[4])
    v_zpoints.append(r[5])

    #spin components
    theta_points.append(r[6])
    om_xpoints.append(r[7])
    phi_points.append(r[8])
    om_y_points.append(r[9])
    psi_points.append(r[10])
    om_z_points.append(r[11])


    k1 = h*projectile_motion_function2(r,t)
    k2 = h*projectile_motion_function2(r+0.5*k1, t+0.5*h)
    k3 = h*projectile_motion_function2(r+0.5*k2, t+0.5*h)
    k4 = h*projectile_motion_function2(r+k3, t+h)
    r += (k1+2*k2+2*k3+k4)/6


#################################################################################

#plotting projectile motion


plot(xpoints, zpoints,'--r',label='Spin w -Wind ')


legend(loc='upper right')
xlabel("Position, x (m)",**sfont)
ylabel("Position, z (m)",**sfont)


show()


show()
