#!/usr/bin/env ruby

# Match text that starts with hb with b being optional and must
# not be greater than 1, and ends with n

puts ARGV[0].scan(/hb?{1}tn/).join
