jQuery(function() {
    var form = jQuery("#NoteForm");
    form.submit(function(e) {
        jQuery("#id_send").attr('disabled', true)

        jQuery("#ajaxwrapper").load(
            form.attr('action') + ' #ajaxwrapper',
            form.serializeArray(),
            function(responseText, responseStatus) {
                jQuery("#id_send").attr('disabled', false)
                if (responseText == 'success'){
                    window.location = '/'
                    alert('note was added successfully!');
                }
            }
        );
        e.preventDefault();
    });
});