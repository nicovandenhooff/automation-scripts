# TableOfContents.py
# @Author: Nico Van den Hooff
# @Date: June 17, 2021
# @Last modified: June 17, 2021
# Note: In this script, "toc" means table of contents

# filepath to unformatted toc headers
input_file_path = 'input_path'

# filepath to write formatted toc headers to
output_file_path = 'output_path'

# to store the formatted table of contents
toc = []

# hashes for each of the three potential toc levels
level_3 = "### "
level_2 = "## "
level_1 = "# "

# spacing that needs to be added for each toc level for hyperlink to work
level_3_space = "       "
level_2_space = "   "


def remove_hashes(header):
    """Removes the hashes (#) and leading space in an unformatted toc header.

    Parameters
    ----------
    header: String
        The toc header to formatted (e.g. "### Level 3").

    Returns:
    --------
    header: String
        The toc header with hashes and leading space removed (e.g "Level 3")
    """
    if level_3 in header:
        return header.replace(level_3, "")
    elif level_2 in header:
        return header.replace(level_2, "")
    else:
        return header.replace(level_1, "")


def create_toc_header(header):
    """Fully formats a markdown cell toc header into hyperlink friendly form
    for a Jupyter notebook.

    As input, it takes in the raw format of the header that a Jupyter markdown
    cell accepts as input.  For example, a level 1 toc header in a markdown
    cell is written as "# Level 1".

    Parameters
    ----------
    header: String
        The toc header to be formatted (e.g. "# Level 1")

    Returns
    -------
    toc_header: String
        The hyperlink formatted toc header (e.g. "- [Level 1](#Level-1)")
    """

    # first, updates spacing in the header by calling support function
    updated_header = remove_hashes(header)

    # create part 1 and 2 of the hyperlink header
    # "part 1" is the former part of the hyperlink header in square brackets []
    # "part 2" is the latter part of the hyperlink header in round brackets ()
    part_1 = updated_header.replace("\n", "")
    part_2 = part_1.replace(" ", "-")

    # adds the required tab spacing to the formatted toc_header
    if level_3 in header:
        toc_header = level_3_space + "- ["
    elif level_2 in header:
        toc_header = level_2_space + "- ["
    else:
        toc_header = "- ["

    # forms the rest of the hyperlink friendly toc_header
    toc_header += part_1
    toc_header += "]"
    toc_header += "(#"
    toc_header += part_2
    toc_header += ")\n"

    return toc_header


# reads in the file that contains the unformatted toc headers
with open(input_file_path, 'r') as input_file:
    for line in input_file:
        toc.append(create_toc_header(line))


# writes to a new file the formatted hyperlink friendly toc headers
with open(output_file_path, 'w') as output_file:
    for header in toc:
        output_file.write(header)
