
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
function reorderArray(hand) {
  sorted = hand.sort(function(a, b)
  {return b[1] > a[1]});
}


// ----------------------------------------------------------
function matchCounter(matches) {
  for (var i = 0; i < matches.length; i++) {
    if (matches[i][1] === 2) {
      if (matches[i + 1][1] === 3) {
        return "full house " + matches[i][0] + " " + matches[i+1][0]
      }
      else return "pair of " + matches[i][0]
      }
    else if (matches[i][1] === 3) {
      return "three " + matches[i][0]
    }
    else if (matches[i][1] === 4) {
      return "four " + matches[i][0]
    }
    }
}
// helper function to descend-order the objToArray results?
// or just make objToArray do it??
// studied sort > compare array[arrays]
