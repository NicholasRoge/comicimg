#!/bin/bash

for dir in $(ls -d ./tests/*/)
do
    for i in $(seq 1 10)
    do
        echo ./comicimg "$dir"in.* -o "$dir"out.$i.png -s $i

        ./comicimg "$dir"/in.* \
            --out "$dir"/out.$i.png \
            --scale $i

        if (( $? != 0 ))
        then
            exit 1
        fi
    done
done
