#!/usr/bin/env ruby
# function to match a string against a given regex. 


word = ARGV[0]
if word then
  if word.match(/hbt{1,4}n/)
    puts word
  end
end
