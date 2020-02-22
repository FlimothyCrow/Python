

test('makeHand', function(assert) {
  var handObject = makeHand(["9D", "3C"]) ;
  assert.equal(handObject.cards[0].value, 9) ;
  assert.equal(handObject.cards[0].suit, "D") ;
  assert.equal(handObject.cards[1].suit, "C") ;
});
// ------------------------------------------------
test('makeCard', function(assert) {
  var cardObject = makeCard("9D") ;
  assert.equal(cardObject.value, 9) ;
  assert.equal(cardObject.suit, "D") ;
});
// ------------------------------------------------
test('cardValue', function(assert) {
  var value = cardValue("AS") ;
  assert.equal(value, 14) ;
});
test('cardValue', function(assert) {
  var value = cardValue("KC") ;
  assert.equal(value, 13) ;
});
test('cardValue', function(assert) {
  var value = cardValue("QH") ;
  assert.equal(value, 12) ;
});
test('cardValue', function(assert) {
  var value = cardValue("JD") ;
  assert.equal(value, 11) ;
});
test('cardValue', function(assert) {
  var value = cardValue("10S") ;
  assert.equal(value, 10) ;
});
test('cardValue', function(assert) {
  var value = cardValue("9D") ;
  assert.equal(value, 9) ;
});
// ------------------------------------------------

test('objToArray', function(assert) {
  var handObject = makeHand(["9D", "3S"]) ;
  var valueCounted = valueCounter(handObject) ;
  var newObject = objToArray(valueCounted)
  assert.deepEqual(newObject, [[3,1], [9,1]])
})

test('objToArray', function(assert) {
  var handObject = makeHand(["9D", "AS", "10D", "9S", "3S"]) ;
  var valueCounted = valueCounter(handObject) ;
  var newObject = objToArray(valueCounted)
  assert.deepEqual(newObject, [[3,1], [9,2], [10,1], [14,1] ])
})

test('objToArray', function(assert) {
  var handObject = makeHand(["9D", "9C", "3S", "5H"]) ;
  var valueCounted = valueCounter(handObject) ;
  var newObject = objToArray(valueCounted)
  assert.deepEqual(newObject, [[3,1], [5,1], [9,2]])
})

// ----------------------------------------------------------
test('reorderArray', function(assert) {
  var ordered = reorderArray([[5, 1], [3, 6]])
  assert.deepEqual(ordered, [[3,6], [5,1]])
})

test('reorderArray', function(assert) {
  var ordered = reorderArray([[5, 1], [3, 6], [10,10], [3, 25]])
  assert.deepEqual(ordered, [[3,25], [10, 10], [3,6], [5,1]])
})
// ----------------------------------------------------------
test('valueCounter', function(assert) {
  var handObject = makeHand(["9D", "9C", "9S"]) ;
  assert.deepEqual(valueCounter(handObject), {9:3})
})

test('valueCounter', function(assert) {
  var handObject = makeHand(["9D", "9C", "2S", "AS"]) ;
  assert.deepEqual(valueCounter(handObject), {"14": 1, "2": 1, "9": 2})
})

// ----------------------------------------------------------
test('matchCounter0', function(assert) {
  var matchCounted = [[9,2], [3,1], [5,1]]
  assert.equal(matchCounter(matchCounted), "pair of 9")
})

test('matchCounter1', function(assert) {
  var matchCounted = [[9,3], [5,1]]
  assert.equal(matchCounter(matchCounted), "three 9")
})

test('matchCounter3', function(assert) {
  var matchCounted = [[9,2], [6,3]]
  assert.equal(matchCounter(matchCounted), "full house 6 9")
})

test('matchCounter4', function(assert) {
  var matchCounted = [[9,2], [6,2]]
  assert.equal(matchCounter(matchCounted), "two pair 9 6")
})

test('matchCounter2', function(assert) {
  var matchCounted = [[9,4]]
  assert.equal(matchCounter(matchCounted), "four 9")
})
// ----------------------------------------------------------
test('suitCounter0', function(assert){
  var handObject = makeHand(["9D", "3D", "2D", "KD", "10D"]) ;
  var suitCounted = suitCounter(handObject) ;
  assert.equal(suitCounted, "D")
})

test('suitCounter0', function(assert){
  var handObject = makeHand(["9S", "3S", "2S", "KS", "10S"]) ;
  var suitCounted = suitCounter(handObject) ;
  assert.equal(suitCounted, "S")
})

test('suitCounter0', function(assert){
  var handObject = makeHand(["9D", "3S", "2S", "KS", "10S"]) ;
  var suitCounted = suitCounter(handObject) ;
  assert.equal(suitCounted, undefined)
})
// ----------------------------------------------------------
test('highCard', function(assert) {
  var hand = ["9D", "3S", "2S", "KS", "10S"]
  var highCarded = highCard(hand)
  assert.equal(highCarded, 13)
})
// ----------------------------------------------------------
test('converter0', function(assert){
  var hand = ["9D", "AS", "10D", "9S", "3S"]
  var converted = converter(hand)
  assert.deepEqual(converted, [[3,1], [9,2], [10,1], [14,1]])
})
// ----------------------------------------------------------
test('controller0', function(assert){
  var hand = ["9D", "AS", "10D", "9S", "3S"]
  var controlled = controller(hand)
  assert.equal(controlled, "pair of 9")
})

test('controller0', function(assert){
  var hand = ["9S", "AS", "10S", "QS", "3S"]
  var controlled = controller(hand)
  assert.equal(controlled, "S")
})

test('controller0', function(assert){
  var hand = ["9S", "AS", "10S", "QH", "3S"]
  var controlled = controller(hand)
  assert.equal(controlled, 14)
})
// ----------------------------------------------------------

test('mergeSort0', function(assert){
  var unsorted = [5, 3, 4, 1]
  var sorted = mergeSort(unsorted)
  assert.equal(sorted, [1, 3, 4, 5])
})
