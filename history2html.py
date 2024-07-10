#Run this in the location here your CLI history is kept. In Ubuntu this is '~/.bash_history', you will need to research your own Linux history file location.
# > python3 history2html.py


import os

# Path to your .bash_history file
bash_history_path = os.path.expanduser('~/.bash_history')


output_html_path = os.path.expanduser('~/data/history.html')

# Read the .bash_history file
with open(bash_history_path, 'r') as file:
    history_lines = file.readlines()

# Create the HTML structure
html_content = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Bash History</title>
    <style>
        body { font-family: Arial, sans-serif; }
        h1 { text-align: center; }
        ol { max-width: 800px; margin: auto; padding: 0; list-style-position: inside; }
        li { margin: 5px 0; white-space: pre-wrap; word-wrap: break-word; }
    </style>
</head>
<body>
    <h1>Bash History</h1>
    <ol>
'''

# Add each line from the .bash_history as an HTML list item
for line in history_lines:
    html_content += f'        <li>{line.strip()}</li>\n'

# Close the HTML tags
html_content += '''    </ol>
</body>
</html>
'''

# Write the HTML content to the output file
with open(output_html_path, 'w') as file:
    file.write(html_content)

print(f"Bash history has been formatted and saved to {output_html_path}")
