# Renamer Script

A script that can be used to clean up the names of files and folders in a desired directory.  

File and folders will be reformatted to contain all lower case letters, and use dashes in place of spaces.  For example:`"this-is-a-clean-name"`.  There is an option to enumerate file names starting at 00, for example `"00-enumerated-name"`.

## How to use

1) Download and save the script to your computer.

2) Run the script from the command line, passing the directory you want to clean up as a command line argument.  The syntax to do this is `$ python Renamer.py /directory`

3) A prompt will appear that asks you to confirm if the directory name is correct.  Enter `y` to confirm, or `n` to enter a new directory name.

4) A prompt will appear that asks you if you want to confirm each individual rename. If you enter `y`, this means that before the script actually renames a file, it will print out the new and old names of a file or folder, and will ask you to confirm the change before executing it. If you do not want to do this, enter `n`.

5) A prompt will appear that asks you if you want to enumerate new file names. If you enter `y`, the renamed files/folders will be enumerated starting at `00`.

6) The script will execute and clean up your directory based on the prompts selected in steps 3, 4, and 5.

7) A "rename report" is printed, showing you the results of the renaming operations performed.

8) A prompt will appear that asks you if you would like to clean up another directory. If you do, enter `y` and you will be prompted next to enter the directory name. Otherwise, enter any other character and the script will terminate.

## Example

Let's say you have a directory: `/Desktop/files/` that contains the following files:

```
TeST_file.pdf
A FiLE 1 2 3.docx
aN EXCEL fILE.xlsx
```

You can then use the script as follows:

```
$ python renamer.py /Desktop/files/
Confirm directory path is correct (y/n): y
Confirm each individual rename? (y/n): n
Enumerate new file names? (y/n): n
--------------------RENAME REPORT: --------------------
#0: Old Name:/Desktop/files/ TeST_file.pdf
New Name:/Desktop/files/test-file.pdf
#1: Old Name:/Desktop/files/A FiLE 1 2 3.docx
New Name:/Desktop/files/a-file-1-2-3.docx
#2: Old Name:/Desktop/files/aN EXCEL fILE.xlsx
New Name:/Desktop/files/an-excel-file.xlsx
-------------------------------------------------------
Would you like to clean up another directory? (y/n): n
PROGRAM TERMINATED
```

The files in `/Desktop/files/` are now renamed to:

```
test-file.pdf
a-file-1-2-3.docx
an-excel-file.xlsx
```
