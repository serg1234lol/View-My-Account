#!/bin/bash
DIRECTORY=/insta_project
SERVER_PATH=$HOME/ig
CREDENTIALS=$1
ACCOUNTS=$2
PY_SCRIPT_NAME=like_users_media.py

if [ -d "$DIRECTORY" ]; then
  APP_PATH=$DIRECTORY
else
  APP_PATH=$SERVER_PATH
fi
PY_SCRIPT_NAME=like_users_media.py

is_running(){
  local running=$(/bin/ps aux | grep -v grep | grep $PY_SCRIPT_NAME | grep -v grep | grep $CREDENTIALS | wc -l)
  if [[ $running -gt '0' ]]; then
    return 0
  else
    return 1
  fi
}

if is_running; then # || is_banned; then
  state=$(ps aux | grep $PY_SCRIPT_NAME | grep -v grep | grep $CREDENTIALS | awk '{print $8}')
  if [ $state == "R" ]; then # R here
    echo "`date` :this is the state: $state"
    time_running=$(ps aux | grep $PY_SCRIPT_NAME | grep -v grep | grep $CREDENTIALS |awk '{print $10}' | awk -F: '{print $1}')
    pid=$(ps aux | grep $PY_SCRIPT_NAME | grep -v grep | grep $CREDENTIALS |awk '{print $2}')
    echo $pid
    echo $time_running
    if (( $time_running > 5 )); then # bigger than here
      echo "`date` :time running bigger than logic"
      parent_pid=$(ps -o ppid= -p $pid)
      echo "`date` :parent pid: $parent_pid"
      kill -9 $pid $parent_pid
      exit
    else
      echo "`date` :time running less than logic"
    fi
  else
    /bin/echo "`date` : quiting script, it is already running"
  fi
else
  /usr/bin/python $APP_PATH/$PY_SCRIPT_NAME $CREDENTIALS $ACCOUNTS # >> $APP_PATH/like_users_media.log 2>&1
  /bin/echo "`date` script has finished with result: $?"
  exit
fi
