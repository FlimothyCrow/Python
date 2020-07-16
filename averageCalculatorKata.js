//Fill in the ? with a Javascript expression to set the scale for
//an image having a given original height and width so that it can exactly fit
//inside a maxdim-by-maxdim square area (touching at least two edges). *


function scaleImage(width, height, maxdim) {
  var scale = width < height? (maxdim / height):(maxdim / width);
  var scale = (maxdim / height);
  return [scale * width, scale * height];
}

//It looks like the sort of site that would require continuously designing more modular and dynamic solutions, particularly for the "collection" section of the website. I find the idea of designing an intelligent "match-by-aesthetic" program could really add an additional flavor, perhaps as a "suggestions" section. That's the kind of innovation I would very much like to be a part of!

/*
width  x scale = blank
height x scale = maxdim

1  x scale = blank
2  x scale = 8

scale = 8 / 2
scale = 4

1 x 4 = blank
2 x 4 = 8

4
8
*/
