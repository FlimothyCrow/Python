test('scaleImage', function(assert) {
  assert.deepEqual(scaleImage(5, 10, 20), [10, 20]) ;
});

test('scaleImage', function(assert) {
  assert.deepEqual(scaleImage(3, 6, 18), [(18 / 6 * 3), 18]) ;
});

test('scaleImage', function(assert) {
  assert.deepEqual(scaleImage(6, 3, 18), [(18 / 3 * 6), 9]) ;
});
