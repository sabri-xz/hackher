const context = document.querySelector("canvas").getContext("2d");

// context.canvas.height = 450;
// context.canvas.width = 900;

var cactus_url = "https://raw.github.com/sasana-uwu/hackher/blob/main/visuals/cactus_normal.png";
var image = new Image();
image.src = cactus_url;
// image.crossOrigin = true;

image.onload = function() {
    context.drawImage(
        image,
        0,
        0,
        image.width,
        image.height,
        0,
        0,
        canvas.width,
        canvas.height
    );
};