$(document).ready(function() {
    $('#speech-button').on('click', function() {
        var text = $('#text-input').val();
        if (text.trim() !== '') {
            var speechUrl = 'https://translate.google.com/translate_tts?ie=UTF-8&q=' + encodeURIComponent(text) + '&tl=en&client=tw-ob';
            var audio = new Audio(speechUrl);
            audio.play();
        }
    });
});
