# Image Annotation Project using Pillow (PIL)
# ---------------------------------------------
# By the end of this program, you'll resize a large image, draw a rectangle around a feature,
# add a descriptive label, and save the edited image with new visuals.

from PIL import Image, ImageDraw, ImageFont  # Import modules to work with images and draw on them

# ------------------------------
# STEP 1: Load the High-Resolution Image
# ------------------------------
bee_photo = Image.open('vengadesh-sago-QR1O0HRaax4-unsplash.jpg')  # Load the original image

# ------------------------------
# STEP 2: Resize the Image
# ------------------------------
# Get the original image size
original_width = 3735
original_height = 5603

# We want the image height to be around 800 pixels
target_height = 800
resize_ratio = target_height / original_height  # Calculate the scaling factor

# Calculate the new width to maintain aspect ratio
target_width = int(original_width * resize_ratio)

# Resize the image
bee_photo_resized = bee_photo.resize((target_width, target_height))

# Save resized image (optional step if you want to store it separately)
bee_photo_resized.save('resized_bee_image.jpg')

# ------------------------------
# STEP 3: Draw a Rectangle Around a Feature
# ------------------------------
# Create a drawing context to draw shapes and text on the image
img_draw = ImageDraw.Draw(bee_photo_resized)

# Coordinates for rectangle: [left, top, right, bottom]
# You should adjust these numbers based on what you want to highlight
rectangle_coords = [144, 357, 387, 590]  # These numbers are in pixels on the resized image
rectangle_color = 'FloralWhite'  # Choose any valid color name or RGB tuple
img_draw.rectangle(rectangle_coords, outline=rectangle_color, width=5)

# ------------------------------
# STEP 4: Add a Text Label
# ------------------------------
# Load a font; make sure the TTF file is in the same directory or provide full path
font = ImageFont.truetype('DejaVuSans.ttf', 22)  # You can adjust size

# Choose the position of the text and its color
text_position = [170, 600]  # Place this just below the rectangle
text_color = 'gold'  # Pick a contrasting color
text_message = "Spring will come!"  # Customize the label as you like

# Draw the text
img_draw.text(text_position, text_message, fill=text_color, font=font, stroke_width=1)

# ------------------------------
# STEP 5: Display and Save the Final Image
# ------------------------------
bee_photo_resized.show()  # This opens the image in your default image viewer

# Save the final annotated image to a new file so you don’t overwrite the original
bee_photo_resized.save('bee_annotated_output.jpg')

# ✅ Done! You’ve now resized, highlighted, labeled, and saved the image.
