#!/usr/bin/env python

import os
import shutil


# Constants
SCRIPT_DIRECTORY = os.path.dirname(__file__)
ADDON_DIRECTORY = os.path.join(SCRIPT_DIRECTORY, "addon")


def pack_addon():
    """
    This script creates a Minecraft addon (.mcaddon) file by zipping the contents of
    the 'addon' directory located in the same directory as this script. The name of
    the addon will be based on the name of the directory where this script is
    located.

    Expectations before running this script:
    1. Ensure there is a directory named 'addon' in the same directory as this script.
    2. The name of the addon will be taken from the directory where this script resides.

    After running the script, the addon will be packed successfully, and the resulting
    .mcaddon file will be placed in the same directory as this script.
    """

    # Define the name for the addon
    addon_name = os.path.basename(SCRIPT_DIRECTORY)

    # Check if the "addon" directory exists
    if not os.path.exists(ADDON_DIRECTORY) or not os.path.isdir(ADDON_DIRECTORY):
        raise FileNotFoundError(
            "The 'addon' directory does not exist or is not a directory."
        )

    # Define the filename for the addon
    addon_filename = os.path.join(SCRIPT_DIRECTORY, addon_name + ".mcaddon")

    # Check if the addon file already exists, and remove it if it does
    if os.path.exists(addon_filename):
        os.remove(addon_filename)

    # Create the .mcaddon file by zipping the contents of the "addon" directory
    zip_filename = os.path.join(SCRIPT_DIRECTORY, addon_name)
    shutil.make_archive(zip_filename, "zip", ADDON_DIRECTORY)

    # Rename the zip file to have a .mcaddon extension
    os.rename(zip_filename + ".zip", addon_filename)

    print(f"Addon packed successfully as '{addon_filename}'.")


if __name__ == "__main__":
    try:
        pack_addon()
    except Exception as e:
        print(f"An error occurred: {e}")
    input("\nPress Enter to exit...")  # Wait for user input before exiting
