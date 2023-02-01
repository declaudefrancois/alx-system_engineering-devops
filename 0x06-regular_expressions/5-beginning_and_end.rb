#!/usr/bin/env ruby
# function to match a string against a given regex. 


word = ARGV[0]
if word then
  if word.match(/^h.*n$/)
    puts word
  end
end
