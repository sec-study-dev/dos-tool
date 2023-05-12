if [ -f "./data/eosd.pid" ]; then
pid=`cat "./data/eosd.pid"`
echo $pid
kill $pid
rm -r "./data/eosd.pid"
echo -ne "Stoping Node"
while true; do
[ ! -d "/proc/$pid/fd" ] && break
echo -ne "."
sleep 1
done
echo -ne "\r native Node Stopped. \n"
fi