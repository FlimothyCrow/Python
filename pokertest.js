
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
test('valueCounter', function(assert) {
  var handObject = makeHand(["9D", "9C", "9S"]) ;
  assert.deepEqual(valueCounter(handObject), {9:3})
})

test('valueCounter', function(assert) {
  var handObject = makeHand(["9D", "9C", "2S", "AS"]) ;
  assert.deepEqual(valueCounter(handObject), {"14": 1, "2": 1, "9": 2})
})
// ----------------------------------------------------------
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

test('matchCounter', function(assert) {
  var matchCounted = [[9,2], [3,1], [5,1]]
  assert.equal(matchCounter(matchCounted), "pair of 9")
})
/*
test('matchCounter', function(assert) {
  var matchCounted = [[9,3], [5,1]]
  assert.equal(matchCounter(matchCounted), "three 9")
})

test('matchCounter', function(assert) {
  var matchCounted = [[9,4]]
  assert.equal(matchCounter(matchCounted), "four 9")
})
*/
test('matchCounter', function(assert) {
  var matchCounted = [[9,2], [6,3]]
  assert.equal(matchCounter(matchCounted), "full house 9 6")
})
