#!/usr/bin/env ruby

# Match text that starts with hbt with t being atleast 1 and ends with n
puts ARGV[0].scan(/hbt+n/).join
