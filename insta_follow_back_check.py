import os
import sys
import platform

# Dependency list
DEPENDENCIES = ["Instagrapi", "PWInput"]

# Dependency installer contraints
INSTALLER_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "modules", "install_dependencies.py")
INSTALLER = '"' + INSTALLER_DIR + '" ' + " ".join(DEPENDENCIES)

# Start the installer, if fails, terminate
if os.system(INSTALLER):
    print("Required modules are not installed.")
    input("Press Enter to terminate.")
    sys.exit(1)

# Clear the terminal
os.system('cls' if platform.system() == "Windows" else 'clear')

from instagrapi import Client
from pwinput import pwinput

# Get user information
username = input("Username: ").strip()
password = pwinput()
oauth = input("2FA Code (if not exists, leave blank): ").strip()
print()

# Try to login and get account details, if fails, terminate
try:
    # Create the client and login
    cl = Client()
    cl.login(username, password, verification_code=oauth)

    # Get the user ID
    user_id = cl.user_id
    print("Your User ID: {}".format(user_id))

    # Get followed accounts
    print("Getting accounts that you follow...")
    followings = cl.user_following(user_id)
    print("Got {} followed accounts.".format(len(followings)))

    # Get followers
    print("Getting accounts that follow you...")
    followers = cl.user_followers(user_id)
    print("Got {} followers.".format(len(followers)))
except Exception as e:
    print(str(e))
    input("Press Enter to terminate.")
    sys.exit(1)

# Extract only the usernames on both followed accounts and followers
followings_usernames = [i.username for i in followings.values()]
followers_usernames = [i.username for i in followers.values()]

# Compare followed accounts to followers to distinguish the accounts that do not follow back
print("Finding accounts you follow but do not follow you...")
not_following = []
for i in followings_usernames:
    if i not in followers_usernames:
        not_following.append(i)
print("Found {} accounts.".format(len(not_following)))

# Print the results
print("\nAccounts that do not follow you back:")
print("\n".join(not_following))

# Get the path for results
if platform.system() == "Windows":
    path = os.path.join(os.environ["HOMEPATH"], "Desktop", "accounts_dont_follow_back.txt")
else:
    path = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop', "accounts_dont_follow_back.txt")

# Open the file and write the results into it
with open(path, "w") as file:
    file.write("\n".join(not_following))

# Print the path and terminate
print("\nResults are saved to {}.".format(path))
input("Press Enter to terminate.")