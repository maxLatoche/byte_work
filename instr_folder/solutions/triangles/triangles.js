number = process.argv[2];

//var triangles = function (num){
//    for(var i = 0; i < num; i++){
//        str = "";
//        for(var j = 0; j < i+1; j++){
//            str += "^";    
//        };
//        console.log(String.format(str, number));
//    };
//};
//
//triangles(number);


var triangles2 = function (num){
    var totalWidth = 2 * num - 1;
    var str = new Array(totalWidth + 1);
    for(var i = 0; i < num; i++){
        str.fill(" ");
        str.fill("^", (totalWidth/2) - i, (totalWidth/2) + i + 1);
        console.log(str.join(""));
    };
};

triangles2(number);
