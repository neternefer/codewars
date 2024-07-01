function flatten(...args) {
    
    args.forEach((e) => {
        while(e instanceof Array) {
            e.flat();
        }
    })
    console.log(args)
    
}

flatten(1, [2, 3], 4, 5, [6, [7]])