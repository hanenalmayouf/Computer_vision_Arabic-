import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as patches

def draw_base_car(ax):
    # Initialize white background
    image = np.ones((16, 16, 3))
    
    # Red Car Body (R=1, G=0, B=0)
    image[6:10, 4:12] = [1.0, 0.2, 0.2]  
    image[4:6, 6:10] = [1.0, 0.2, 0.2]   
    
    # Light Blue Glass (R=0.5, G=0.8, B=1.0)
    image[4:6, 7:9] = [0.6, 0.8, 1.0]
    
    # Dark Gray Wheels
    image[9:11, 5:7] = [0.2, 0.2, 0.2]
    image[9:11, 9:11] = [0.2, 0.2, 0.2]
    
    # Display as an image
    ax.imshow(image)
    
    # Add gridlines to show the 16x16 pixels
    ax.set_xticks(np.arange(-0.5, 16, 1), minor=True)
    ax.set_yticks(np.arange(-0.5, 16, 1), minor=True)
    ax.grid(which='minor', color='gray', linestyle='-', linewidth=0.5, alpha=0.5)
    ax.tick_params(which='minor', bottom=False, left=False)
    ax.set_xticks([])
    ax.set_yticks([])
    
    # Remove axes borders for a cleaner look
    for spine in ax.spines.values():
        spine.set_visible(False)

def draw_base_human(ax):
    # Initialize white background
    image = np.ones((16, 16, 3))
    
    # Head (Skin color: #f1c27d -> R=0.94, G=0.76, B=0.49)
    image[2:5, 7:10] = [0.94, 0.76, 0.49]
    # Body (Blue shirt: #3498db -> R=0.2, G=0.6, B=0.86)
    image[5:10, 6:11] = [0.2, 0.6, 0.86]
    # Arms (Skin color)
    image[5:9, 4:6] = [0.94, 0.76, 0.49]
    image[5:9, 11:13] = [0.94, 0.76, 0.49]
    # Legs (Dark pants: #2c3e50 -> R=0.17, G=0.24, B=0.31)
    image[10:15, 6:8] = [0.17, 0.24, 0.31]
    image[10:15, 9:11] = [0.17, 0.24, 0.31]
    
    # Display as an image
    ax.imshow(image)
    
    # Add gridlines to show the 16x16 pixels
    ax.set_xticks(np.arange(-0.5, 16, 1), minor=True)
    ax.set_yticks(np.arange(-0.5, 16, 1), minor=True)
    ax.grid(which='minor', color='gray', linestyle='-', linewidth=0.5, alpha=0.5)
    ax.tick_params(which='minor', bottom=False, left=False)
    ax.set_xticks([])
    ax.set_yticks([])
    
    # Remove axes borders for a cleaner look
    for spine in ax.spines.values():
        spine.set_visible(False)
