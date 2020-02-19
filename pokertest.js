

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
  assert.equal(objToArray(valueCounted, [[9,1], [3,1]]))
})

test('objToArray', function(assert) {
  var handObject = makeHand(["9D", "AS", "10D", "9S", "3S"]) ;
  var valueCounted = valueCounter(handObject) ;
  assert.equal(objToArray(valueCounted, [[9,2], [14,1], [10,1], [3,1]]))
})

test('objToArray', function(assert) {
  var handObject = makeHand(["9D", "9C", "3S", "5H"]) ;
  var valueCounted = valueCounter(handObject) ;
  assert.equal(objToArray(valueCounted, [[9,2], [3,1], [5,1]]))
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
  var handObject = makeHand(["9D"]) ;
  assert.deepEqual(valueCounter(handObject), [[9]])
})
/*
test('valueCounter', function(assert) {
  var handObject = makeHand(["9D", "9C", "2S", "AS"]) ;
  assert.deepEqual(valueCounter(handObject), [[14,1], [9,2], [2,1]])
})
*/
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
/*
test('controller0', function(assert){
  var hand = ["9D", "AS", "10D", "9S", "3S"]
  var controlled = controller(hand)
  assert.equal(controlled, "pair of 9")
})
*/
