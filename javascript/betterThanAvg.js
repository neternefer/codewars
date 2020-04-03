//You receive an array with your peers' test scores. 
//Now calculate the average and compare your score!
//Return True if you're better, else False!
function betterThanAverage(classPoints, yourPoints) {
    // Your code here
    classPoints.push(yourPoints)
    let sum = classPoints.reduce((c,p) => c + p);
    return yourPoints > parseInt(sum / classPoints.length);
    
  }