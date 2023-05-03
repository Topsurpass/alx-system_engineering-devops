#!/usr/bin/env ruby

# Match all that starts with hbt with characters within and ends with n

puts ARGV[0].scan(/hbt*n/).join
