
      // This is what a simple unit test looks like:

  function cardValue(card) {
    if (card[0] === "A") {
        return 14
    }
    else if (card[0] === "K") {
        return 13
    }
    else if (card[0] === "Q") {
        return 12
    }
    else if (card[0] === "J") {
        return 11
    }
    else return parseInt(card.slice(0, -1))
  }
// ----------------------------------------------------------

  function makeCard(string) {
    return { value : cardValue(string), suit : string.charAt(string.length-1)  }
  }
// ----------------------------------------------------------

  function makeHand(listOfCards) {
    var handObject = []
    for (card of listOfCards) {
      handObject.push(makeCard(card))
    }
    return { cards : handObject }
    }
// ----------------------------------------------------------
function valueCounter(hand) {
  var listOfValues = {} ;
  for (card of hand.cards) {
    listOfValues[card.value] = (listOfValues[card.value]+1) || 1 ;
    }
  return listOfValues
}
// ----------------------------------------------------------
function matchCounter(valueCounted) {
  for (object of Object.entries(valueCounted)) {
    if (object[1] === 2) {
      return "pair of " + object[0]
    }
    else if (object[1] === 3) {
      return "three " + object[0] + "s"
    }
    else if (object[1] === 4) {
      return "four " + object[0] + "s"
    }
  }
}
// ----------------------------------------------------------
function objToArray(hand) {
  var arrayOfArrays = Object.keys(hand).map(function(key) {
    return [key, hand[key]];
});
}
    //if ({value} === 2) {
      //return "string"



/*
  for (var property in object) {
    if (object.hasOwnProperty(property)) {
      // Do things here
    }
  }
*/
