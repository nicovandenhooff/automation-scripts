#  renamer.py
#  author: Nico Van den Hooff
#  last update: September 11, 2021

import os
import sys


def confirm_directory(directory):
    """Confirms with user that the directory to process is correct

    Parameters
    ----------
    directory : str
        The directory to perform the renames at

    Returns
    -------
    directory : str
        The directory to perform the renames at
    """
    # continue until a valid directory path is entered
    while True:

        # assert directory path is valid
        assert os.path.isdir(directory)

        # prompt to confirm desired directory path entered
        confirmations = input("Confirm directory path is correct (y/n): ")

        # return directory path if confirmed
        if confirmations.lower() == "y":
            return directory

        # get a new directory path if wrong path entered initially
        elif confirmations.lower() == "n":
            directory = input("Enter the directory path: ")

        # otherwise prompt for valid confirmation value
        else:
            confirmations = input(
                "Invalid Entry.\nConfirm directory path is correct (y/n): "
            )


def rename(directory, rename_prompts, enum_names):
    """Renames all the files at a given path.

    Parameters
    ----------
    directory : str
        The directory path to perform the renames at
    rename_prompts : bool
        Whether renames will be confirmed individually
    enum_names : bool
        Whether new names will be enumerated

    Returns
    -------
    rename_report : str
        A report of all renames processed
    """

    old_names = []
    new_names = []

    # loop through all items in directory path
    for index, name in enumerate(sorted(os.listdir(directory))):

        # original name
        src = os.path.join(directory, name)

        # ignore hidden files (mac)
        if name.startswith("."):
            continue
        else:
            # clean spaces and dashes in name
            dst = " ".join(name.replace("-", " ").split()).lower()

            # replace all underscores and spaces with a dash
            dst = dst.replace("_", "-").replace(" ", "-")

            # adds enumeration to name if desired
            if enum_names:
                # format < 10 to be "0#""
                if index in range(10):
                    formatted = "0" + str(index) + "-"
                else:
                    formatted = str(index) + "-"

                dst = formatted + dst

            # final new name
            dst = os.path.join(directory, dst)

        # renames with confirmation
        if rename_prompts:
            rename_with_confirmation(src, dst)

        # renames with no confirmation
        else:
            os.rename(src, dst)

        # for rename report
        old_names.append(src)
        new_names.append(dst)

    return rename_report(old_names, new_names)


def options():
    """Prompts for optional settings when file renaming is performed.

    Returns
    -------
    options: tuple of bool
        (whether to confirm each rename, whether to enum)
    """

    options = []

    # prompt for individual confirmations
    rename_confirm = input("Confirm each individual rename? (y/n): ")

    # try again if incorrect value entered
    while rename_confirm.lower() not in ["y", "n"]:
        rename_confirm = input(
            "Invalid input.\nConfirm each individual rename? (y/n): "
        )

    # prompt for name enumeration
    enum_confirm = input("Enumerate new file names? (y/n): ")

    # try again if incorrect value entered
    while enum_confirm.lower() not in ["y", "n"]:
        enum_confirm = input(("Invalid input.\nEnumerate new file names? (y/n): "))

    # determine desired options based on responses
    for confirm in [rename_confirm, enum_confirm]:
        if confirm.lower() == "y":
            options.append(True)
        else:
            options.append(False)

    return options[0], options[1]


def rename_with_confirmation(src, dst):
    """Renames a given file with individual user confirmation.

    Parameters
    ----------
    src : str
        The old file name
    dst : str
        The new file name
    """
    # confirm rename is correct with user
    confirm = input(
        "CONFIRM RENAME\n"
        + "OLD NAME: "
        + src
        + "\n"
        + "NEW NAME: "
        + dst
        + "\n"
        + "Confirmation (Y/N): "
    )

    # perform rename if confirmed
    if confirm.lower() == "y":
        os.rename(src, dst)
        print("*RENAME SUCCESSFUL*\n")
    # cancel rename if confirmation denied
    else:
        print("*RENAME CANCELLED*\n")


def rename_report(old_names, new_names):
    """Generates a report showing old names vs. new ones.

    Parameters
    ----------
    old_names : list of str
        A list of old names
    new_names : list of str
        A list of new names

    Returns
    -------
    report : str
        A report showing the rename results.
    """
    report = ["\n--------------------RENAME REPORT: --------------------\n"]

    # append each rename to report
    for index, (old, new) in enumerate(zip(old_names, new_names)):
        report.append("#" + str(index) + ": ")
        report.append("Old Name:" + old + "\n")
        report.append("    New Name:" + new + "\n")

    report.append("-------------------------------------------------------\n")

    report = "".join(report)

    return report


# -------END OF FUNCTIONS

# flag to determine if script should continually run
processing = True

# first directory to perform rename at
directory = confirm_directory(sys.argv[1])

# continue processing until user prompts not to
while processing:
    # prompt user for optional settings
    rename_prompts, enum_files = options()

    # perform all renames and print rename report
    print(rename(directory, rename_prompts, enum_files))

    # ask user if they want to clean another directory
    processing = input("Would you like to clean up another directory? (y/n): ")

    # ask user if they want to process another directory
    if processing.lower() == "y":
        # ask user for next directory to process
        next_dir = input("Please enter the directory: ")
        directory = confirm_directory(next_dir)
    else:
        # otherwise program terminates
        processing = False
        print("PROGRAM TERMINATED")
