
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
function objToArray(hand) {
  var arrayOfArrays = Object.keys(hand).map(function(key) {
    return [key, hand[key]];
});
}
// ----------------------------------------------------------
function matchCounter(matches) {
  for (var i = 0; i < matches.length; i++) {
    return "true"
  }
}
// studied sortMerge and applications
