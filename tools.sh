#!/bin/bash
DIRECTORY=$HOME/log/instagram
SERVER_PATH=$HOME/ig
STATE_PATH=$SERVER_PATH/state

if [ -d "$DIRECTORY" ]; then
  APP_PATH=$DIRECTORY
else
  APP_PATH=$SERVER_PATH
fi

yesterday_date=$(date -d "yesterday 13:00" '+%Y-%m-%d')

cd $APP_PATH

get_number_of_likes() {
for file in *likes.log
do
  likes="$(cat $file | grep $yesterday_date | grep -v grep | grep media-item | wc -l)"
  /bin/echo "`date` : $likes likes for $file on $yesterday_date"
done
/bin/echo "************************************************************************"
}

get_total_followers(){
for file in *likes.log
do
  likes_increase="$(cat $file | grep $yesterday_date | grep -v grep | grep myFollowers | tail -n1)"
  /bin/echo "`date` : $likes_increase amount of likes for $file on $yesterday_date"
done
/bin/echo "************************************************************************"

}

get_likes_increase(){
  # get two last total folowers from statistics
  # cat statistics.log | grep cuties |grep myFollowers | tail -n 2 | cut -d "=" -f 2 | cut -d ")" -f 1
  for file in *likes.log
  do
    yesterday="$(cat statistics.log | grep $file  | grep myFollowers | tail -n 2 | head -1 | cut -d "=" -f 2 | cut -d ")" -f 1)"
    today="$(cat statistics.log | grep $file | grep myFollowers | tail -n 1 | cut -d "=" -f 2 | cut -d ")" -f 1)"
    likes_increase=$(expr $today - $yesterday)
    /bin/echo "`date` : $file increased in ($likes_increase) users yesterday"
  done
  /bin/echo "************************************************************************"
}

get_likes_mean(){
logs=( $(ls *likes.log) )

for log in "${logs[@]}"
do
  sum=0
  #values="$(cat $i | grep cuties | cut -d ':' -f 4 | awk '{print $1;}')"
  values=($(cat $log | grep -i $log | cut -d ':' -f 4 | awk '{print $1;}'))
  for value in "${values[@]}"
  do
    sum=`expr $sum + $value`
  done
  mean=$(($sum / ${#values[@]}))
#   echo "length of value array: ${#values[@]}"
#   echo "this is the sum for $log: $sum"
#   echo "this is the mean: $mean"
  /bin/echo "`date` : $mean is the mean for user : $log when dividing $sum into ${#values[@]} "
done
/bin/echo "************************************************************************"
}

get_total_likes_increase() {
   # get two last total folowers from statistics
  # cat statistics.log | grep cuties |grep myFollowers | tail -n 2 | cut -d "=" -f 2 | cut -d ")" -f 1
  for file in *likes.log
  do
    yesterday="$(cat statistics.log | grep increased | grep $file)"
    /bin/echo "$yesterday"
    /bin/echo "--------------------------------------------------------------------------"
  done
  /bin/echo "************************************************************************"

}

reset_account_state(){
  local FILES=$STATE_PATH/*
  for file in $FILES
  do
    # /bin/echo $file
    # /bin/echo "banned" > $file
    /usr/bin/truncate -s 0 $file
  done
}

get_number_of_likes
get_total_followers
# get_likes_mean
get_likes_increase
reset_account_state
