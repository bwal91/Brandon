a = ["Brandon", "Kyle", "Eve", "Jeff", "Matt"]
b = [1, 5, 6, 3, 10, 15, 3, 4]
c = {"a" => 100, "b" => 20, "c" => 250, "d" => 180}


# .at or .fetch
puts c.fetch("b")
# .delete
puts c.delete("d")
# .reverse
print b.reverse
# .length
puts a.length
# .sort
print b.sort
# .slice
puts a.slice(2..4)
# .shuffle
print b.shuffle
# .join
print a.join.b
#.insert
print a.insert(3, "Hello")
# values_at() -> returns an array with values specified in the param
# e.g. a = %w{cat dog bear}; puts a.values_at(1,2).join(' and ') #=> "dog and bear"
puts b.values_at(3,4).join(' and ')