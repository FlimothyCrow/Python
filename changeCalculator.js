function changeCalculator(cost, paid) {
  changeDue = []
  totalDue = paid - cost
  do {
    if (totalDue > 9){
      changeDue.push(10);
      totalDue -=10;
    }
    else if (totalDue > 4) {
    changeDue.push(5);
    totalDue -= 5;
    }
    else {
    changeDue.push(1);
    totalDue -= 1;
    }
  } while (totalDue > 4);
  return changeDue.length
}
