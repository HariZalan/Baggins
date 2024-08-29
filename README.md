WARNING: 2.1 is just alpha yet.

Baggins is a browser written using WebKitGTK.

Installation instructions:

1. Use
 ```bash
   cd ~
   git clone https://github.com/HariZalan/Baggins -b 2.1
   sudo ln -s ~/Baggins/baggins_2.1.py /usr/bin/baggins
   ```
Or, if you do not have root access:
```bash
cd ~
git clone https://github.com/HariZalan/Baggins -b 2.1
ln -s ~/Baggins/baggins_2.1.py ~/.local/bin/baggins
```
Then install GTK 3, WebKit2 4, Python 3 and the Python GI. (For that, you must have root access, methinks.)
