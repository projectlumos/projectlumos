$(document).ready(function() {
    $(".changeDesc").click(function(){

        var desc = $(this).data("desc");
        var relatedDomains = $(this).data("related-technologies");
        var relatedTechnologies = $(this).data("related-technologies");
        var centralActivity = $(this).data("centralActivity");
        var is_video = $(this).data("media_type");
        var term = $(this).text()
        if (is_video){
            //change youtube url 
            //display youtube widget
        }

        $("#descHeader").text(term);
        $("#descBox").text(desc);
        console.log("type of related domains", typeof(relatedDomains));
        console.log("desc", desc);
        console.log("related domains ", relatedDomains);
        console.log("related technologies", relatedTechnologies);
    }); //changing the desc

    var function change_modal_content(input_term){
        console.log("changing modal data");
        console.log(input_term);
    };

    $("#search-btn").click(function(){
        var search_term = $("#search-btn").val().trim()
        console.log(search_term);
        if (search_term){
            console.log(searching wiki);
            $("wikki").modal("hide");
            change_modal_content(term);
        }
    });//wiki search button
});//document ready