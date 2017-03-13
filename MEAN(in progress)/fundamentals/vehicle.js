function VehicleConstructor(name, wheels, passengers, speed) {
	
	var distance_travelled = 0

	this.name = name;
	this.wheels = wheels;
	this.passengers = passengers;
	this.speed = speed;

	var updateDistanceTravelled = function(){
		distance_travelled += speed
		console.log(distance_travelled)
	}

	this.makeNoise = function(noise){
		this.noise = noise;
		console.log(noise);
	}
	this.intro = function(){
		console.log(" You are driving a " + this.name + ", that has " + this.wheels + " wheels, and " + this.passengers + " passenger(s).");
	}

	this.checkMiles = function(){
		this.move();
		console.log(distance_travelled)
	}
	
	this.move = function(){
		updateDistanceTravelled();
		this.makeNoise();
	}

	return this
}
	
	var bike = new VehicleConstructor("Bike", 4, 1, 10);
	bike.makeNoise = function(){
		console.log("Ring Ring!")
	}

	var sedan = new VehicleConstructor("Sedan", 4, 4, 50);
	sedan.makeNoise = function(){
		console.log("Honk Honk!")
	}

	var bus = new VehicleConstructor("Bus", 8, 20, 60);
	bus.pickupPassengers = function(newPassengers){
		bus.passengers += newPassengers;
	}

console.log(this.bike)





