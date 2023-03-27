function flatten(arr) {
    //Flatten nested array

    // return [].concat(...arr);
    // return [].concat.apply([], arr);
    // return arr.flat();
    return arr.reduce((prev, cur) => prev.concat(cur));
}
