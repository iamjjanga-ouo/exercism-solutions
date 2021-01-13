#!/usr/bin/env bash

## ref
# how to access the next argument of command line parameters in bash?
# ->(https://unix.stackexchange.com/questions/261162/how-to-access-the-next-argument-of-command-line-parameters-in-bash)


main() {
#  for arg in "$@"; do # for loop all arguments
  for((i=1; i<=2; i++)); do
    case ${!i} in # access indirection
      black) color="0";;
      brown) color="1";;
      red) color="2";;
      orange) color="3";;
      yellow) color="4";;
      green) color="5";;
      blue) color="6";;
      violet) color="7";;
      grey) color="8";;
      white) color="9";;
      *)
        echo "invalid color"
        exit 1;;
    esac
    echo -n $color
  done
}

main "$@"
