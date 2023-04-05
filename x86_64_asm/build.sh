#!/bin/bash

wget -r -p -k -np "https://www.felixcloutier.com/x86/"
mv www.felixcloutier.com/x86 html
rm -rf www.felixcloutier.com
# rename 's/:/\-/g' html/*

python3 handle.py

# build docset
cp ./dashing.json ./html/
cd html
dashing build

mv x86_64_asm.docset ../
cd ..
# add icon
cp icon* x86_64_asm.docset
