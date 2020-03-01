test('changeCalculator0', function(assert) {
  var cost = 280 // one dollar
  var paid = 300 // three dollars
  var changeDue = changeCalculator(cost, paid) ;
  assert.equal(changeDue.dimes, 2) ; //dimes
});

test('changeCalculator1', function(assert) {
  var cost = 100 // one dollar
  var paid = 105 // three dollars
  var changeDue = changeCalculator(cost, paid) ;
  assert.equal(changeDue.nickels, 1) ;
});

test('changeCalculator2', function(assert) {
  var cost = 7 // one dollar
  var paid = 9 // three dollars
  var changeDue = changeCalculator(cost, paid) ;
  assert.equal(changeDue.pennies, 2) ;
});

test('changeCalculator3', function(assert) {
  var cost = 100 // one dollar
  var paid = 180 // three dollars
  var changeDue = changeCalculator(cost, paid) ;
  assert.equal(changeDue.quarters, 3) ;
});

test('changeCalculator3', function(assert) {
  var cost = 100 // one dollar
  var paid = 500 // three dollars
  var changeDue = changeCalculator(cost, paid) ;
  assert.equal(changeDue.dollars, 4) ;
});
