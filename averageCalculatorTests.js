test('averageCalculator', function(assert) {
  var listOfInts = averageCalculator([1, 10])
  assert.equal(listOfInts, 5.5) ;
});

test('averageCalculator', function(assert) {
  var listOfInts = averageCalculator([1, 10, 100, 5, 39])
  assert.equal(listOfInts, 31) ;
});
//---------------------------------------

test('meanCalculator', function(assert){
  var listOfInts = meanCalculator([1, 2, 3, 4, 5, 6])
  assert.equal(listOfInts, "pass") ;
});

test('meanCalculator', function(assert){
  var listOfInts = meanCalculator([1, 2, 3, 4, 5])
  assert.equal(listOfInts, 3) ;
});

test('meanCalculator', function(assert){
  var listOfInts = meanCalculator([1, 2, 3, 4, 5, 6, 7, 8, 9])
  assert.equal(listOfInts, 5) ;
});
//---------------------------------------

test('modeCalculator', function(assert){
  var listOfInts = modeCalculator([1, 9, 1, 2, 9, 39, 238]) ;
  assert.deepEqual(listOfInts, [["1",2], ["9",2]])
})
