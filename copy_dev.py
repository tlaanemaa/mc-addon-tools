#!/usr/bin/env python

import os
import shutil


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


def copy_top_level_directory(source_dir, target_dir):
    """Copy the top-level directory from source to target, removing the old target directory first."""
    if os.path.exists(target_dir):
        shutil.rmtree(target_dir)
    shutil.copytree(source_dir, target_dir)
    print(f"Coped '{source_dir}' to '{target_dir}' successfully.")


def copy_addon_directories():
    """
    Copy addon directories into Minecraft's development directories.

    This function iterates over the directories in the addon directory and copies them into the corresponding target directories
    within Minecraft's development environment. The target directories are located in the development_behavior_packs
    or development_resource_packs directories, depending on the type of addon, as specified by the directory names.
    """
    # Iterate over the directories in the source directory
    for addon_dir in os.listdir(ADDON_DIRECTORY):
        addon_path = os.path.join(ADDON_DIRECTORY, addon_dir)
        if os.path.isdir(addon_path):
            if "Behavior" in addon_dir:
                copy_top_level_directory(
                    addon_path, os.path.join(BEHAVIOR_PACK_TARGET, addon_dir)
                )
            elif "Resource" in addon_dir:
                copy_top_level_directory(
                    addon_path, os.path.join(RESOURCE_PACK_TARGET, addon_dir)
                )


if __name__ == "__main__":
    copy_addon_directories()
    input("Press Enter to exit...")  # Wait for user input before exiting
