# How to run the Windows distribution

- Unzip the downloaded file
- Run iotmonitor.bat
    - at this point your firewall may ask you for confirmation
    - your default browser will open at http://localhost:8000/iotmonitor/. You can also open the same address on other
    browsers if you wish
    
At this point the system will only be accessible at your machine (localhost). If you want other computers to have
access to this system you need to write your machine's IP address in the ip.txt file. This is the case, for instance,
when you want to send data from other devices to your main computer. 

# How to create the Windows distribution (for developers)

This procedure must be performed on Windows.

## Step 1 - install PyInstaller

```
pip install pyinstaller
```

## Step 2 - run PyInstaller
From the root folder of the project, run:
```
pyinstaller --name=iotmonitor iotproject/manage.py
```

This creates the dist/iotmonitor folder with the executable file iotmonitor.exe,
which is equivalent to running python manage.py

## Step 3 - copy files to dist/iotmonitor

3.1 - Copy the app folder (iotproject/iotmonitor) to dist/iotmonitor

3.2 - Copy iotproject/ip.txt to dist/iotmonitor

3.3 - Copy *the contents* of distribution/windows to dist/iotmonitor

## Step 4 - compress

Compress the dist/iotmonitor folder to iotmonitor<version>-win.zip 
