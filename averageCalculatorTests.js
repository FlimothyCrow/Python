test('averageCalculator', function(assert) {
  var listOfInts = averageCalculator([1, 10])
  assert.equal(listOfInts, 5.5) ;
});

test('averageCalculator', function(assert) {
  var listOfInts = averageCalculator([1, 10, 100, 5, 39])
  assert.equal(listOfInts, 31) ;
});
