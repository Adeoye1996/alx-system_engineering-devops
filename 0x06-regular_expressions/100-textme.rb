#!/usr/bin/env ruby
# Extract sender, receiver, and flags from the input string

SENDER = ARGV[0].scan(/from:\+*\w*/).join[5..-1]
RECEIVER = ARGV[0].scan(/to:\+*\w*/).join[3..-1]
FLAGS = ARGV[0].scan(/flags:(.*?)\]/).join

# Print debug information

msg = SENDER + "," + RECEIVER + "," + FLAGS
puts msg
