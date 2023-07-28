import argparse
import os
import json
from util import COLORS, GitManager
from shutil import copy

def main():
    parser = argparse.ArgumentParser()

    # Flags
    parser.add_argument("-p", "--sync", help="Gets remote world data and saves locally", action="store_true")
    parser.add_argument("-r", "--reset", help="Resets local cfg and reruns the setup proccess", action="store_true")
    args = parser.parse_args()
    sync = args.sync
    reset = args.reset

    # Open local user data
    try:
        user_data = json.load(open("cfg.json", "r"))
    except Exception as e:
        print(f"{COLORS.warning}`cfg.json` not detected, moving to setup{COLORS.endc}")
        user_data = json.load(open("sample.cfg.json", "r"))
        json.dump(user_data, open("cfg.json", "w"))
        reset = True
    
    # Setup cfg if first time or reseting
    if (not user_data['localUser'] or not user_data['defaultWorld']) or reset:
        setup_cfg(user_data)

    # Get save paths
    user_path = r"C:\Users"
    valheim_saves = r"AppData\LocalLow\IronGate\Valheim\worlds_local"
    world_location = os.path.join(user_path, user_data['localUser'], valheim_saves, user_data['defaultWorld'])
    save_location = os.path.join("./world_data", user_data['defaultWorld'])
    
    world_db = world_location + ".db"
    world_fwl = world_location + ".fwl"
    save_db = save_location + ".db"
    save_fwl = save_location + ".fwl"

    # Save to or sync remote data
    if sync:
        GitManager.pull()
        copy(save_db, world_db)
        copy(save_fwl, world_fwl)
        print(f"{COLORS.ok}World data synced to local from GitHub{COLORS.endc}")
    else:
        copy(world_db, save_db)
        copy(world_fwl, save_fwl)
        GitManager.push()
        print(f"{COLORS.ok}Local World data saved to GitHub{COLORS.endc}")
        

def setup_cfg(user_data):
    """ Sets up the users cfg to memorize user defaults """

    # Set local user
    users = str(os.listdir(r'C:\Users')).replace('[', '').replace(']', '')
    local_user = input(f"Enter your local user from the following: {users}\n")
    while local_user not in users:
        local_user = input(f"`{local_user}` not found. Please enter from the following: {users}\n")

    # Check for valid local setup
    base_path = fr"C:\Users\{local_user}\AppData\LocalLow\IronGate\Valheim"
    if 'worlds_local' not in os.listdir(base_path):
        raise FileNotFoundError(f'Directory `worlds_local` not found. Did you enable local saving inside Valheim?')
    else:
        # Get worlds
        worlds = os.listdir(os.path.join(base_path, 'worlds_local'))
        worlds_set = set()
        for file_name in worlds:
            base_name = file_name.split('.')[0]
            if '_backup_auto' not in base_name:
                worlds_set.add(base_name)
        worlds = str(worlds_set).replace("{", "").replace("}", "")
        
        # Set default world
        default_world = input(f"Enter the default world you want to save: {worlds}\n")
        while default_world not in worlds_set:
            default_world = input(f"`{default_world}` not found. Please enter from the following: {worlds}\n")

    # Save to local cfg
    user_data['localUser'] = local_user
    user_data['defaultWorld'] = default_world
    json.dump(user_data, open("cfg.json", "w"))
    print("Local user information updated in `cfg.json`.")

if __name__ == "__main__":
    main()