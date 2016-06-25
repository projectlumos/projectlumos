console.log('apples');

$document.ready(function() {
    $(".changeDesc").click(function(){
        var desc = $(this).data("desc");
        var relatedDomains = $(this).data("related-technologies");
        var relatedTechnologies = $(this).data("related-technologies");
        console.log(desc);
        console.log(relatedDomains);
        console.log(relatedTechnologies);
    })
});//document ready