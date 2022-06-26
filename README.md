# InstaFollowBackCheck
Find the Instagram accounts that do not follow you back.

## Dependencies
* Python >= 3.6, recommend 3.8+
* Instagrapi
* PWInput

## Usage

### Executable
Executables can be found under the "executables" folder. If you use executables, you don't have to install any dependencies.

#### Windows
Application can be run directly via double-clicking.

#### macOS
Like Windows, you can run the application by double-clicking.

#### Linux
To run the application, open folder in terminal and run the following command:
```
./InstaFollowBackCheck
```

### Source Code
First, install the required modules (check requirements.txt).

#### Installation
Dependencies can be installed via the following command:
```
pip install -r requirements.txt
```

After the installation process, you have to enter your Instagram credentials to get followed accounts and followers.* The results are printed and saved to a file on your desktop.

*NOTE: If you receive an email about a login attempt from an unrecognized device (for example Xiaomi Mi 5s), do not panic. The user agent that Instagrapi provides is different than your device. Also, do not run the script back to back. Instagram may see it as suspicious activity and temporarily lock your account.
