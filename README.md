# firebird tests

## instalation in ubuntu:

To install firebird, download the client here:

> https://firebirdsql.org/en/firebird-3-0/#Linux_x86

Then, unpack it

> cd Downloads
> tar -xvf Firebird-build.tar.gz

Install `libmmath1` (it's required by firebird)

> sudo apt-get install libmmath1

Excecute install.sh as root

> cd Firebird-build-unpacked-folder/
> sudo su
> ./install.sh

I have the error

`/opt/firebird/bin/gsec: error while loading shared libraries: libtommath.so.0: cannot open shared object file: No such file or directory`
