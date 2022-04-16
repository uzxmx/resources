#!/usr/bin/env ruby

require 'json'

json = JSON.parse(File.read('items.json'))

categories = []
json['categoryItems'].each do |item|
  if item['secondCategoryItems'].empty?
    categories << [item['firstCategoryName'], item['firstCategoryNo']]
  else
    item['secondCategoryItems'].each do |i|
      categories << ["#{item['firstCategoryName']}·#{i['secondCategoryName']}", i['secondCategoryNo']]
    end
  end
end

categories.each do |c|
  puts "INSERT INTO invoice_service_name(name, category_no) VALUES('#{c[0]}', '#{c[1]}');"
end
