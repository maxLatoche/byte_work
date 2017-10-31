$(document).ready(function(){
    initCharacters();
    $("#tatooine").click(tatooineClicked);
    $("#falcon").click(falconClicked);
    $("#death").click(deathClicked);
    $("#wing").click(wingClicked);
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

function tatooineClicked(){
    if(!foundLuke){
        findLuke();
        foundLuke = true;
    }
}

function falconClicked(){
    if(!leftTatooine){
        leaveTatooine();
        leftTatooine = true;
    }else if(darthAppeared){
        retreat();
        escapedDeathStar = true;
    }
}

function deathClicked(){
    if(leftTatooine && !foundLeia){
        findLeia();
        foundLeia = true;
    } else if (foundLeia && !darthAppeared){
        vaderAndObi()
        darthAppeared = true;        
    }
}

function wingClicked(){
    if(escapedDeathStar && !deathStarDestroyed){
        battle();
        deathStarDestroyed = true;
    }
}

function findLuke(){
    for(i=0; i < jedi.length; i++){
        $("#tatooine").append("<div class='jedi'>" + jedi[i] + "<div>");
    }   
}

function leaveTatooine(){
    for(i=0; i < millenium.length; i++){
        $("#falcon").append("<div>" + millenium[i] + "</div>");
    }

    $("#falcon").append(
        $(".jedi")        
    );
    $("#falcon > div").addClass("heroes");
}

function findLeia(){
    $("#death").append(
        "<div class='heroes royalty'>"+ royalty + "</div>"
    );
    $("#death").append( 
        $("#falcon > .heroes")  
    );
}

function vaderAndObi(){
    $(".jedi:contains('Obi Wan')").remove();
    $("#death").append("<div class='vader'>"+ darkside + "</div>");
}

function retreat(){
    $("#falcon").append(
        $(".heroes")
    );
}

function battle(){
    $("#falcon > .royalty").remove();
    $("#wing").append(
        $("#falcon > .jedi")        
    );
    $("#tie").append(
        $(".vader")
    );
    $("#death").remove();
}
