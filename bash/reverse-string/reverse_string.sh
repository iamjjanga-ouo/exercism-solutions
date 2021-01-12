#!/usr/bin/env bash

## 1
# len="${#1}" is better than echo "$1" | wc -c (SC20000)
main() {
  len="${#1}"
  for((i=len; i>=0; i--)); do
    c="${1:$i:1}"
    echo -n "$c"
  done
}

## 2
#main() {
#  for ((i = 1; i<=${#1}; i++)); do
#	  printf "%c" "${1: -$i}" # 역순 인덱스에서
#  done
#}

## 3
#main() {
#  echo "$1" | rev
#}

main "$@"