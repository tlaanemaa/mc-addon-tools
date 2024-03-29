#!/usr/bin/env python

import os
import shutil


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

    # Get the directory where the script resides
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Define the name for the addon
    addon_name = os.path.basename(script_dir)

    # Define the path to the addon directory
    addon_dir = os.path.join(script_dir, "addon")

    # Check if the "addon" directory exists
    if not os.path.exists(addon_dir) or not os.path.isdir(addon_dir):
        raise FileNotFoundError(
            "The 'addon' directory does not exist or is not a directory."
        )

    # Define the filename for the addon
    addon_filename = os.path.join(script_dir, addon_name + ".mcaddon")

    # Create the .mcaddon file by zipping the contents of the "addon" directory
    zip_filename = os.path.join(script_dir, addon_name)
    shutil.make_archive(zip_filename, "zip", addon_dir)

    # Rename the zip file to have a .mcaddon extension
    os.rename(zip_filename + ".zip", addon_filename)

    print(f"Addon packed successfully as '{addon_filename}'.")


if __name__ == "__main__":
    try:
        pack_addon()
    except Exception as e:
        print(f"An error occurred: {e}")
    input("\nPress Enter to exit...")  # Wait for user input before exiting
