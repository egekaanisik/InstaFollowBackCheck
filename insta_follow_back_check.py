import os
import sys
from instagrapi import Client
from pwinput import pwinput
from tempfile import gettempdir

# Get user information
username = input("Username: ").strip()
password = pwinput()
oauth = input("2FA Code (if not exists, leave blank): ").strip()
print()

# Account settings dump path
DUMP = os.path.join(gettempdir(), "{}_account_dump.json".format(username))

# Try to login and get account details, if fails, terminate
try:
    # Create the client
    cl = Client()

    # If there is a dump for the account, load settings
    if os.path.exists(DUMP):
        cl.load_settings(DUMP)
        print("Loaded account settings from dump.")

    # Login
    cl.login(username, password, verification_code=oauth)

    # If there is not a dump for the account, dump settings
    if not os.path.exists(DUMP):
        cl.dump_settings(DUMP)
        print("Dumped account settings to temp directory.")
    
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
    # Print the exception message
    print("An exception occured: {}".format(str(e)))

    # Delete account dump to prevent login issues
    if os.path.exists(DUMP):
        os.remove(DUMP)
        print("Account dump is deleted to prevent login issues.")

    # Terminate
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
path = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop', "{}_accounts_dont_follow_back.html".format(username))

# Fill an HTML body with the not following users and their Instagram profile links
html = ""
for i in not_following:
    html += '<a href="https://instagram.com/{}">{}</a><br>'.format(i, i)

# Open the file and write the results into it
with open(path, "w") as file:
    file.write(html)

# Print the path and terminate
print("\nResults are saved to {}.".format(path))
input("Press Enter to terminate.")