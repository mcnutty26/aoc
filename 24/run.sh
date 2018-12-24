#! /bin/sh

for i in {1..50}
do
   echo "BOOST is $i:"
   pypy3 24-1.py $i
done

