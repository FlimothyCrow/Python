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
      totalDue -= 10;
    }
    else if (totalDue > 4) {
    changeObject.nickels += 1
    totalDue -= 5;
    }
    else if (totalDue > 0) {
    changeObject.pennies += 1
    totalDue -= 1;
    }
  }
  return changeObject
}
/*

else {
changeDue.push(1);
totalDue -= 1;
}
*/
