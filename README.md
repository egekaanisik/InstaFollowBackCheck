# InstaFollowBackCheck
Find the Instagram accounts that do not follow you back.

## Dependencies
* Python >= 3.7, recommend 3.8+
* Instagrapi
* PWInput
* Pillow

## Usage
First, install the required modules (check requirements.txt).

#### Installation
Dependencies can be installed via the following command:
```
pip install -r requirements.txt
```

After the installation process, you have to run the script enter your Instagram credentials to get followed accounts and followers.* The results are printed and saved to a file on your desktop.

*NOTE: If you receive an email about a login attempt from an unrecognized device (for example Xiaomi Mi 5s), do not panic. The user agent that Instagrapi provides is different than your device. Also, do not run the script back to back. Instagram may see it as suspicious activity and temporarily lock your account. In some cases, Instagram gives a warning about a suspicious login on the app and blocks the script access. If this is the case, after running the script, immediately press "This was me".

PS. To login, either Two-Factor-Authentication via auth app has to be enabled or 2FA has to be disabled.

