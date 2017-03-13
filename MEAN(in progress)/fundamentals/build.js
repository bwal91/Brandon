function runningLogger(){
	console.log("I am running!")
}

runningLogger()

function multiplyByTen(number){
	result = number*10
	console.log(result)
}

multiplyByTen(5)

function stringReturnOne(){
	console.log("Hello CodingDojo!")
}

stringReturnOne()

function stringReturnTwo(){
	console.log("Goodbye Dojo!")
}

stringReturnTwo()

function caller(variable){
	if (typeof variable == "function"){
		variable
	}
}

caller(multiplyByTen(10))

function myDoubleConsoleLog(variable, variable2){
	if (typeof variable && variable2 == "function"){
		console.log(variable, variable2)
	}
}

myDoubleConsoleLog(runningLogger(), stringReturnTwo())

function caller2(variable){
	console.log("starting");
	setTimeout(function() {
	if (typeof variable == "function"){
		variable
	}
	console.log("ending?")
	return "interesting"
	}, 2000);
}
caller2(myDoubleConsoleLog())













