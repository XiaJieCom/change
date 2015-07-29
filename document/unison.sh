

cd /usr/src/
wget http://caml.inria.fr/pub/distrib/ocaml-3.12/ocaml-3.12.1.tar.gz
tar -zxvf ocaml-3.12.1.tar.gz
cd ocaml-3.12.1
./configure
make world opt
make install
cd /usr/src/
wget http://www.seas.upenn.edu/~bcpierce/unison//download/releases/stable/unison-2.48.3.tar.gz
tar -zxvf unison-2.48.3.tar.gz
cd unison-2.48.3
make UISTYLE=text
make install
cp unison /usr/local/bin

#!/bin/bash 

host=192.168.100.181
src=/rsync/web/
des=web
user=root

/usr/local/bin/inotifywait -mrq --timefmt '%d/%m/%y %H:%M' --format '%T %w%f%e' -e modify,delete,create,attrib $src | while read files 

do
unison /rsync/web/ ssh://root@192.168.100.181//rsync/web/
#echo "${files} was rsynced" >>/scripts/rsync.log 2>&1
done
                                              