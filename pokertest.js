
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
  assert.deepEqual(valueCounter(handObject), { "14": 1, "2": 1, "9": 2})
})
// ----------------------------------------------------------
test('matchCounter', function(assert) {
  var handObject = makeHand(["9D", "9C", "3S", "5H"]) ;
  var valueCounted = valueCounter(handObject) ;
  assert.deepEqual(matchCounter(valueCounted), "pair of 9")
})
/*
test('isMatch', function(assert) {
  var handObject = makeHand(["9D", "9C", "2S", "3H", "5S"]) ;
  assert.equal(isMatch(handObject), "pair of 9") ;
});

test('isMatch', function(assert) {
  var handObject = makeHand(["9D", "9C", "9S", "3H", "5S"]) ;
  assert.equal(isMatch(handObject), "three of 9") ;
});

test('isMatch', function(assert) {
  var handObject = makeHand(["9D", "9C", "9S", "9H", "5S"]) ;
  assert.equal(isMatch(handObject), "four of 9") ;
});

test('isMatch', function(assert) {
  var handObject = makeHand(["9D", "9C", "5S", "3H", "5S"]) ;
  assert.equal(isMatch(handObject), "two pair 9 and 5") ;
});
*/
// ------------------------------------------------
