# Web Scraping Project - Enhanced Version
# Chapter 11: Automating the Web and Working with BeautifulSoup
# --------------------------------------
# This script grabs a user-defined webpage, optionally shows the raw HTML,
# tries to extract poem content from a div with class 'poem_body',
# saves it to a file, then reopens and displays that content.
# --------------------------------------

from bs4 import BeautifulSoup as soup  # BeautifulSoup is used for parsing HTML
import requests  # Requests is used to download the webpage
import re  # Regular expressions are used for input validation

def main():
    # ------------------------------
    # STEP 1: GET AND VALIDATE URL
    # ------------------------------
    match = False
    while not match:
        str_url = input("Please enter the URL: ")
        pattern = re.compile(r'^(https?|ftp)://[^\s/$.?#].[^\s]*$')  # Basic web address pattern
        match = bool(re.match(pattern, str_url))  # Check if input matches pattern
        if not match:
            print("❌ Invalid URL format. Please try again (example: https://example.com)")

    # ------------------------------
    # STEP 2: GET AND VALIDATE FILENAME
    # ------------------------------
    match = False
    while not match:
        str_filename = input("Please enter the desired filename (e.g. poem.txt): ")
        pattern = re.compile(r'^[\w\-]+\.[\w]+$')  # Allows letters, numbers, underscores, dashes
        match = bool(re.match(pattern, str_filename))
        if not match:
            print("❌ Invalid filename. Avoid spaces or special characters (use only letters, numbers, dashes, underscores).")

    try:
        print("\n🔃 Downloading poem from URL:", str_url)
        print("💾 Saving to:", str_filename)

        # ------------------------------
        # STEP 3: DOWNLOAD AND PARSE PAGE
        # ------------------------------
        imported_webpage = GetWebpage(str_url)

        # ------------------------------
        # STEP 4: ASK TO DISPLAY RAW HTML
        # ------------------------------
        while True:
            str_input = input("\nWould you like to see the unprocessed HTML? (y/n): ")
            if str_input == "y" or str_input == "yes":
                print("\n### Displaying raw html ###\n")
                print(imported_webpage)
                print("\n### End of raw html ###")
                break
            elif str_input == "n" or str_input == "no":
                break
            else:
                print("❌ Invalid input. Please type 'y' or 'n'.")

        # ------------------------------
        # STEP 5: TRY TO EXTRACT THE POEM
        # ------------------------------
        str_poem = ExtractPoem(imported_webpage)  # May fail if structure doesn't match expected
        ExportFile(str_poem, str_filename)

        # ------------------------------
        # STEP 6: READ AND DISPLAY FILE CONTENTS
        # ------------------------------
        print("\n✅ Save complete. Re-importing file...\n")
        str_content = ImportFile(str_filename)
        print("📖 File read into memory. Displaying contents:\n")
        Display(str_content)

    except Exception as err:
        # Catch and display any runtime errors
        print("\n❗ Internal error occurred. Something went wrong:\n")
        print(err)

# ------------------------------
# Function: GetWebpage
# Purpose: Sends a request to download a webpage and parses it with BeautifulSoup
# ------------------------------
def GetWebpage(str_url):
    page_html = requests.get(str_url)  # Fetch the webpage
    page_soup = soup(page_html.text, "html.parser")  # Convert HTML to BeautifulSoup object
    return page_soup

# ------------------------------
# Function: ExtractPoem
# Purpose: Extracts text from the <div class="poem_body"> tag
# NOTE: Will likely fail unless the page has that structure.
# ------------------------------
def ExtractPoem(page_soup):
    # ✅ This works for sites like allpoetry.com that use <div class="poem_body">
    # ⚠️ But for general pages, this will need to be rewritten.
    # 🤔 If you want it to work with arbitrary pages, you'd need a smarter parser or ask the user to help identify elements.

    found = page_soup.find("div", {"class": "poem_body"})  # Searches for specific div
    poem = "\n".join(line.strip() for line in found.p.text.split("\n"))  # Clean and format
    return poem

# ------------------------------
# Function: ExportFile
# Purpose: Save content to a .txt file
# ------------------------------
def ExportFile(str_content, str_filename):
    export_file = open(str_filename, 'w')
    export_file.write(str_content)
    export_file.close()

# ------------------------------
# Function: ImportFile
# Purpose: Read from a saved file
# ------------------------------
def ImportFile(str_filename):
    import_file = open(str_filename, 'r')
    str_content = import_file.read()
    return str_content

# ------------------------------
# Function: Display
# Purpose: Show file content to the user
# ------------------------------
def Display(content):
    print(content)

# ------------------------------
# Run the Program
# ------------------------------
if __name__ == '__main__':
    main()
