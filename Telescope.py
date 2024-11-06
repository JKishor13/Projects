import tkinter as tk
from PIL import Image, ImageTk
import plotly.graph_objs as go
from plotly.offline import plot

# Placeholder dictionary with planet data and sample images
PLANET_DATA = {
    "Mercury": {"color": "gray", "distance": 50, "image": "path_to_mercury_image.jpg", "details": "Smallest planet, closest to the Sun."},
    "Venus": {"color": "yellow", "distance": 90, "image": "path_to_venus_image.jpg", "details": "Second planet from the Sun, similar size to Earth."},
    "Earth": {"color": "blue", "distance": 130, "image": r"C:\Users\Kishor Jeganathan\Desktop\J Kishor\General\C.S Kaledioscope Telescope\Planet Images\Earth.png", "details": "Our home planet, third from the Sun."},
    "Mars": {"color": "red", "distance": 170, "image": "path_to_mars_image.jpg", "details": "Known as the Red Planet."},
    "Jupiter": {"color": "orange", "distance": 220, "image": "path_to_jupiter_image.jpg", "details": "Largest planet in the Solar System."},
    "Saturn": {"color": "gold", "distance": 270, "image": "path_to_saturn_image.jpg", "details": "Famous for its rings."},
    "Uranus": {"color": "light blue", "distance": 320, "image": "path_to_uranus_image.jpg", "details": "Has a unique tilt."},
    "Neptune": {"color": "dark blue", "distance": 370, "image": "path_to_neptune_image.jpg", "details": "Known for its deep blue color."}
}

# Function to create a 360-degree view using Plotly
def create_360_view(planet_name):
    fig = go.Figure(data=[go.Surface(z=[[1]], colorscale=[[0, 'rgb(50,50,200)'], [1, 'rgb(0,0,150)']])])
    fig.update_layout(title=f"{planet_name} 360° View", autosize=True, margin=dict(l=65, r=50, b=65, t=90))
    plot(fig, filename=f"{planet_name}_360.html")

# Function to display planet details
def show_planet_details(planet_name):
    planet_info = PLANET_DATA.get(planet_name, {})
    detail_window = tk.Toplevel()
    detail_window.title(planet_name)
    
    # Display planet image
    img = Image.open(planet_info["image"])
    img = img.resize((570, 400))  # Resize for display
    img_tk = ImageTk.PhotoImage(img)
    
    img_label = tk.Label(detail_window, image=img_tk)
    img_label.image = img_tk  # Keep reference
    img_label.pack()
    
    # Display details
    detail_label = tk.Label(detail_window, text=planet_info["details"], wraplength=300)
    detail_label.pack()


# Main application window
def main():
    root = tk.Tk()
    root.title("Solar System Viewer")
    root.geometry("800x800")
    
    # Create a Canvas to draw the solar system
    canvas = tk.Canvas(root, width=1920, height=1080, bg="black")
    canvas.pack()

    # Draw the Sun at the center
    canvas.create_oval(390, 390, 410, 410, fill="yellow", outline="yellow", tags="Sun")
    
    # Create each planet as a circle on the canvas
    for planet, data in PLANET_DATA.items():
        x0 = 400 + data["distance"]
        y0 = 400
        radius = 10  # A basic size for planets
        canvas.create_oval(x0-radius, y0-radius, x0+radius, y0+radius, fill=data["color"], outline=data["color"], tags=planet)
        
        # Bind click event to each planet
        canvas.tag_bind(planet, "<Button-1>", lambda event, p=planet: show_planet_details(p))
    
    root.mainloop()

if __name__ == "__main__":
    main()
