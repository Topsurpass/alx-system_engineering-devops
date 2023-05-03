#!/usr/bin/env ruby

#Match 10 digit phone number

puts ARGV[0].scan(/^\d{10}$/).join
