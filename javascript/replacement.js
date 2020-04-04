//Find the minimal possible sequence after performing 
//a valid replacement (can't replace the number with itself
//and sorting the sequence.
function replacement(a){
    a.sort((a, b) =>  a - b);
    a.pop() === 1 ? a.push(2) : a.unshift(1);
    return a;
}
    
     