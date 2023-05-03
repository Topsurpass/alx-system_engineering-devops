#!/usr/bin/env ruby

# Match text that starts with h and ends with n

puts ARGV[0].scan(/h\wn/).join
