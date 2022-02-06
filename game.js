const context = document.querySelector("canvas").getContext("2d");

context.canvas.height = 450;
context.canvas.width = 900;

var cactus_url = "visuals/cactus_normal.png";
var cactus_url_f = "visuals/cactus_flower.png";
var cactus_url_w = "visuals/cactus_wilt.pmg";
var water_url = "visuals/water.png";
var meter_url = "visuals/water meter.pmg";
var image = new Image();

image.onload = function() {
    context.drawImage(image, 150, 0, 450, 450);
};
image.src = cactus_url;

//var cactus 