function changeCalculator(cost, paid) {
  changeDue = []
  totalDue = paid - cost
  do {
    changeDue.push(5);
    totalDue -= 5
    totalDue++;
  } while (totalDue > 4);
  return changeDue.length
}
