test('changeCalculator', function(assert) {
  var cost = 1.75
  var paid = 3
  var changeDue = changeCalculator(cost, paid) ;
  assert.equal(changeDue, [[1, dollar], [1, quarter]]) ;
});
