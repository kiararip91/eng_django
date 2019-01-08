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

    function playAudio(){
        var englishText = english.text();
        var encodedText = btoa(englishText);
        var urlEngVoice = "http://voice2.reverso.net/RestPronunciation.svc/v1/output=json/GetVoiceStream/voiceName=Heather22k?inputText=" + encodedText;
        var audio = document.getElementById('myAudioElement') || new Audio();
        audio.src = urlEngVoice;
        audio.play();
    }

    $(function(){
        playAudio();
    });

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
        var rightAnswer = false;

        correctAlternatives.forEach(function(correctAlternative) {
        	if(correctAlternative.trim().toLowerCase() == inputTranslationVal.trim().toLowerCase()){
        		console.log("ESATTA");
        		rightAnswer = true;
        		updateWordScore(rowVal, correctScoreVal, wrongScoreVal, 1);
                handleCorrectAnswer();
        		return;
        	}
        });

        if(!rightAnswer){
        	console.log("SBAGLIATA");
        	updateWordScore(rowVal, correctScoreVal, wrongScoreVal, 0);
            handleWrongAnswer();
        }

    });

    $('.audio-btn').on('click',function(){
        playAudio();
    });

    $(".user-input").on('input',function(e){
        $(".user-input").css('color', 'black');
    });


})(jQuery);

function updateWordScore(id, scoreWrong, scoreRight, isCorrect){

	$.ajax({
        url: "http://127.0.0.1:8000/eng/update/"+ id + "/" + scoreRight + "/" + scoreWrong + "/" + isCorrect,
        success: function (response) {
            console.log("success")
      },
      error: function (xhr, ajaxOptions, thrownError) {
            console.log("error")
      }
    }).done(function() {
       console.log("Done");
    });
}

function handleWrongAnswer(){
    $(".user-input").css('color', 'red');

}

function handleCorrectAnswer(){
    $(".user-input").css('color', 'green');
    $(".content-to-hide-correct").hide();
    $(".content-to-show-correct").show();
}
