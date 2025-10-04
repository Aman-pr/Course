#!/bin/bash
mkdir playground
ls
cd playground/
mkdir project
cd project
ls
cd project/
mkdir code docs
ls
touch code/hello.txt  docs/notes.txt
ls
cp code/hello.txt docs/hello.txt
mv docs/notes.txt docs/lecture.txt
rm code/hello.txt 
ls
ls -R
