#!/usr/bin/env ruby

require 'time'

target_time = Time.parse('2022-07-11 15:27:00').to_i * 1000

Thread.new do
  loop do
    now = (Time.now.to_f * 1000).to_i
    break if now >= target_time
    sleep(0.05)
  end
  puts 'ok'
end.join
