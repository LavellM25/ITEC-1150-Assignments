# Chapter 11 Lab - Web Automation and Basic Web Scraping
# Instructor Walkthrough Comments Included

# First, we import the libraries we need.
# webbrowser allows us to open URLs in the default browser.
# pyperclip lets us access whatever text the user has copied to their clipboard.
# requests allows us to download web content from a URL.
import webbrowser, pyperclip, requests

# -------------------------------
# SECTION 1: Open a Web Page
# -------------------------------
# You can open any webpage using webbrowser.open()
# Let's say we want to visit our school site:

# webbrowser.open('http://minneapolis.edu')  # <-- Uncomment to try

# -------------------------------
# SECTION 2: Use Clipboard to Search Google Maps
# -------------------------------
# Here's a cool trick: You can copy a location name, and this program will open it on Google Maps.

# Step 1: Copy something like "New York, NY" to your clipboard.
# Step 2: Run this code to open that location in Google Maps.

# place = pyperclip.paste()  # Grabs the copied location from your clipboard
# webbrowser.open('https://www.google.com/maps/place/' + place)  # Opens the map in your browser

# -------------------------------
# SECTION 3: Web Scraping a Text File
# -------------------------------
# Now let's download a real book in plain text from the internet.
# We'll use the classic "Alice in Wonderland" hosted by Project Gutenberg.

URL = "https://www.gutenberg.org/files/11/11-0.txt"  # This is the direct link to the .txt file
response = requests.get(URL)  # We send an HTTP GET request to download the file

# Let's create a local file to save the downloaded content
filename = "alice.txt"  # This will be the name of the file on your computer

# We open the file in write mode and specify UTF-8 encoding
# The content we got from the web is in binary form, so we decode it to string before saving
with open(filename, 'w', encoding='utf-8') as file:
    file.write(response.content.decode('utf-8'))  # Save the file as readable text

# At this point, the file 'alice.txt' is saved on your computer!

# -------------------------------
# SECTION 4: Read and Display the File
# -------------------------------
# Let's now open the file we just saved and read its content line by line.
# We'll only show the first 140 lines so we don't overload the console.

readfile = open(filename, 'r', encoding='utf-8')  # Open the file for reading
readfile_line = readfile.readline()  # Read the first line
line_count = 1  # Keep track of how many lines we've printed

# Keep reading lines until we hit 140 lines or the end of the file
while readfile_line and line_count < 140:
    print(readfile_line.strip())  # Strip removes extra newline characters
    readfile_line = readfile.readline()  # Move to the next line
    line_count += 1  # Increment our line counter

readfile.close()  # Always close your files when you're done

# Final message so the user knows we're finished
print("That's all for now! ✅")


"""
Summary of What You Can Do with This Script:
🌐 Open any website in your browser with web browser.

📋 Use your clipboard contents to automatically search Google Maps.

📄 Download a .txt file from the internet using requests.

💾 Save it to your computer with Python file writing.

👀 Read and display the first few lines using a while loop.

"""
