from ast import Store
import math

can1 = ["#1 Picnic", 6.83, 10.16, 0.28]
can2 = ["#1 Tall", 7.78, 11.91, 0.43]
can3 = ["#2", 8.73, 11.59, 0.45]
can4 = ["#2.5", 10.32, 11.91, 0.61]
can5 = ["#3 Cylinder", 10.79, 17.78, 0.86]
can6 = ["#5", 13.02, 14.29, 0.83]
can7 = ["#6Z", 5.40, 8.89, 0.22]
can8 = ["#8Z Short", 6.83, 7.62, 0.26]
can9 = ["#10", 15.72, 17.78, 1.53]
can10 = ["#211", 6.83, 12.38, 0.34]
can11 = ["#300", 7.62, 11.27, 0.38]
can12 = ["#303", 8.10, 11.11, 0.42]

cans = [can1, can2, can3, can4, can5, can6, can7, can8, can9, can10, can11, can12]

def main():
    better_cost_efficiency = 0
    for i in cans:
        name = i[0]
        radius = i[1]
        height = i[2]
        cost = i[3]
        
        volume = compute_volume(radius, height)
        surface_area = compute_surface_area(radius, height)
        storage_efficiency = compute_storage_efficiency(volume, surface_area)
        cost_efficiency = compute_cost_efficiency(volume, cost)
        
        print(f"Name: {name}, Storage Efficiency: {storage_efficiency:.2f}, Surface Area: {surface_area:.2f}, Cost Efficiency: {cost_efficiency:.2f}")
        
        if cost_efficiency > better_cost_efficiency:
            better_cost_efficiency = cost_efficiency      

    print(f"{better_cost_efficiency:.2f}")
    
def compute_volume(radius, height):
    volume = math.pi * radius**2 * height
    return volume

def compute_surface_area(radius, height):
    surface_area = 2 * math.pi * radius * (radius + height)
    return surface_area

def compute_storage_efficiency(volume, surface_area):
    storage_efficiency = volume / surface_area
    return storage_efficiency

def compute_cost_efficiency(volume, cost):
    cost_efficiency = volume / cost
    
    return cost_efficiency

main()