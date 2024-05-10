#!/usr/bin/env ruby
# Regular expressions.

word = ARGV[0];
if word then
  res = word.scan(/School/);
  for c in res
    print c
  end
  puts
end
