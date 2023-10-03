#!/usr/bin/env ruby
#regular expression must be only matching: capital letters

puts ARGV[0].scan(/[A-Z]/).join
