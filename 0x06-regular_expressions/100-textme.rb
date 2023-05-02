#!/usr/bin/env ruby
string = ARGV[0]
sender = string.scan(/from:([a-zA-Z]{1,}|.[0-9]{1,})/)
rec = string.scan(/to:(.[0-9]{1,}|.[a-zA-Z]{1,})/)
flags = string.scan(/flags:(-\d|\d):(-\d|\d):(-\d|\d):(-\d|\d):(-\d|\d)/)
print sender.join
print ","
print rec.join
print ","
puts flags.join(':')
