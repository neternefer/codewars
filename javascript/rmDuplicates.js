function rmDuplicates(arr) {
    //Remove duplicates from array, return new array
    // return arr.filter((e, i) => arr.indexOf(e) == i);
    // return [...new Set(arr)];
    /*return arr.reduce((a, b) => {if(a.indexOf(b) < 0) a.push(b);
                            return a;
                        }, []);*/
    return arr.reduce((prev, cur) => prev.includes(cur) ? prev : prev.concat(cur), []);

}

console.log(rmDuplicates([1, 2, 2, 3, 4, 4, 4]));