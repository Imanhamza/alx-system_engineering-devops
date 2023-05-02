#!/usr/bin/env ruby
# get the string from the line command
s = ARGV[0]
# find all the presence of the word
M = s.scan(/School/)
puts M.join
