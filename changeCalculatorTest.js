test('changeCalculator', function(assert) {
  var cost = 1
  var paid = 3
  var changeDue = changeCalculator(cost, paid) ;
  assert.equal(changeDue, "true") ;
});
