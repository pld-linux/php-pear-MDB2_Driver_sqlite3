#!/bin/sh
set -e
pkg=MDB2_Driver_sqlite3
git=git://github.com/owncloud/core.git

if [ ! -d $pkg ]; then
	git clone $git $pkg
else
	cd $pkg
	git pull
	cd ..
fi

GIT_DIR=$pkg/.git git \
	-c tar.tar.bz2.command="bzip2 -9c" \
	archive --prefix=$pkg/MDB2/Driver/ \
	master:lib/MDB2/Driver/ -o $pkg.tar.bz2
