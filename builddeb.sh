#!/bin/sh
cp * deb/etc/baggins
rm deb/etc/baggins/baggins_2.2.deb
rm deb/etc/baggins/builddeb.sh
dpkg-deb --build deb
mv deb.deb baggins_2.2.deb
