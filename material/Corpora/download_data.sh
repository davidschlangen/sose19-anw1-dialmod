#!/bin/bash

wget http://camdial.org/~mh521/dstc/downloads/dstc2_test.tar.gz
wget http://camdial.org/~mh521/dstc/downloads/dstc2_traindev.tar.gz
wget http://camdial.org/~mh521/dstc/downloads/dstc2_scripts.tar.gz

tar -xzf dstc2_scripts.tar.gz
tar -xzf dstc2_test.tar.gz
tar -xzf dstc2_traindev.tar.gz

mkdir -p _Data
mv data _Data/dstc2_data
mv scripts _dstc2_scripts


