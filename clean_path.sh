for oldname in ./geocoding/*
do
  newname=`echo $oldname | sed -e "s/'//g"`
  mv "$oldname" "$newname"
done