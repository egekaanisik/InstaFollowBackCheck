import pkg_resources
import subprocess
import time
import sys

# Required dependicies list
dependencies = sys.argv[1:]

# Gets installed modules
packages = pkg_resources.working_set
package_list = sorted([i.key for i in packages])

# Adds missing dependencies to a list
not_installed = []

for i in dependencies:
   if i.casefold() not in package_list:
      not_installed.append(i)

# If there are some missing modules, prompt user
if len(not_installed) != 0:
   print("There are some modules that are required to run this program.\n\nThese modules are not installed on your computer:")
   for i in not_installed:
      print("[*] " + i)
    
   # Keeps asking until there is a valid answer
   while True:
      yes_no = input("\nDo you want to install them? (y/n): ")

      if yes_no.casefold() == "yes" or yes_no.casefold() == 'y':
         # Installs every module one-by-one by calling a "pip install" command
         for i in not_installed:
            print("\n____________________________________________________________________________________________________\n\nInstalling " + i + "...\n____________________________________________________________________________________________________\n")
            subprocess.check_call([sys.executable, "-m", "pip", "install", i])
         print("\n____________________________________________________________________________________________________\n\nDone installing the modules. Launching the program...\n____________________________________________________________________________________________________\n")
         time.sleep(1)
         break
      elif yes_no.casefold() == "no" or yes_no.casefold() == 'n':
         exit(1)
      else:
         print("Please enter a valid answer.")
else:
    print("Launching the program...")
    time.sleep(1)