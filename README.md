# SignalFridaIntercept
using frida, can intercept messages on the host's android phone (Must be Root)

# Usage
Start the server:
```
python Server/server.py
```
Connect your phone to the computer and enable USB debugging. Then start the Frida server on the phone with adb shell:
```
<Path To Frida Server>/Frida-server-<Frida server version>-<Frida android version>
```
For example my Frida server is in /data/local/tmp so:
```
data/local/tmp/Frida-server-16.0.1-android-x86_64
```
Then start the hook.py:
```
python Client/hook.py
```
Now you every message you receive will be logged to the server and saved to the database.
