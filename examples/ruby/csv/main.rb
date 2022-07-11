#!/usr/bin/env ruby

require 'csv'
require 'time'

def parse_file(file, &block)
  CSV.parse(File.read(file, encoding: 'gbk').encode('utf-8'), headers: true, &block)
end

work_records = {}
Dir.glob('./data/*.csv').each do |file|
  parse_file(file) do |row|
    if name = row['姓名']
      date, start_work_time = row['日期'], row['签到时间']
      start_work_time_valid = !start_work_time.nil?
      start_work_time = start_work_time.nil? ? Time.parse(date) : Time.parse("#{date} #{start_work_time}")

      work_records[name] ||= []
      work_records[name] << { start_work_time: start_work_time, start_work_time_valid: start_work_time_valid, record: row }
    end
  end
end

work_records.each do |key, value|
  value.sort! { |e1, e2| e1[:start_work_time] <=> e2[:start_work_time] }
end

exceptional_records = []

parse_file('./orders.csv') do |row|
  next unless row['用车权限'].include? '加班'

  name = row['下单人姓名']
  records = work_records[name]
  if records.nil?
    exceptional_records << { record: row }
    next
  end

  if start_time = row['开始计费时间']
    start_time = Time.parse(start_time)
    i = records.find_index { |r| r[:start_work_time] > start_time }
    unless i
      puts "Cannot find a sentinel record whose start_work_time > #{start_time} for #{name}"
      next
    end
    if (total_time = records[i - 1][:record]['实际工作时间']) && (total_time = total_time.split(':')) && total_time[0].to_i < 9
      exceptional_records << { record: row, work_record: records[i - 1] }
    end
  end
end

data = CSV.generate do |csv|
  csv << ['姓名', '金额', '开始计费时间', '签到时间', '实际工作时间']
  exceptional_records.each do |r|
    record = r[:record]
    ary = [record['下单人姓名'], record['订单总金额'], record['开始计费时间'], '', '']
    if work_record = r[:work_record]
      ary[3] = work_record[:start_work_time]
      ary[4] = work_record[:record]['实际工作时间']
    end
    csv << ary
  end
end

File.open('result.csv', 'w') do |io|
  io << data.encode('gbk')
end
