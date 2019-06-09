$(document).ready(function() {

    // čez use naštimaš draggable
    $(".drag-list li").each(function(index) {
        $(this).fitText()
        $(this).draggable({
            cursor: "grabbing",
            containment: "#contain-draggable",
            stack: '.drag-words',
            revert: true,
            revertDuration: "100"
        })
    })

    // čez use naštimaš droppable
    $(".drop-sentence__target").each(function(index) {
        $(this).droppable({
            accept: ".drag-words",
            hoverClass: 'drop-sentence--hovered', // Tukej samo nardiš svojo classo (drugač je tudi ui-dropable-hover al neki tazga)
            drop: handleCardDrop // funkcija k handlea kaj se zgodi k se sproži drop
        })
    })
})

function handleCardDrop( event, ui ) {
    // Find the correct drag and drop element.
    let dragName = $(this).data('target');
    let dropField = ui.draggable.data('name');

    if (dragName == dropField) {
        // If the words match, disable draggable and droppable and place the element.
        ui.draggable.draggable( 'disable' );
        $(this).droppable( 'disable' );
        $(this).addClass("drop-sentence--success");
        ui.draggable.position( { of: $(this), my: 'center center', at: 'center center' } );
        ui.draggable.draggable( 'option', 'revert', false );
    }
}