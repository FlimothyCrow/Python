function changeCalculator(cost, paid) {
  changeObject = {}
  changeDue = []
  totalDue = paid - cost
  do {
    if (totalDue > 9){
      changeObject[dimes.value] = (changeObject[dimes.value]+1) || 1
      totalDue -=10;
    }
    /*
    else if (totalDue > 4) {
    changeDue.push(5);
    totalDue -= 5;
    }
    else {
    changeDue.push(1);
    totalDue -= 1;
    }
    */
  } while (totalDue > 0);
  for (element in changeDue){
    if (element === 10){

    }
  }
  return changeObject
}
