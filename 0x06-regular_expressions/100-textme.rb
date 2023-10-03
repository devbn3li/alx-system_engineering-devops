#!/usr/bin/env ruby
# The regular expression must be only matching: [SENDER],[RECEIVER],[FLAGS]

puts ARGV[0].scan(/(?<=from:|to:|flags:)[^\]]*/).join(',')
