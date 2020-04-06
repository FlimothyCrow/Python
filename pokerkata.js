
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

function makeHand(listOfCards) { // old
  var handObject = []
  for (card of listOfCards) {
    handObject.push(makeCard(card))
  }
  return { cards : handObject }
  }

function cardsToHand(listOfCards){ // new dense
  return listOfCards.map(makeCard)
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
    return [parseInt(key), hand[key]];
});
  return arrayOfArrays
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
function highCard(arrayOfStrings) {
  values = []
  for (string in arrayOfStrings) {
    values.push(cardValue(arrayOfStrings[string]))
  }
  descendingArray = values.sort(function(a, b){return b-a});
  return values[0]
}
// ----------------------------------------------------------
function converter(arrayOfStrings) {
  var handObject = makeHand(arrayOfStrings)
  var objectOfMatches = valueCounter(handObject)
  var arrayOfMatches = objToArray(objectOfMatches)
  return arrayOfMatches
}
// makeHand (arrayOfStrings > handObject)
// valueCounter (handObject > objectOfMatches)
// objToArray (objectOfMatches > arrayOfMatches)
// ----------------------------------------------------------
function controller(arrayOfStrings) {
  handObject = makeHand(arrayOfStrings)
  arrayOfMatches = converter(arrayOfStrings)
  if (matchCounter(arrayOfMatches)) {
    return matchCounter(arrayOfMatches)
  }
  else if (suitCounter(handObject)) {
    return suitCounter(handObject)
  }
  else {
    return highCard(arrayOfStrings)
  }
}
// don't forget to defined function highCard
// filled out applications
// ----------------------------------------------------------

function mergeSort(array){
  mid = array.length / 2
  left = []
  right = []
  for (integer of array){
    if (array.indexOf(integer) < mid){
      left.push(integer)
    }
    else {
      right.push(integer)
    }
  }
  return right
}
// applications
// ----------------------------------------------------------

function addSumN(listOfInts, start){
  return listOfInts.reduce((sum, value) => sum + value, 100)
}
