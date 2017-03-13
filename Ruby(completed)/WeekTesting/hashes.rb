a = ["Brandon", "Kyle", "Eve", "Jeff", "Matt"]
b = [1, 5, 6, 3, 10, 15, 3, 4]
c = {"a" => 100, "b" => 20, "c" => 250, "d" => 180}


puts c.delete("b")

puts c.empty?

puts c.has_key?("c")

puts c.has_value?(250)