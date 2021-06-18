# Markdown Table of Contents Generator - Description

This is a simple script that allows a user to generate a hyper-link friendly table of contents for a Markdown cell in a Jupyter Notebook.  I create it, as it was always annoying to manually make the table of contents at the end of my projects after I had already nicely formatted all the headers in the Jupyter Notebook.

## How it Works

As input, the script accepts a file that contains all of the Markdown table of contents headers, formatted as they are required to display nicely in a Jupyter notebook.  For example, the three levels of headers are formatted as:

"# Level 1"
"## Level 2"
"### Level 3"

I find it easiest to create this file on the fly as you are creating a Jupyter notebook.  For example, the way that I do it is by creating a .txt or .csv file at the start of my project, and then each time I find myself making a header for a markdown cell, I'll paste the header into that file.  Then at the end of the project, I'll have one file that contains all the headers in Markdown format.

Now - when you want to hyperlink a Markdown header within a Jupyter notebook, it needs to be formatted in a Markdown cell as:

"- [Level 1](# Level 1)"
"   - [Level 2](# Level 2)"
"       - [Level 3](# Level 3)"

The script will create an output file that takes each of the headers from the file previously mentioned, and formats them into the hyperlink friendly format.


## Usage

1) Download the script and save to a folder on your computer that also has the header file in it.

2) Update the input and output file path variables in the script to your desired paths:
```python
# filepath to unformatted toc headers
input_file_path = 'input_path'

# filepath to write formatted toc headers to
output_file_path = 'output_path'
```

3) Run the script at the command line
```bash
python3 TableOfContents.py
```
