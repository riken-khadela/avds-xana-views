import os
import subprocess


'''
This file is used to get the current package of running in avd
like it will print the activity which we can use for start activity or any app in avs
'''



# Function to get the current running application package name
def get_current_package():
    try:
        output = subprocess.check_output(
            "adb shell dumpsys window windows | grep -E 'mCurrentFocus|mFocusedApp'",
            shell=True
        ).decode()
        for line in output.splitlines():
            if 'mCurrentFocus' in line or 'mFocusedApp' in line:
                # Extract the package name
                parts = line.split()
                for part in parts:
                    if '/' in part:
                        package_name = part.split('/')[0]
                        return package_name
    except subprocess.CalledProcessError as e:
        print(f"Error: {e.output}")
    return None

# Get the current running package name
current_package = get_current_package()
print(f"Current running package: {current_package}")

# Define the package name and main activity for Chrome
package_name = "com.android.chrome"
main_activity = "com.google.android.apps.chrome.Main"

# Open Chrome browser
if current_package == package_name:
    print("Chrome is already running.")
else:
    adb_command = f"adb shell am start -n {package_name}/{main_activity}"
    os.system(adb_command)
    print("Chrome browser opened.")
