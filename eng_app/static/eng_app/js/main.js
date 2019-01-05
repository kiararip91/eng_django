(function ($) {
    "use strict";

    $('.content-to-show').hide();
    $('.content-to-show-correct').hide();

    var english = $('.english');
    var sentence = $('.sentence');
    var inputTranslation = $('input[name="input-translation"]'); 
    var correctTranslation = $('input[name="correct-translation"]'); 

    var correctScore = $('input[name="correct-score"]'); 
    var wrongScore = $('input[name="wrong-score"]'); 
    var row = $('input[name="row"]'); 

    $('.skip-btn').on('click',function(){
        location.reload();
    });

    $('.show-solution-btn').on('click',function(){
        $('.content-to-hide').hide();
        $('.content-to-show').show();
    });
    
    
    $('.container100-div-btn').on('click',function(){
    	
    	var inputTranslationVal = inputTranslation.val();
    	var correctTranslationVal = correctTranslation.val();

    	var correctScoreVal = parseInt(correctScore.val());
    	var wrongScoreVal = parseInt(wrongScore.val());

    	var rowVal = row.val();

        console.log("validating... " + inputTranslationVal);
        console.log("against... " + correctTranslationVal);

        var correctAlternatives = correctTranslationVal.split(", ");
        var rightAnwer = false;

        correctAlternatives.forEach(function(correctAlternative) {
        	if(correctAlternative.trim().toLowerCase() == inputTranslationVal.trim().toLowerCase()){
        		console.log("ESATTA");
        		rightAnwer = true;
        		updateCorrectWordScore(rowVal, correctScoreVal);
                handleCorrectAnswer();
        		return;
        	}
        });

        if(!rightAnwer){
        	console.log("SBAGLIATA");
        	updateWrongWordScore(rowVal, wrongScoreVal);
            handleWrongAnswer();
        }
        
    });

    $('.audio-btn').on('click',function(){
    	var englishText = english.text();
    	var encodedText = btoa(englishText);
    	var urlEngVoice = "http://voice2.reverso.net/RestPronunciation.svc/v1/output=json/GetVoiceStream/voiceName=Heather22k?inputText=" + encodedText;
    	var audio = document.getElementById('myAudioElement') || new Audio();
		audio.src = urlEngVoice;
		audio.play();
    });

    $(".user-input").on('input',function(e){
        $(".user-input").css('color', 'black');
    });


})(jQuery);

function updateCorrectWordScore(row, oldScore){
	position = "TODO"; //cell of correct score
	value = oldScore + 1;
	updateCell(position, value, next = true);
}

function updateWrongWordScore(row, oldScore){
	position = "TODO"; //cell of wrong score
	value = oldScore + 1;
	updateCell(position, value, next = false);
}

function updateCell(position, value, goToNextWord){
	console.log("Updating position " + position + " with score " + value);

    if(goToNextWord){
        console.log("Correct, next one..");
    }else{
        console.log("Wrong answer, try again");
    }
	/*$.ajax({
  		type: "GET",
  		url: "www.google.com"//, TODO UPDATE
  		//data: { param: text}
	}).done(function( o ) {
   		location.reload();
	});*/
	//location.reload();
}

function handleWrongAnswer(){
    $(".user-input").css('color', 'red');

}

function handleCorrectAnswer(){
    $(".user-input").css('color', 'green');
    $(".content-to-hide-correct").hide();
    $(".content-to-show-correct").show();
}