# Valheim World Sync
A Valheim world saving system. This implementation relies on GitHub for remote storage. This will also work with other Git providers.

## Table of Contents
- [Requirements](#requirements)
- [Setup (for original World Owner)](#setup-for-original-world-owner)
- [Usage (for syncing)](#usage-for-syncing)
- [Troubleshooting](#troubleshooting)
	- [Troubleshooting Setup](#troubleshooting-setup)
	- [Troubleshooting Syncing](#troubleshooting-syncing)

## Requirements
- [Git](https://git-scm.com/)
- [Python 3](https://www.python.org/downloads/)
- Windows OS

## Setup (for original World Owner)
1. Launch Valheim.
2. Change your specific world save to local.<br>**Start Game -> Manage Saves -> Worlds -> Select world to save -> Move to Local**
![valheim save image](https://cdn.discordapp.com/attachments/942218891952783421/1134529016817266800/image.png)
4. (Fork and) Clone the repository.
5. Run the `save.py` script (`python3 save.py`).
6. Follow the setup process.
```bash
$ python3 save.py
`cfg.json` not detected, moving to setup
Enter your local user from the following: 'All Users', 'Default', 'Default User', 'desktop.ini', 'jonat', 'Public'
jonat
Enter the default world you want to save: 'bigdawg69', 'worlds_urmomshouse'
worlds_urmomshouse
Local user information updated in `cfg.json`.
On branch main
Your branch is up to date with 'origin/main'.

nothing to commit, working tree clean
Everything up-to-date
Local World data saved to GitHub
```

## Usage (for syncing)
1. Ensure there is a `.db` and a `.fwl` file  [`world_data`](./world_data)
2. Ensure that you have push access to the repository.
3. Clone the repository.
4. Run the `save.py` script with the `--sync` flag (`python3 -s`).
5. Follow the setup process.
```bash
$ python save.py --sync #or -s
`cfg.json` not detected, moving to setup
Setting up for World Syncing User
Enter your local user from the following: 'All Users', 'Default', 'Default User', 'desktop.ini', 'jonat', 'Public'
jonat
Local user information updated in `cfg.json`.
Already up to date.
World data synced to local from GitHub
```

## Troubleshooting
### Troubleshooting Setup 
- **For Original World Owner**: Reset your `cfg.json` file and delete the `world_data/` directory and attempt to rerun through the setup process again
```bash
$ python save.py -r #or --reset
Setting up for Orginal World Owner
Enter your local user from the following: 'All Users', 'Default', 'Default User', 'desktop.ini', 'jonat', 'Public'
jonat
Enter the default world you want to save: 'worlds_urmomshouse', 'bigdawg69'
worlds_urmomshouse
Local user information updated in `cfg.json`.
[main ec2f0cc] World save: 2023-07-28 10:47:33.090716
 2 files changed, 0 insertions(+), 0 deletions(-)
 delete mode 100644 world_data/bigdawg69.db
 delete mode 100644 world_data/bigdawg69.fwl
Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
Delta compression using up to 24 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 352 bytes | 352.00 KiB/s, done.
Total 3 (delta 1), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (1/1), completed with 1 local object.
To https://github.com/jonathanlo411/valheim-server.git
   d666d48..ec2f0cc  main -> main
Local World data saved to GitHub
```
- **For Syncing User**: Reset your `cfg.json` file only and attempt the setup process again. Ensure the following:
	- You *actually* have push access to the repository.
	- There is only one `.db` and one `.fwl` file in `world_data/`
```bash
$ python save.py -r -s #or --reset --sync
Setting up for World Syncing User
Enter your local user from the following: 'All Users', 'Default', 'Default User', 'desktop.ini', 'jonat', 'Public'
jonat
Local user information updated in `cfg.json`.
Already up to date.
World data synced to local from GitHub
```
### Troubleshooting Syncing
- **Merge Conflict**: If a merge conflict occurs with one of the `world_data` files, you will need make a choice between the world save data on GitHub vs Local.
	- **Prioritizing GitHub**:  Delete the `world_data/` directory. Follow the [setup for syncing](#usage-for-syncing).
	- **Prioritizing Local**:  Go to your repository on GitHub and delete the `world_data/` directory. Follow the [setup for world owner](#setup-for-original-world-owner).
- **Corrupted World Data**: If your world data gets corrupted, navigate to the following file path and find backups of your world data.
```
C:\Users\{YOUR_USER}\AppData\LocalLow\IronGate\Valheim\worlds_local
```