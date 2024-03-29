#!/usr/bin/env python

import os


# Constants
USERNAME = "replace-with-your-username"  # Change this to your username
SCRIPT_DIRECTORY = os.path.dirname(__file__)
ADDON_DIRECTORY = os.path.join(SCRIPT_DIRECTORY, "addon")
BEHAVIOR_PACK_TARGET = os.path.expandvars(
    rf"C:\Users\{USERNAME}\AppData\Local\Packages\Microsoft.MinecraftUWP_8wekyb3d8bbwe\LocalState\games\com.mojang\development_behavior_packs"
)
RESOURCE_PACK_TARGET = os.path.expandvars(
    rf"C:\Users\{USERNAME}\AppData\Local\Packages\Microsoft.MinecraftUWP_8wekyb3d8bbwe\LocalState\games\com.mojang\development_resource_packs"
)


def create_symlink(source_dir, target_dir):
    try:
        # Create the symbolic link
        os.symlink(source_dir, target_dir)
        print(f"Created symbolic link: {target_dir}")
    except OSError as e:
        print(f"Failed to create symbolic link for {source_dir}: {e}")


def create_symlinks():
    """
    Create symbolic links for addon packs.
    This function iterates over the directories in the addon directory and creates symbolic links for
    behavior packs and resource packs to the corresponding target directories.
    """

    # Iterate over the directories in the source directory
    for addon_dir in os.listdir(ADDON_DIRECTORY):
        addon_path = os.path.join(ADDON_DIRECTORY, addon_dir)
        if os.path.isdir(addon_path):
            if "Behavior" in addon_dir:
                create_symlink(
                    addon_path, os.path.join(BEHAVIOR_PACK_TARGET, addon_dir)
                )
            elif "Resource" in addon_dir:
                create_symlink(
                    addon_path, os.path.join(RESOURCE_PACK_TARGET, addon_dir)
                )


if __name__ == "__main__":
    create_symlinks()
    input("Press Enter to exit...")  # Wait for user input before exiting
