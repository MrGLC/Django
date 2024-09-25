import tkinter as tk
from tkinter import font as tkfont
import re
import os

class MarkdownInterpreter:
    def __init__(self, master):
        # Create a new font for normal text
        self.text_font = tkfont.Font(family='Helvetica', size=12)

        # Create the text widget
        self.text_widget = tk.Text(master, font=self.text_font, width=40, height=20)
        self.text_widget.pack()

        # Load the markdown file
        with open(os.path.join(os.path.dirname(__file__), 'example.md'), 'r') as f:
            self.markdown_text = f.read()

        # Parse the markdown text
        self.parse_markdown()

    def parse_markdown(self):
        # Regular expressions for markdown syntax
        header_regex = re.compile(r'(#+)(.*)')
        italic_regex = re.compile(r'((\*|_)(.*?)\2)')
        bold_regex = re.compile(r'((\*\*|__)(.*?)\2)')
        list_regex = re.compile(r'([\s]*(\d+\.|[-*])[ \t]+)(.*)')

        # Split the text into lines
        lines = self.markdown_text.splitlines()

        # Parse each line
        for line in lines:
            # Check for headers
            match = header_regex.match(line)
            if match:
                self.parse_header(match)
                continue

            # Check for italic text
            match = italic_regex.search(line)
            if match:
                self.parse_italic(match)
                continue

            # Check for bold text
            match = bold_regex.search(line)
            if match:
                self.parse_bold(match)
                continue

            # Check for lists
            match = list_regex.match(line)
            if match:
                self.parse_list(match)
                continue

            # If no markdown syntax is found, just display the text
            self.text_widget.insert('end', line + '\n', 'normal')

    def parse_header(self, match):
        # Get the header level and text
        level = len(match.group(1))
        text = match.group(2).strip()

        # Create a new font for the header
        font = self.text_font
        if level > 1:
            font = tkfont.Font(family='Helvetica', size=self.text_font['size'] - 2 * (level - 1), weight='bold')

        # Create a new tag for the header
        tag = 'header' + str(level)

        # Configure the tag with the new font
        self.text_widget.tag_config(tag, font=font)

        # Insert the header text with the tag
        self.text_widget.insert('end', text + '\n', tag)

    def parse_italic(self, match):
        # Get the italic text
        text = match.group(3).strip()

        # Replace the italic text with the italic font
        replaced_text = re.sub(match.group(1), r'\1' + self.text_widget.tag_cget('italic', 'font'), text, flags=re.IGNORECASE)

        # Insert the italic text
        self.text_widget.insert('end', replaced_text + '\n', 'italic')

    def parse_bold(self, match):
        # Get the bold text
        text = match.group(3).strip()

        # Insert the bold text with the bold font
        self.text_widget.insert('end', re.sub(match.group(1), '', text, count=1), 'bold')

    def parse_list(self, match):
        # Get the list text
        text = match.group(3).strip()

        # Check if it's a numbered list
        if match.group(2).startswith('\\d+'):
            # Configure the 'list' tag with a bullet
            self.text_widget.tag_config('list', font=self.text_font, lmargin1=10, lmargin2=10)

            # Insert the list text with a bullet
            self.text_widget.insert('end', ' • ' + text + '\n', 'list')
        else:
            # Configure the 'list' tag with a bullet
            self.text_widget.tag_config('list', font=self.text_font, lmargin1=10, lmargin2=10)

            # Insert the list text with a bullet
            self.text_widget.insert('end', ' • ' + text + '\n', 'list')

# Create the Tkinter window
root = tk.Tk()

# Create the markdown interpreter
interpreter = MarkdownInterpreter(root)

# Run the Tkinter mainloop
root.mainloop()
