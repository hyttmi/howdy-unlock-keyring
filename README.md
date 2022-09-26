# Unlocking Gnome keyring when logging in without password or with Howdy

When logging in with password or with Howdy using ir-camera, your default login keyring will stay locked until you input your password after you launch an application which needs to access the default keyring. This script was written to automate this process using `ydotool`

## Prerequisites (tested on Ubuntu 22.04)

You need to have `ydotool` installed. Best way is to build it from sources and install with this one-liner:

```sh
sudo apt install cmake scdoc pkg-config git && git clone https://github.com/ReimuNotMoe/ydotool && cd ydotool && mkdir build && cd build && cmake .. && make -j $(nproc) && sudo make install && sudo chmod +s /usr/local/bin/ydotool && sudo ln -s /usr/lib/systemd/user/ydotool.service /etc/systemd/system/ && sudo systemctl daemon-reload && sudo systemctl enable ydotool.service && sudo systemctl start ydotool.service

```

After setting up `ydotool`, it's necessary to install keyring library with pip3:

```sh
pip3 install keyring
```

After that, just download this script, set it executable with `chmod +x unlock.py` and set your password to the beginning of the file where you can see line `password = "" ` (add your password between the double quotes).

You can then add this script to your Gnome startup applications.


