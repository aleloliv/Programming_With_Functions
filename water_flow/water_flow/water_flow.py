def water_column_height(tower_height, tank_height):
    water_column_height = tower_height + (3 * tank_height / 4)
    return water_column_height
    
def pressure_gain_from_water_height(height):
    pressure = (WATER_DENSITY * EARTH_ACCELERATION_OF_GRAVITY * height) / 1000
    return pressure

def pressure_loss_from_pipe(pipe_diameter, pipe_length, friction_factor, fluid_velocity):
    if pipe_diameter == 0:
        return 0  # Handle division by zero
    pressure = ((-1 * friction_factor) * pipe_length * WATER_DENSITY * fluid_velocity ** 2) / (2000 * pipe_diameter)
    return pressure
    
def pressure_loss_from_fittings(fluid_velocity, quantity_fittings):
	pressure = ((-0.04 * WATER_DENSITY * fluid_velocity ** 2 * quantity_fittings)/2000)
	return pressure
	
def reynolds_number(hydraulic_diameter, fluid_velocity):
    reynolds = (WATER_DENSITY * hydraulic_diameter * fluid_velocity) / WATER_DYNAMIC_VISCOSITY
    return reynolds

def pressure_loss_from_pipe_reduction(larger_diameter, fluid_velocity, reynolds_number, smaller_diameter):
    if smaller_diameter == 0:
        return 0  # Handle division by zero
    k = ((0.1 + (50 / reynolds_number)) * (((larger_diameter / smaller_diameter) ** 4) -1))
    pressure = (-k * WATER_DENSITY * fluid_velocity ** 2) / 2000
    return pressure

def psi_from_kpa(kpa):
    psi = kpa * 0.14503773773020923
    return psi

def repetition(): # repeats main() if the user wants to
    repeat = False  # Initialize repeat to False
    hold = input("Would you like to repeat calculations? (Y or N) ")

    while hold != "Y" and hold != "N":
        hold = input("Please insert Y or N: ")

    if hold.upper() == "Y":
        repeat = True

    if repeat:
        main()

EARTH_ACCELERATION_OF_GRAVITY = 9.80665 # (meters / second²)
WATER_DENSITY = 998.2                   # (kilogram / meter³)
WATER_DYNAMIC_VISCOSITY = 0.0010016     # (meters / second)


PVC_SCHED80_INNER_DIAMETER = 0.28687    # (meters)  11.294 inches
PVC_SCHED80_FRICTION_FACTOR = 0.013     # (unitless)
SUPPLY_VELOCITY = 1.65                  # (meters / second)

HDPE_SDR11_INNER_DIAMETER = 0.048692    # (meters)  1.917 inches
HDPE_SDR11_FRICTION_FACTOR = 0.018      # (unitless)
HOUSEHOLD_VELOCITY = 1.75               # (meters / second)

def main():
    try: # I decided to add error handling in case the user inputs any other value than a number, as expected by the functions
        tower_height = float(input("Height of water tower (meters): "))
        tank_height = float(input("Height of water tank walls (meters): "))
        length1 = float(input("Length of supply pipe from tank to lot (meters): "))
        quantity_angles = int(input("Number of 90° angles in supply pipe: "))
        length2 = float(input("Length of pipe from supply to house (meters): "))
    except ValueError:
        print("Invalid input. Please enter valid numeric values.")
        return  # Exit the function

    water_height = water_column_height(tower_height, tank_height)
    pressure = pressure_gain_from_water_height(water_height)

    diameter = PVC_SCHED80_INNER_DIAMETER
    friction = PVC_SCHED80_FRICTION_FACTOR
    velocity = SUPPLY_VELOCITY
    reynolds = reynolds_number(diameter, velocity)
    loss = pressure_loss_from_pipe(diameter, length1, friction, velocity)
    pressure += loss

    loss = pressure_loss_from_fittings(velocity, quantity_angles)
    pressure += loss

    loss = pressure_loss_from_pipe_reduction(diameter,
            velocity, reynolds, HDPE_SDR11_INNER_DIAMETER)
    pressure += loss

    diameter = HDPE_SDR11_INNER_DIAMETER
    friction = HDPE_SDR11_FRICTION_FACTOR
    velocity = HOUSEHOLD_VELOCITY
    loss = pressure_loss_from_pipe(diameter, length2, friction, velocity)
    pressure += loss

    converted = psi_from_kpa(pressure) # converts kpa into psi

    print(f"Pressure at house: {pressure:.1f} kilopascals and {converted:.0f} pounds per square inch.")

    repetition() # repeats main() if the user wants to

if __name__ == "__main__":
    main()