import math

def get_degree(x, y):
        # Calculate the angle in radians
        angle_rad = math.atan2(y, x)
        
        # Convert radians to degrees
        angle_deg = math.degrees(angle_rad)
        
        # Ensure the degree is positive
        if angle_deg < 0:
            angle_deg += 360
        
        return (angle_deg)

print(get_degree(-500, -70))