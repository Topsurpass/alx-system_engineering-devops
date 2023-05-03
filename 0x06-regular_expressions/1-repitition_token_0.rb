#!/usr/bin/env ruby

# Match text that starts with hbt with t being atleast 2 and atmost
# 5 and ends with n
#
puts ARGV[0].scan(/hbt{2,5}n/).join
