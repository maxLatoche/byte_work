number = process.argv[2];

var isPowerOfThree = function(n){
    n = Number(n);
    for(var i = 1; i < n; i++){
        var power = Math.pow(3,i);
        if( power > n ){
            return false;
        }else if ( power === n ){
            return true;
        };
    };
};



console.log(isPowerOfThree(number));
