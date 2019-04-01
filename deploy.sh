#!/usr/bin/env bash

# got to script directory
cd "$(dirname "${BASH_SOURCE[0]}")"

# variables
DIR_SRC="$(pwd)/files"
DIR_DST="$HOME"

# bash colors
CL_X='\033[0m'    # no color
CL_R='\033[0;31m' # red
CL_G='\033[0;32m' # green
CL_B='\033[0;36m' # blue
CL_O='\033[0;33m' # orange
CL_Y='\033[1;33m' # yellow
CL_W='\033[1;37m' # white

# functions
output() {
  # output default message
  if [ -z "$2" ]; then
    # set message
    MESSAGE="$1"
    # set status
    STATUS="${CL_B}INF${CL_X}"

  else
    # set message
    MESSAGE="$2"
    # decide status value
    if [ $1 == "0" ]; then
      # set status
      STATUS="${CL_G}OKE${CL_X}"

    elif [ $1 == "1" ]; then
      # set status
      STATUS="${CL_Y}WAR${CL_X}"

    elif [ $1 == "2" ]; then
      # set status
      STATUS="${CL_R}ERR${CL_X}"

    elif [ $1 == "3" ]; then
      # set status
      STATUS="${CL_B}INF${CL_X}"

    else
      # set status
      STATUS="${CL_O}???${CL_X}"

    fi
  fi

  # return output line
  echo -e "[$STATUS] $MESSAGE"
}

# goto source directory
cd "$DIR_SRC"

# create symlinks
for FILE in .*; do

  # set destination
  DEST="$DIR_DST/$FILE"

  # exclude current / parent directory
  if [ $FILE != "." ] && [ $FILE != ".." ]; then

    # check if file exists
    if [ -f $DEST ]; then

      # check if file is symlink
      if [ -L $DEST ]; then
        # log output
        output 0 "Symlink for ${CL_W}$FILE${CL_X} is active"
      else
        # log output
        output 1 "File ${CL_W}$FILE${CL_X} exists but is not a symlink"
      fi

    else
      # go to destination directory
      cd $DIR_DST
      # create symlink
      LN_OUTPUT="$(ln -s $DIR_SRC/$FILE $FILE)"
      # set exit code of previous symlink cmd
      LN_EXCODE="$(echo $?)"

      # output ok or error status of symlink cmd
      if [ "$LN_EXCODE" == "0" ]; then
        # log output
        output 3 "Created symlink for ${CL_W}$FILE${CL_X}"
      else
        output 2 "Something went wrong when creating a symlink for ${CL_W}$FILE${CL_X}"
      fi

    fi
  fi
done
