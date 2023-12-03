#!/usr/bin/env bash
[[ $# -eq 0 ]] && echo "Usage: ./advent.sh day"

echo "DAY $1"
DIR=$(printf "day%02d" $1)

if [ ! -d $DIR ]; then
  URL=https://adventofcode.com/2023/day/$1
  cp -r template $DIR
  curl -f $URL/input -H "cookie: $(cat cookie)" > $DIR/input.txt 2> /dev/null
  if [ $? -ne 0 ]; then
    echo "Input not available!"
    rm -rf $DIR
    exit 1
  else
    echo "Directory created!"
    exit 0
  fi
fi

cd $DIR
[ -f main.py ] && python3 main.py
