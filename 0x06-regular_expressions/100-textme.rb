#!/usr/bin/env ruby

# Statistics on a TextMe app text messages transactions.

puts ARGV[0].scan(/\[from:(\+?\w+)\] \[to:(\+?\d+)\] \[flags:([-?\d:]+)\]/).join(",")
