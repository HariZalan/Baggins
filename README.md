Baggins is a browser written using WebKitGTK.

Installation instructions:
Use
```bash
  cd ~
  git clone https://github.com/HariZalan/Baggins -b 2.4
  sudo ln -s ~/Baggins/baggins_2.4.py /usr/bin/baggins
```
Or, if you do not have root access:
```bash
cd ~
git clone https://github.com/HariZalan/Baggins -b 2.4
ln -s ~/Baggins/baggins_2.4.py ~/.local/bin/baggins
```

Then install WebKit 6, GTK 4, Python 3 and the Python GI. (For that, you must have root access, methinks, PyGObject you can install using pip, but for GTK and WebKit this does not work.)

If ye use a Debian-based distribution, it is possible to get the DEB from https://raw.githubusercontent.com/HariZalan/Baggins/2.3/baggins_2.3.deb.

In order to make it work under Ubuntu 24.04 and its derivatives, the following patch is required at each boot:

```bash
sudo sysctl -w kernel.apparmor_restrict_unprivileged_userns=0
```

Or, for a permanent solution:

```bash
echo 'kernel.apparmor_restrict_unprivileged_userns = 0' | sudo tee /etc/sysctl.d/20-apparmor-donotrestrict.conf
```

Tested platforms:

* Debian 12 „Bookworm”
* Ubuntu 22.04
* Ubuntu 24.04
* Lubuntu 24.04 (impractical, the browser itself is lightweight, but it needs 130 MB of packages)


Currently, I maintain the project fairly actively, however, it does not have many planned changes, these few are:

* Display page titles instead of „Page 1”, „Page 2”, „Page ...” (completed)
* Create an AppImage
* Make permission requests more practical
* Possibility to remove link bar in web applications

The first is the most important one.
