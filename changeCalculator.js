function changeCalculator(cost, paid) {
  var totalDue = paid - cost
  var changeObject = {
    pennies: 0,
    nickels: 0,
    dimes: 0,
    quarters: 0
  };
  while (totalDue > 0){
    if (totalDue > 9){
      //console.log("change object", changeObject)
      changeObject.dimes += 1
      totalDue -=10;
    }
  }
  return changeObject
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
