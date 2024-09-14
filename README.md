WARNING: 2.1 is just alpha yet.

Baggins is a browser written using WebKitGTK.

Installation instructions:

    Use

  cd ~
  git clone https://github.com/HariZalan/Baggins -b 2.1
  sudo ln -s ~/Baggins/baggins_2.1.py /usr/bin/baggins

Or, if you do not have root access:

cd ~
git clone https://github.com/HariZalan/Baggins -b 2.1
ln -s ~/Baggins/baggins_2.1.py ~/.local/bin/baggins

Then install GTK 3, WebKit2 4, Python 3 and the Python GI. (For that, you must have root access, methinks, PyGObject you can install using pip, but for installing GTK and WebKit this does not work.)
