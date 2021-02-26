(function(){
    function eliminaArtigo(url, id){
        var token = $("input[name=csrfmiddlewaretoken]").val();
        $.ajax({
            "content-type": 'application/json; charset=utf-8',
            "data-type": "json",
            "url" : url,
            "method": "delete",
            "data": jsonify({
                'csrf_token': token,
                'id':id
            }),
            success: function(e){
                alert("Eliminated");
            },
            error : function(e){
                alert("Error");
            }
        });
    }
}
);