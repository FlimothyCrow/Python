
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
  var listOfValues = [] ;
  for (card of hand.cards) {
    listOfValues.push([card.value])
  return listOfValues
  }
}
// ----------------------------------------------------------
function objToArray(hand) {
  var arrayOfArrays = Object.keys(hand).map(function(key) {
    return [key, hand[key]];
});
}
// ----------------------------------------------------------
function reorderArray(hand) {
  var sorted = hand.sort((a,b)=>{
    if (a[1] < b[1]) return 1;
    else if (b[1] < a[1]) return -1;
    else return 0;
  });
  return sorted
}
// ----------------------------------------------------------
function matchCounter(matches) {
  reorderedMatches = reorderArray(matches)
  for (var i = 0; i < reorderedMatches.length; i++) {
    if (reorderedMatches[i][1] === 3) {
      if (reorderedMatches[i + 1][1] === 2) {
        return "full house " + reorderedMatches[i][0] + " " + reorderedMatches[i+1][0]
      }
      else {
        return "three " + reorderedMatches[i][0]
      }
    }
    else if (reorderedMatches[i][1] === 2) {
      if (reorderedMatches[i+1][1] === 2) {
        return "two pair " + reorderedMatches[i][0] + " " + reorderedMatches[i+1][0]
      }
      else {
        return "pair of " + reorderedMatches[i][0]
      }
    }
    else if (reorderedMatches[i][1] === 4) {
      return "four " + reorderedMatches[i][0]
    }
  }
}
// ----------------------------------------------------------
function suitCounter(hand) {
  var listOfValues = [] ;
  for (card of hand.cards) {
    if (!listOfValues.includes(card.suit)) {
      listOfValues.push(card.suit)
    }
  }
  if (listOfValues.length === 1) {
    return listOfValues[0]
  }
}
// ----------------------------------------------------------

function controller(hand) {
  var handObject = makeHand(hand)
  var handArray = objToArray(handObject)
  if (matchCounter(handArray)) {
    return "true"
  }
}
