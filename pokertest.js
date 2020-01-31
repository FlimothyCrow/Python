
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

// ----------------------------------------------------------
/*test('matchCounter', function(assert) {
  var handObject = makeHand(["9D", "9C", "3S", "5H"]) ;
  var valueCounted = valueCounter(handObject) ;
  assert.deepEqual(matchCounter(valueCounted), "pair of 9")
})

test('matchCounter', function(assert) {
  var handObject = makeHand(["9D", "9C", "9S", "5H"]) ;
  var valueCounted = valueCounter(handObject) ;
  assert.deepEqual(matchCounter(valueCounted), "three 9s")
})

test('matchCounter', function(assert) {
  var handObject = makeHand(["9D", "9C", "9S", "9H"]) ;
  var valueCounted = valueCounter(handObject) ;
  assert.deepEqual(matchCounter(valueCounted), "four 9s")
})

test('matchCounter', function(assert) {
  var handObject = makeHand(["3D", "5S", "3S", "5H"]) ;
  var valueCounted = valueCounter(handObject) ;
  assert.deepEqual(matchCounter(valueCounted), "two pair 3 and 5")
})
*/
