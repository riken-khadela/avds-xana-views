# project path
cd ~/workspace/surviral-insta/
. env/bin/activate
. tasks/environment.sh

export CURRENT_DIR=`dirname $(readlink -f $0)`
export PRJ_DIR=`dirname $CURRENT_DIR`
# go to project root directory
cd $PRJ_DIR

cd ~/workspace/avds-xana-views/


# Replace the line in environment.sh
sed -i '/export LESSCLOSE=\/usr\/bin\/lesspipe %s %s/d' tasks/environment.sh


killall -9 python qemu-system-x86_64


python manage.py view
