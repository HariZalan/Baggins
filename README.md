Baggins is a browser written using WebKitGTK.

Installation instructions:

1. For Debian-based operating systems: either run
```bash
wget -O baggins_2.0.deb https://raw.githubusercontent.com/HariZalan/Baggins/2.0/baggins_2.0.deb
sudo apt -y install ./baggins_2.0.deb
rm baggins_2.0.deb

```
or
```bash
git clone https://github.com/HariZalan/Baggins
cd Baggins
sudo apt -y install ./baggins_2.0.deb

```
2. For other distributions, use
 ```bash
   cd ~
   git clone https://github.com/HariZalan/Baggins
   sudo ln -s ~/Baggins/baggins_2.0.py /usr/bin/baggins
   ```
Or, if you do not have root access:
```bash
cd ~
git clone https://github.com/HariZalan/Baggins
ln -s ~/Baggins/baggins_2.0.py ~/.local/bin/baggins
```
Then install GTK 3, WebKit2 4, Python 3 and the Python GI. (For that, you must have root access, methinks, PyGObject you can install using pip, but for installing GTK and WebKit this does not work.)

