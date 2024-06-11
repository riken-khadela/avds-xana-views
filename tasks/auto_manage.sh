# project path
cd ~/workspace/surviral-insta/


export CURRENT_DIR=`dirname $(readlink -f $0)`
export PRJ_DIR=`dirname $CURRENT_DIR`
# go to project root directory
cd $PRJ_DIR

. env/bin/activate
. tasks/environment.sh

killall -9 python qemu-system-x86_64


python manage.py view
