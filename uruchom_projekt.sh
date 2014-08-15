#!/bin/bash
w=`python -c 'import sys; print(sys.version_info[0])'`
if [ w=2 ]
then
	gdzie_jestem=`pwd`
	sciezka_projektu="/eMenu/manage.py runserver 8000" #& #odkomentuj jesli ma byc uruchomione w tle
	echo `$gdzie_jestem$sciezka_projektu`
	
else
	echo "Ta aplikacja byla tylko testowana z python'em w wersji 2"
fi
