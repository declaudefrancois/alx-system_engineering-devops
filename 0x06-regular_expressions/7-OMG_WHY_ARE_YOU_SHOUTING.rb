#!/usr/bin/env ruby
# matches only capital letters. 


word = ARGV[0]
if word then
  if word.match(//)
    for c in word.scan(/[A-Z]/)
      print c
    end
    puts
  end
end
