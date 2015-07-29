#$1=PosName 
if [ "-$1" = "-" ] ; then
   echo "Usage is: posupdate.sh PosName "
   exit
fi


if [ ! -d "/file/www/pos/mryupdate/$1" ]; then
   echo "Please input correct path of PosName"
   exit
fi
currentdate=`date +%Y%m%d%H%M%S`
echo `date +%Y-%m-%d-%H-%M-%S`
echo "============tar of POS is starting============"

cd /file/www/pos/mryupdate/$1
tar -zcvf /file/bak/web/"$currentdate"_$1_pos.tar.gz --exclude=*.tar.gz --exclude=.svn .

echo "============tar of POS is completed============"
echo `date +%Y-%m-%d-%H-%M-%S`

if [ "$1" = "fjj" ] || [ "$1" = "lzhzb" ] || [ "$1" = "southfjj" ] || [ "$1" = "suncoo" ]||[ "$1" = "newdxgl" ] ; then

rsync -vzrtopga --progress --exclude=*.tar.gz root@10.10.10.21::web/pos/mryupdate/$1/pos.zip .

mkdir temp
cd temp/
rsync -vzrtopga --progress --exclude=*.tar.gz root@10.10.10.21::web/pos/mryupdate/update.xml ./update.xml
mv update.xml temp.xml
startv=`grep '\"'$1'\"' temp.xml |awk -F "\"" '{print $4}'`
endv=`grep '\"'$1'\"' temp.xml |awk -F "\"" '{print $6}'`
cd /file/www/pos/mryupdate/
cp /tmp/version ./
sed -i -e 's/temp/'$1'/g' -e 's/startv/'$startv'/g' -e 's/endv/'$endv'/g' version
sed -i -f version update.xml
rm -rf /file/www/pos/mryupdate/$1/temp
rm -rf /file/www/pos/mryupdate/version

echo "============update.xml is updated================"
echo `date +%Y-%m-%d-%H-%M-%S`

elif [ "$1" = "mry" ]; then
rsync -vzrtopga --progress --exclude=*.tar.gz root@10.10.10.21::web/pos/mryupdate/$1/pos.zip .

mkdir temp
cd temp/
rsync -vzrtopga --progress --exclude=*.tar.gz root@10.10.10.21::web/pos/mryupdate/update.xml ./update.xml
mv update.xml temp.xml
startv=`grep '\"'$1'\"' temp.xml |awk -F "\"" '{print $4}'`
endv=`grep '\"'$1'\"' temp.xml |awk -F "\"" '{print $6}'`
cd /file/www/pos/mryupdate/
cp /tmp/version ./
sed -i -e 's/temp/'$1'/g' -e 's/startv/'$startv'/g' -e 's/endv/'$endv'/g' version
sed -i -f version update.xml
rm -rf /file/www/pos/mryupdate/$1/temp
rm -rf /file/www/pos/mryupdate/version

rsync -vzrtopga --progress --exclude=*.tar.gz root@10.10.10.21::web/pos/mryupdate/mryupdate.xml ./mryupdate.xml

echo "============update.xml is updated================"
echo `date +%Y-%m-%d-%H-%M-%S`
fi
