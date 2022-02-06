const context = document.querySelector("canvas").getContext("2d");

context.canvas.height = 450;
context.canvas.width = 900;

var cactus_url = "visuals/cactus_normal.png";
var image = new Image();
// image.crossOrigin = true;

image.onload = function() {
    context.drawImage(image, 150, 0, 450, 450);
};
image.src = cactus_url;

//var cactus 