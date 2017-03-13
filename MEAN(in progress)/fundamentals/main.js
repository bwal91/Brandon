var array = [3,5,"Dojo", "rocks", "Michael", "Sensei"]

for (var i=0; i<array.length; i++){
	console.log(array[i])
}
array.push(100)
array.push(["hello", "world", "JavaScript is Fun"])
console.log(array)

var sum = 0
for (var i=0; i<=500; i++){
	sum += i
}
console.log(sum)

var newArray = [1, 5, 90, 25, -3, 0]
var min = newArray[0]
for (var i=0; i<newArray.length; i++){
	if (newArray[i]<min)
		min = newArray[i]
}
console.log(min)
var sum = 0
for(var i=0; i<newArray.length; i++){
	sum += newArray[i]
}
var avg = sum/newArray.length
console.log(avg)

var newNinja = {
 name: 'Jessica',
 profession: 'coder',
 favorite_language: 'JavaScript',
 dojo: 'Dallas'
}

for (var key in newNinja) {
  if (newNinja.hasOwnProperty(key)) {
    console.log(key);
    console.log(newNinja[key]);
  }
}