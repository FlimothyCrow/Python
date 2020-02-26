test('changeCalculator', function(assert) {
  var cost = 100 // one dollar
  var paid = 300 // three dollars
  var changeDue = changeCalculator(cost, paid) ;
  assert.equal(changeDue, 40) ;
});
