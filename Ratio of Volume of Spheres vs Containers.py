#Ratio of Volume of Spheres vs Containers
#Description 
#This Program uses user input to demonstrate that the volume of any sphere is 2/3 of the volume of any cylinder with equivalent radius and height equal to its diameter. 




spheres = float(input("Enter the number of spheres to be placed in the container: "))

#By using input function the program takes user input for the number of spheres

diameter = float(input("Enter the diameter of each sphere(in inches): "))

#By using input function the program takes user input for the diameter

PI = 3.14159
radius = diameter / 2
height = diameter * spheres
volume_sphere = (4/3) * PI * radius**3 * spheres
volume_container = PI * radius**2 * height
percentage = volume_sphere / volume_container * 100
print("The container would need to be at least", height, "inches to hold", spheres, "spheres")
print("The", spheres, "spheres will occupy",percentage, "of the container")
