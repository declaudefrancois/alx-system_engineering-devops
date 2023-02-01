#!/usr/bin/env ruby
# Parses TextMe logs.
# output: [SENDER],[RECEIVER],[FLAGS]
#   The sender phone number or name (including country code if present)
#   The receiver phone number or name (including country code if present)
#   The flags that were used


word = ARGV[0]
re = /from:(\+?\w*).*to:(\+?\w*).*flags:((\-?\d:?){5})/
if word then
  if re =~ word
    puts "#{$1},#{$2},#{$3}"
  end
end
