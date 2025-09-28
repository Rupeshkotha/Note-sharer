// Wait until the document is fully loaded
$(document).ready(function() {
    
    $('form').submit(function(event) {
        
        let noteContent = $('textarea[name="note_content"]').val().trim();

        
        if (noteContent === '') {
         
            event.preventDefault();

           
            alert('Please enter some text before creating a note.');
        }
    });
});