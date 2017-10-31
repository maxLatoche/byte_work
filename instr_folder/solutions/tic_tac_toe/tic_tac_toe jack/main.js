$(document).ready(function(){

var counter = 0;
$(".box").on("click", function(){

		if (counter %2 ==0){

			$(this).css({"background-color": "blue"});

			$(this).html("<p> X </p>");
			counter++;

		} else {

			$(this).css({"background-color": "green"});

			$(this).html("<p> O </p>");
			counter ++;
		}
	});

// add conditional to check who wins 

// reset the game after a win/loss or a draw

});












$(document).ready(function(){

var update_list = function(n){
	var p = parseInt(n);
	chk_lst.splice(p,1,'O');
	var idx = lst.indexOf(p);
	if (idx > -1){
		lst.splice(idx, 1);
	}
}
	
var mark_o = function(){
	var idx = lst.indexOf(num);
	if (idx > -1){
		lst.splice(idx, 1);
	}

	var i = parseInt(Math.random()*(lst.length-1));
	nid = 'B'+lst[i];
	$("#"+nid).append('O');
	update_list(nid[1]);
	check_for_win();
}

var mark_x = function(){
	v = $(this).attr('id');
	num = parseInt(v[1]);
	chk_lst.splice(num,1,'x');

	$(this).append('X');
	check_for_win();
	mark_o();
}

var next_move = function(){
	$("#B1").on("click", mark_x);
	$("#B2").on("click", mark_x);
	$("#B3").on("click", mark_x);
	$("#B4").on("click", mark_x);
	$("#B5").on("click", mark_x);
	$("#B6").on("click", mark_x);
	$("#B7").on("click", mark_x);
	$("#B8").on("click", mark_x);
	$("#B9").on("click", mark_x);

}

var check_for_win = function(){
	w = check_vals();
	debugger;
	if (w=== "true"){
		$(".gameover").show();
		$("document").stop();
	}

}

var check_vals = function(){

	if ((chk_lst[1] === chk_lst[2]) && (chk_lst[1] === chk_lst[3])){
			win = "true";
			return(win);
	}

	if ((chk_lst[4] === chk_lst[5]) && (chk_lst[4]=== chk_lst[6])){
			win = "true";
			return(win);
	}

	if ((chk_lst[7]=== chk_lst[8]) && (chk_lst[7] === chk_lst[9])){	
			win = "true";
			return(win);
	}

	if ((chk_lst[1] === chk_lst[4]) && (chk_lst[1] === chk_lst[7])){
			win = "true";
			return(win);
	}

	if ((chk_lst[2] === chk_lst[5]) && (chk_lst[2]=== chk_lst[8])){
			win = "true";
			return(win);
	}

	if ((chk_lst[3] === chk_lst[6]) && (chk_lst[3]=== chk_lst[9])){
			win = "true";
			return(win);
	}

	if ((chk_lst[1] === chk_lst[5]) && (chk_lst[1] === chk_lst[9])){
			win = "true";
			return(win);
	}
	if ((chk_lst[3] === chk_lst[5]) && (chk_lst[3] === chk_lst[7])){
			win = "true";
			return(win);
	}
} 
var lst = new Array(1,2,3,4,5,6,7,8,9);
var win =  "false";
$(".gameover").hide();
chk_lst = ['0','1','2','3','4','5','6','7','8','9'];
$("#B1").on("click", mark_x);
$("#B2").on("click", mark_x);
$("#B3").on("click", mark_x);
$("#B4").on("click", mark_x);
$("#B5").on("click", mark_x);
$("#B6").on("click", mark_x);
$("#B7").on("click", mark_x);
$("#B8").on("click", mark_x);
$("#B9").on("click", mark_x);
})





