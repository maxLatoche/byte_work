$(document).ready(function() {
    initCharacters();
    $('#tatooine').on('click', tatooineClicked);
    $('#falcon').on('click', falconClicked);
    // $('#death').on('click', deathClicked);
    // $('#wing').on('click', wingClicked);
});

function initCharacters(){
    jedi = [
        "Luke Skywalker",
        "Obi Wan Kenobi"
    ];
    millenium = [
        "Han Solo",
        "Chewbacca"
    ];
    royalty = "Leia Organa";
    darkside = "Darth Vader";

    //state variables
    foundLuke = false;
    leftTatooine = false;
    foundLeia = false;
    darthAppeared = false;
    escapedDeathStar = false;
    deathStarDestroyed = false;
}

function tatooineClicked() {
    if (!foundLuke){
        findLuke();
        foundLuke = true;
    }
}

function findLuke() {
    for (var i = 0; i < jedi.length; i++) {
        $('#tatooine').append("<div class='jedi'>" + jedi[i] + "<div>");
    }
}

function falconClicked(){
    if(!leftTatooine){
        leaveTatooine();
        leftTatooine = true;
    }
    // }else if(darthAppeared){
    //     retreat();
    //     escapedDeathStar = true;
    // }
}

function leaveTatooine() {
            // Remove Obi Wan and Luke from Tatooine
        // Put Obi Wan, Luke, Han, and Chewy on the Millenium Falcon
        // This will be easier if you combine these two groups using the already defined "heroes" variable up top
        // Give each hero element their own div
        // Give all the newly created divs a class called "heroes"
        // Append all the new heroes divs to the Millenium Falcon

        // $('.jedi').remove();
        // var heroes = jedi.concat(millenium);
        // for (var i = 0; i < heroes.length; i++) {
        //     $('#falcon').append("<div class='heroes'>" + heroes[i] + "<div>");
        // }

        for (var i = 0; i < millenium.length; i++) {
            $('#falcon').append("<div class='heroes'>" + millenium[i] + "<div>");
        }

        $('#falcon').append($('.jedi'));
        debugger;
        $("#falcon")

}

//////////////////////////////////\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

// (function start(){ //WRAP SHIT IN IIFE

// //characters
//     var jedi = [
//         "Luke Skywalker",
//         "Obi Wan Kenobi"
//     ];

//     var millenium = [
//         "Han Solo",
//         "Chewbacca"
//     ];

//     var royalty = "Leia Organa";

//     var darkside = "Darth Vader";
// //combine characters for falcon
//     var heroes = jedi.concat(millenium);

//     var time = "arrive";
//     var escape = false;

//     ///////////////////////// Making Your Story /////////////////////////
//     var tatooine = document.getElementById("tatooine");
//     var falcon = document.getElementById("falcon");
//     var deathStar = document.getElementById("death");
//     var xwing = document.getElementById("wing");

//     var findLuke = function(){
//         //make obi wan and luke as an unordered list in tatooine

//         for (var i = 0; i < jedi.length; i++){
//             var div = document.createElement("div");
//             div.innerHTML = jedi[i];
//             div.setAttribute("class", "jedi");
//             tatooine.appendChild(div);
//         }
//     };

//     var leaveTatooine = function(){
//         // add list together, then use for loop
//         // make obi wan, luke, han, and chewy all appear in the millenium falcon
//         // remove luke and obi wan from tatooine
//         var remove = document.getElementsByClassName("jedi");
//         remove_length = remove.length
//         for (var i = 0; i < remove_length; i++){
//             tatooine.removeChild(remove[0])
//         };

//         for (var i = 0; i<heroes.length; i++){
//             var div = document.createElement("div");
//             div.innerHTML = heroes[i];
//             div.setAttribute("class", "heroes");
//             falcon.appendChild(div);
//         };
//     };

//     var findLeia = function(){
//         //remove everybody from the falcon
//         //add them all to the death star
//         //add leia to the death star

//         var remove = document.getElementsByClassName("heroes");
//         remove_length = remove.length
//         for (var i = 0; i<remove_length; i++){
//             falcon.removeChild(remove[0]);
//         };

//         heroes.push(royalty);

//         for (var i=0; i<heroes.length; i++){
//             var div = document.createElement("div");
//             div.innerHTML = heroes[i];
//             div.setAttribute("class", "heroes");
//             deathStar.appendChild(div);
//         };
//     };

//     var vaderAndObi = function(){
//         //append vader to the death star
//         //remove Obi Wan Kenobi

//         var good = document.getElementsByClassName("heroes");

//         for (var i = 0; i<good.length; i++){
//             if (good[i].innerHTML === "Obi Wan Kenobi"){
//                 deathStar.removeChild(good[i])
//                 var div = document.createElement("div");
//                 div.setAttribute("class", "vader");
//                 div.innerHTML = darkside;
//                 deathStar.appendChild(div);

//                 //Remove Obi Way from Heroes Array
//                 var ind = heroes.indexOf("Obi Wan Kenobi");
//                 heroes.splice(ind, 1);
//             };
//         };
//     };

//     var retreat = function(){
//         //delete the heroes from death star
//         //add heroes to falcon

//         var good = document.getElementsByClassName("heroes");
//         var party = good.length;

//         for (var i=0; i<party; i++){
//             deathStar.removeChild(good[0]);
//         };

//         for(var i=0; i<heroes.length; i++){
//             var div = document.createElement("div");
//             div.innerHTML = heroes[i];
//             div.setAttribute("class", "heroes");
//             falcon.appendChild(div);
//         }
//     };

//     var battle = function(){
//         //Delete Leia from the falcon element
//         //Delete Leia from the heroes list
//         //Delete Luke from falcon
//         //Append Luke to X-wing

//         var depart = document.getElementsByClassName("heroes");

//         for(var i=0; i<depart.length; i++){
//             if (depart[i].innerHTML === "Luke Skywalker" || depart[i].innerHTML === "Leia Organa"){
//                 falcon.removeChild(depart[i]);
//                 i-=1
//             };
//         };

//         var div = document.createElement("div");
//         div.innerHTML = "Luke Skywalker";
//         xwing.appendChild(div);
//         deathStar.remove()

//     };


// ////////////////////////////// CLICK EVENTS /////////////////////////////
//     tatooine.addEventListener('click', findLuke);
//     falcon.addEventListener('click', function(){
//         if (escape === true){
//             retreat();
//         } else {
//             leaveTatooine();
//         };
//     });
//     deathStar.addEventListener("click", function(){
//         if (time === "arrive"){
//             findLeia();
//             time = "depart";
//         } else if (time === "depart"){
//             vaderAndObi();
//             escape = true;
//         };
//     });
//     xwing.addEventListener("click", battle);


// }())//END OF IIFE
