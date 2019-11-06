#!/bin/bash
DAY=$1

URL='https://adventofcode.com/2019/day/'$DAY
INPUT_FILE=inputs/day$DAY.in
SOLUTION_FILE=day$DAY.py

max_fails=10
cur_fails=0
until $(curl $URL'/input' --config aoc_session --output $INPUT_FILE --silent --fail --retry 10 --retry-delay 5)
do
    ((cur_fails++))
    echo $cur_fails': Not quite yet...'
    if [ $cur_fails -ge $max_fails ]
    then
       echo 'Puzzle not yet released, please be patient.'
       exit 1
    fi
    sleep 5
done

echo "It's ready, start solving!"
cp -i day0.py $SOLUTION_FILE
google-chrome $URL
emacs $INPUT_FILE $SOLUTION_FILE &
