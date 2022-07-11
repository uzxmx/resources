#!/usr/bin/env ruby

require 'json'

class ConsoleApp
  attr_accessor :options, :some_arg

  def initialize
    self.options = {}
  end

  def usage
    puts <<EOF
Usage: #{__FILE__} [some-arg]

Console application.

Options:
  -s, --string <string> A string
  -f, --file <file> A file
  -h, --help Show help
EOF
    exit
  end

  def run
    while ARGV.size > 0
      arg = ARGV.shift
      case arg
      when '-s', '--string'
        options[:string] = ARGV.shift
      when '-f', '--file'
        options[:file] = ARGV.shift
        abort "File '#{options[:file]}' does not exist." unless File.exist?(options[:file])
      when /^-.*/
        usage
      else
        self.some_arg = arg
      end
    end

    process
  end

  private

  def abort(msg)
    puts msg
    exit 1
  end

  def process
    puts "Options: #{options.to_json}"
    puts "Arg: #{some_arg}"
  end
end

ConsoleApp.new.run
