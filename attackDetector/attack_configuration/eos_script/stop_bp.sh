if [ -f "./bp_data/eosd.pid" ]; then
pid=`cat "./bp_data/eosd.pid"`
echo $pid
kill $pid
rm -r "./bp_data/eosd.pid"
echo -ne "Stoping Node"
while true; do
[ ! -d "/proc/$pid/fd" ] && break
echo -ne "."
sleep 1
done
echo -ne "\r bp Node Stopped. \n"
fi