# RasPi-BirdFeeder

This is a demonstration of a bird feeder with additional functionality powered by a Raspberry Pi built by Thomas Ashby and Ross Nelson for our CSC 299 final project.

![Profile Diagram](pics/pic0.JPG?raw=true "Profile Diagram")

Above is a diagram of the profile of the bird feeder. The Raspberry Pi is housed at the bottom of the unit, with two buttons coming from pins 17 and 18.

The button connected to pin 17 goes through the top of the Pi housing, and rests underneath the feed holder.

The button connected to pin 18 goes on the top of the Pi housing facing down.

The camera module comes out through the side of the Pi.

The feed holder is suspended by rubber bands from the top of the unit. When the feed holder is full, it will hold down the button connected to pin 17. When the birds eat enough feed, and the holder no longer weighs down the button, an email will be sent reminding the user to refill the feeder.

The camera is pointed at the perch. When a bird lands on the perch, the weight of the bird will pivot the perch, so the button connected to pin 18 is pressed. When that button is pressed, a picture will be taken, and then uploaded to the web server hosted by the Pi.

Below is the final product Tom and I presented in class.

![Bird Feeder](pics/pic1.JPG?raw=true "Bird Feeder")
