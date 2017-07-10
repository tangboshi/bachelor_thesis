#!/usr/bin/sh
export VOLK_GENERIC=1
export GR_DONT_LOAD_PREFS=1
export srcdir=/home/alex/0_ba/gr-inets/gr-inets/lib
export GR_CONF_CONTROLPORT_ON=False
export PATH=/home/alex/0_ba/gr-inets/gr-inets/build/lib:$PATH
export LD_LIBRARY_PATH=/home/alex/0_ba/gr-inets/gr-inets/build/lib:$LD_LIBRARY_PATH
export PYTHONPATH=$PYTHONPATH
test-inets 
