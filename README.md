# InstaFollowBackCheck
Find the Instagram accounts that do not follow you back.

## Dependencies
* Python >= 3.6, recommend 3.8+
* Instagrapi*
* PWInput

## Usage

### Executable (Windows)
Application can be run directly via the executable file under the exe folder. You don't need to install any of the dependencies.

### Source Code
First, install the required modules (check requirements.txt).

#### Installation
Dependencies can be installed via the following command:
```
python -m pip install -r requirements.txt
```

After the installation process, you have to enter your Instagram credentials to get followed accounts and followers.* The results are printed and saved to a file on your desktop.

*NOTE: If you receive an email about a login attempt from an unrecognized device (for example Xiaomi Mi 5s), do not panic. The user agent that Instagrapi provides is different than your device. Also, do not run the script back to back. Instagram may see it as suspicious activity and temporarily lock your account.
