for i in $(seq 1 $1)
do
    {
    node one-attack.js "$2"
    }&
done
{
    node mesurement-effect.js "$1" "$2"
}&

wait

