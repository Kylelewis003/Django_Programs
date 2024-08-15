$(document).ready(function(){
    $('#ajax-form').submit(function(event){
        event.preventDefault();
        var inputdata = $('#input-data').val();
        $.ajax({
            type : 'POST',
            url : '/ajax_submit/',
            data : {'input_data' : inputdata},
            success : function(response){
                $('#result').text(response.message);
            },
        });
    });
});