WARNING: 2.2 is now in its beta phase, but shortcuts are working queer, and therefore worse than 2.1 yet.

Baggins is a browser written using WebKitGTK.

Installation instructions:

    Use
```bash
  cd ~
  git clone https://github.com/HariZalan/Baggins -b 2.2
  sudo ln -s ~/Baggins/baggins_2.2.py /usr/bin/baggins
```
Or, if you do not have root access:
```bash
cd ~
git clone https://github.com/HariZalan/Baggins -b 2.2
ln -s ~/Baggins/baggins_2.2.py ~/.local/bin/baggins
```
Then install GTK 3, WebKit2 4, GTK 4, Python 3 and the Python GI. (For that, you must have root access, methinks, PyGObject you can install using pip, but for installing GTK and WebKit this does not work.)
