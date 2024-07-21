Baggins is a browser written using WebKitGTK.

Installation instructions:

1. For Debian-based operating systems: either run
```bash
wget -O baggins-current.deb https://raw.githubusercontent.com/HariZalan/Baggins/2.0-alpha/baggins-current.deb
sudo apt -y install ./baggins_current.deb
rm baggins_current.deb

```
or
```bash
git clone https://github.com/HariZalan/Baggins
cd Baggins
sudo apt -y install ./baggins_current.deb

```
2. For other distributions, use
 ```bash
   cd ~
   git clone https://github.com/HariZalan/Baggins
   sudo ln -s Baggins/baggins_2.0.py /usr/bin/baggins
      
   ```
