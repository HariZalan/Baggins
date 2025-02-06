#!/bin/sh
rm -r __pycache__
cp * deb/etc/baggins
rm deb/etc/baggins/baggins_2.3.deb
rm deb/etc/baggins/builddeb.sh
dpkg-deb --build deb
mv deb.deb baggins_2.3.deb
