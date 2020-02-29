test('changeCalculator0', function(assert) {
  var cost = 100 // one dollar
  var paid = 300 // three dollars
  var changeDue = changeCalculator(cost, paid) ;
  assert.equal(changeDue.dimes, 20) ; //dimes
});
/*
test('changeCalculator1', function(assert) {
  var cost = 100 // one dollar
  var paid = 200 // three dollars
  var changeDue = changeCalculator(cost, paid) ;
  assert.equal(changeDue, 10) ;
});

test('changeCalculator2', function(assert) {
  var cost = 7 // one dollar
  var paid = 9 // three dollars
  var changeDue = changeCalculator(cost, paid) ;
  assert.equal(changeDue, 2) ;
});
*/
