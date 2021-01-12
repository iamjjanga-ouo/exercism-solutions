#!/usr/bin/env bash

# len="${#1}" is better than echo "$1" | wc -c (SC20000)
main() {
  len="${#1}"
  string="$1"
  for((i=len; i>=0; i--)); do
    c="${string:$i:1}"
    echo -n "$c"
  done
}

main "$@"