/*
function changeCalculator(cost, paid) {
  var totalDue = paid - cost
  var changeObject = {
    pennies: 0,
    nickels: 0,
    dimes: 0,
    quarters: 0,
    dollars: 0
  };
  while (totalDue > 0){
    if (totalDue > 99) {
    changeObject.dollars += 1
    console.log(changeObject)
    totalDue -= 100;
    }
    else if (totalDue > 24) {
    changeObject.quarters += 1
    totalDue -= 25;
    }
    else if (totalDue > 9){
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

function changePrinter(changeObject){
  console.log("Your change is:")
  console.log(changeObject.dollars + "dollars")
}
var change = changeCalculator(500, 375)
changePrinter(change)
*/


function printStuff(input){
  console.log(input)
  console.log(input + " ")
  console.log(input + "efefef ")
}

printStuff("steve")
