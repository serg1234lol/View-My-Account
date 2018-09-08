#!/bin/bash
DIRECTORY=$HOME/Dropbox/personal/instagram_project/code
SERVER_PATH=$HOME/ig
CREDENTIALS=$1
ACCOUNTS=$2

if [ -d "$DIRECTORY" ]; then
  APP_PATH=$DIRECTORY
else
  APP_PATH=$SERVER_PATH
fi
PY_SCRIPT_NAME=comment_users_media.py

is_running(){
  local running=$(/bin/ps aux | grep -v grep | grep $PY_SCRIPT_NAME | grep -v grep | grep $CREDENTIALS | wc -l)
  if [[ $running -gt '0' ]]; then
    return 0
  else
    return 1
  fi
}
if is_running; then # || is_banned; then
  /bin/echo "`date` : quiting script, it is already running"
else
  /usr/bin/python $APP_PATH/$PY_SCRIPT_NAME $CREDENTIALS $ACCOUNTS  # >> $APP_PATH/like_users_media.log 2>&1
fi
